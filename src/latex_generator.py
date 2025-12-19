"""
LaTeX Resume Generator - Compiles YAML to Professional PDF

Reads config/current_application.yaml and generates output/Generated_Resume.pdf
using LaTeX compilation with Jinja2 templating.

Requirements:
    - MiKTeX (Windows) or TeX Live (Mac/Linux) installed
    - pip install latex jinja2 pyyaml

Usage:
    python src/latex_generator.py

Author: Chandan Resume Automation System
Last Updated: December 15, 2025
"""

import yaml
import re
import sys
from pathlib import Path
from typing import Dict, Any

try:
    from latex import build_pdf
    from latex.jinja2 import make_env
except ImportError:
    print("❌ ERROR: 'latex' package not installed.")
    print("Install with: pip install latex")
    sys.exit(1)

try:
    from jinja2 import Environment, FileSystemLoader
except ImportError:
    print("❌ ERROR: 'jinja2' package not installed.")
    print("Install with: pip install jinja2")
    sys.exit(1)


class LatexResumeGenerator:
    """Generates professional PDF resumes from YAML using LaTeX compilation."""
    
    def __init__(self, yaml_path: str, template_path: str, output_path: str):
        self.yaml_path = Path(yaml_path)
        self.template_path = Path(template_path)
        self.output_path = Path(output_path)
        
        # Verify paths exist
        if not self.yaml_path.exists():
            raise FileNotFoundError(f"YAML config not found: {self.yaml_path}")
        if not self.template_path.exists():
            raise FileNotFoundError(f"Template not found: {self.template_path}")
    
    def escape_latex(self, text: str) -> str:
        """
        Escape LaTeX special characters while preserving bold markers.
        
        Strategy:
        1. Replace ** markers with placeholders
        2. Escape LaTeX special chars
        3. Convert placeholders to \textbf{}
        """
        if not isinstance(text, str):
            return str(text)
        
        # Step 1: Replace **text** with placeholder
        # Use unique placeholders that won't conflict with escaping
        bold_pattern = r'\*\*([^*]+?)\*\*'
        bold_parts = []
        
        def replace_bold(match):
            bold_parts.append(match.group(1))
            return f"BOLDMARKER{len(bold_parts)-1}BOLDMARKER"
        
        text = re.sub(bold_pattern, replace_bold, text)
        
        # Step 2: Escape LaTeX special characters
        latex_special_chars = {
            '&': r'\&',
            '%': r'\%',
            '$': r'\$',
            '#': r'\#',
            '_': r'\_',
            '{': r'\{',
            '}': r'\}',
            '~': r'\textasciitilde{}',
            '^': r'\^{}',
            '\\': r'\textbackslash{}',
        }
        
        for char, escaped in latex_special_chars.items():
            text = text.replace(char, escaped)
        
        # Step 3: Convert placeholders to \textbf{}
        for i, bold_text in enumerate(bold_parts):
            # Escape the content inside bold markers too
            escaped_bold = bold_text
            for char, escaped in latex_special_chars.items():
                escaped_bold = escaped_bold.replace(char, escaped)
            
            text = text.replace(
                f"BOLDMARKER{i}BOLDMARKER",
                f"\\textbf{{{escaped_bold}}}"
            )
        
        return text
    
    def process_yaml_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Process YAML data: escape LaTeX chars and handle bold markers."""
        
        # Process summary (contains bold markers)
        if 'summary' in data:
            data['summary'] = self.escape_latex(data['summary'])
        
        # Process header
        if 'header' in data:
            for key in ['name', 'title', 'contact']:
                if key in data['header']:
                    # Don't escape contact info (contains hyperref elements)
                    if key == 'contact':
                        # Just escape special chars, no bold processing
                        data['header'][key] = data['header'][key].replace('&', r'\&')
                    else:
                        data['header'][key] = self.escape_latex(data['header'][key])
        
        # Process skills (no bold markers, just escape)
        if 'skills' in data:
            for skill in data['skills']:
                skill['category'] = self.escape_latex(skill['category'])
                skill['items'] = self.escape_latex(skill['items'])
        
        # Process experience bullets (contain bold markers)
        if 'experience' in data:
            for exp in data['experience']:
                exp['company'] = self.escape_latex(exp['company'])
                exp['role'] = self.escape_latex(exp['role'])
                exp['location'] = self.escape_latex(exp['location'])
                exp['duration'] = self.escape_latex(exp['duration'])
                
                if 'bullets' in exp:
                    exp['bullets'] = [self.escape_latex(b) for b in exp['bullets']]
        
        # Process projects (contain bold markers)
        if 'projects' in data:
            for project in data['projects']:
                project['title'] = self.escape_latex(project['title'])
                project['tech'] = self.escape_latex(project['tech'])
                # GitHub stays as-is (literal string in template)
                
                if 'bullet1' in project:
                    project['bullet1'] = self.escape_latex(project['bullet1'])
                if 'bullet2' in project:
                    project['bullet2'] = self.escape_latex(project['bullet2'])
        
        return data
    
    def load_yaml(self) -> Dict[str, Any]:
        """Load and parse YAML configuration."""
        with open(self.yaml_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    
    def render_template(self, data: Dict[str, Any]) -> str:
        """Render Jinja2 LaTeX template with data."""
        
        # Create Jinja2 environment for LaTeX
        # Use ((( ))) delimiters to avoid conflicts with LaTeX { }
        env = Environment(
            loader=FileSystemLoader(self.template_path.parent),
            block_start_string='((*',
            block_end_string='*))',
            variable_start_string='(((',
            variable_end_string='))))',
            comment_start_string='((=',
            comment_end_string='=))',
            trim_blocks=True,
            lstrip_blocks=True,
            autoescape=False  # We handle escaping manually
        )
        
        template = env.get_template(self.template_path.name)
        return template.render(**data)
    
    def compile_to_pdf(self, latex_source: str) -> bytes:
        """Compile LaTeX source to PDF using pdflatex."""
        try:
            print("🔨 Compiling LaTeX to PDF...")
            pdf = build_pdf(latex_source, builder='pdflatex')
            return pdf
        except Exception as e:
            print(f"❌ LaTeX compilation failed!")
            print(f"Error: {str(e)}")
            
            # Try to extract useful error info
            error_str = str(e)
            if 'line' in error_str.lower():
                print("\n📋 Error details:")
                print(error_str)
            
            # Save problematic .tex file for debugging
            debug_path = self.output_path.parent / 'debug_resume.tex'
            with open(debug_path, 'w', encoding='utf-8') as f:
                f.write(latex_source)
            print(f"\n💾 Saved debug LaTeX to: {debug_path}")
            print("   You can compile manually to see full errors:")
            print(f"   pdflatex {debug_path}")
            
            raise
    
    def generate(self):
        """Main generation workflow: YAML → LaTeX → PDF"""
        
        print("=" * 60)
        print("📄 LaTeX Resume Generator")
        print("=" * 60)
        
        # Step 1: Load YAML
        print(f"\n📖 Reading YAML: {self.yaml_path.name}")
        data = self.load_yaml()
        company = data.get('company_name', 'Unknown')
        print(f"   Company: {company}")
        
        # Step 2: Process data (escape LaTeX, handle bold)
        print("\n🔧 Processing data (escaping LaTeX chars, handling bold markers)...")
        data = self.process_yaml_data(data)
        
        # Step 3: Render template
        print(f"\n📝 Rendering template: {self.template_path.name}")
        latex_source = self.render_template(data)
        print(f"   Generated {len(latex_source)} characters of LaTeX")
        
        # Step 4: Compile to PDF
        pdf = self.compile_to_pdf(latex_source)
        
        # Step 5: Save PDF
        print(f"\n💾 Saving PDF: {self.output_path}")
        with open(self.output_path, 'wb') as f:
            f.write(bytes(pdf))
        
        file_size = self.output_path.stat().st_size / 1024  # KB
        print(f"   File size: {file_size:.1f} KB")
        
        print("\n" + "=" * 60)
        print("✅ SUCCESS! Resume generated successfully!")
        print("=" * 60)
        print(f"\n📂 Output: {self.output_path.absolute()}")


def main():
    """Main entry point."""
    
    # Define paths
    base_dir = Path(__file__).parent.parent
    yaml_path = base_dir / 'config' / 'current_application.yaml'
    template_path = base_dir / 'templates' / 'resume_latex_template.tex'
    output_path = base_dir / 'output' / 'Generated_Resume.pdf'
    
    # Ensure output directory exists
    output_path.parent.mkdir(exist_ok=True)
    
    try:
        generator = LatexResumeGenerator(
            yaml_path=str(yaml_path),
            template_path=str(template_path),
            output_path=str(output_path)
        )
        
        generator.generate()
        
        # Try to open the PDF (Windows)
        try:
            import os
            os.startfile(str(output_path.absolute()))
        except:
            pass  # Non-Windows or permission issues
        
    except FileNotFoundError as e:
        print(f"❌ ERROR: {e}")
        print("\nMake sure you have:")
        print("  - config/current_application.yaml")
        print("  - templates/resume_latex_template.tex")
        sys.exit(1)
    
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        print("\nTroubleshooting:")
        print("  1. Check if pdflatex is installed: pdflatex --version")
        print("  2. See LATEX_SETUP.md for installation instructions")
        print("  3. Check debug_resume.tex for LaTeX syntax errors")
        sys.exit(1)


if __name__ == '__main__':
    main()
