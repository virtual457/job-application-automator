"""
LaTeX Resume Generator - Simple YAML to LaTeX Converter

Reads YAML configuration and generates clean LaTeX code for Overleaf.

Usage:
    python generate_latex.py

Output:
    output/generated_resume.tex (ready to paste into Overleaf)

Author: Chandan Resume Automation System
Last Updated: December 19, 2025
"""

import yaml
import re
from pathlib import Path
from typing import Dict, Any

try:
    from jinja2 import Environment, FileSystemLoader
except ImportError:
    print("❌ ERROR: jinja2 not installed")
    print("Install with: pip install jinja2")
    exit(1)


class LaTeXGenerator:
    """Generates LaTeX resume code from YAML using base template."""
    
    def __init__(self, yaml_path: str):
        self.yaml_path = Path(yaml_path)
        
        # Setup Jinja2 environment with LaTeX-safe delimiters
        template_dir = Path(__file__).parent / 'templates'
        self.env = Environment(
            loader=FileSystemLoader(str(template_dir)),
            block_start_string='((*',
            block_end_string='*))',
            variable_start_string='(((',
            variable_end_string=')))',
            comment_start_string='((=',
            comment_end_string='=))',
            trim_blocks=True,
            lstrip_blocks=True,
            autoescape=False  # We handle escaping manually
        )
        
        if not self.yaml_path.exists():
            raise FileNotFoundError(f"YAML config not found: {self.yaml_path}")
    
    def escape_latex(self, text: str) -> str:
        """
        Escape LaTeX special characters while preserving bold markers.
        
        Strategy:
        1. Protect **bold** markers with placeholders
        2. Escape LaTeX special chars (NOT backslash - YAML has LaTeX commands)
        3. Convert placeholders to \\textbf{}
        """
        if not isinstance(text, str):
            return str(text)
        
        # Step 1: Replace **text** with placeholders
        bold_pattern = r'\*\*([^*]+?)\*\*'
        bold_parts = []
        
        def replace_bold(match):
            bold_parts.append(match.group(1))
            return f"<<<BOLD{len(bold_parts)-1}>>>"
        
        text = re.sub(bold_pattern, replace_bold, text)
        
        # Step 2: Escape LaTeX special characters (NOT backslash!)
        latex_escapes = {
            '&': r'\&',
            '%': r'\%',
            '$': r'\$',
            '#': r'\#',
            '_': r'\_',
            '{': r'\{',
            '}': r'\}',
            '~': r'\textasciitilde{}',
            '^': r'\^{}',
        }
        
        for char, escaped in latex_escapes.items():
            text = text.replace(char, escaped)
        
        # Step 3: Convert placeholders to \textbf{}
        for i, bold_text in enumerate(bold_parts):
            # Escape content inside bold too
            escaped_bold = bold_text
            for char, escaped in latex_escapes.items():
                escaped_bold = escaped_bold.replace(char, escaped)
            
            text = text.replace(
                f"<<<BOLD{i}>>>",
                f"\\textbf{{{escaped_bold}}}"
            )
        
        return text
    
    def process_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Process YAML data: escape LaTeX chars and handle bold markers."""
        
        # Process header
        if 'header' in data:
            if 'name' in data['header']:
                data['header']['name'] = self.escape_latex(data['header']['name'])
            if 'title' in data['header']:
                data['header']['title'] = self.escape_latex(data['header']['title'])
            # Contact stays as-is (already LaTeX)
        
        # Process education (if dynamic)
        if 'education' in data:
            if 'ms_coursework' in data['education']:
                data['education']['ms_coursework'] = self.escape_latex(data['education']['ms_coursework'])
            if 'be_coursework' in data['education']:
                data['education']['be_coursework'] = self.escape_latex(data['education']['be_coursework'])
        
        # Process skills
        if 'skills' in data:
            for skill in data['skills']:
                skill['category'] = self.escape_latex(skill.get('category', ''))
                skill['items'] = self.escape_latex(skill.get('items', ''))
        
        # Process experience
        if 'experience' in data:
            for exp in data['experience']:
                exp['company'] = self.escape_latex(exp.get('company', ''))
                exp['role'] = self.escape_latex(exp.get('role', ''))
                exp['duration'] = self.escape_latex(exp.get('duration', ''))
                if 'bullets' in exp:
                    exp['bullets'] = [self.escape_latex(b) for b in exp['bullets']]
        
        # Process projects
        if 'projects' in data:
            for project in data['projects']:
                project['title'] = self.escape_latex(project.get('title', ''))
                project['tech'] = self.escape_latex(project.get('tech', ''))
                # github_link stays as-is (URL)
                if 'bullet1' in project:
                    project['bullet1'] = self.escape_latex(project['bullet1'])
                if 'bullet2' in project:
                    project['bullet2'] = self.escape_latex(project['bullet2'])
        
        return data
    
    def load_yaml(self) -> Dict[str, Any]:
        """Load and parse YAML configuration."""
        with open(self.yaml_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    
    def generate(self) -> str:
        """Main generation: YAML → LaTeX."""
        
        print("=" * 60)
        print("📄 LaTeX Resume Generator")
        print("=" * 60)
        
        # Load YAML
        print(f"\n📖 Reading YAML: {self.yaml_path.name}")
        data = self.load_yaml()
        company = data.get('company_name', 'Unknown')
        print(f"   Company: {company}")
        
        # Process data (escape LaTeX, handle bold)
        print("\n🔧 Processing data...")
        data = self.process_data(data)
        
        # Load template
        print("   Loading template: base_template.tex")
        template = self.env.get_template('base_template.tex')
        
        # Render template
        print("   Rendering template...")
        latex_code = template.render(**data)
        
        print(f"   Generated {len(latex_code)} characters")
        print("\n✅ LaTeX generation complete!")
        
        return latex_code


def main():
    """Main entry point."""
    
    # Paths
    base_dir = Path(__file__).parent
    yaml_path = base_dir / 'config' / 'current_application.yaml'
    output_path = base_dir / 'output' / 'generated_resume.tex'
    
    # Check YAML exists
    if not yaml_path.exists():
        print(f"❌ ERROR: YAML config not found")
        print(f"   Expected: {yaml_path}")
        print("\n📋 To create config:")
        print("   1. Copy: config/sample_config.yaml")
        print("   2. To:   config/current_application.yaml")
        print("   3. Edit with your data")
        return 1
    
    try:
        # Generate
        generator = LaTeXGenerator(yaml_path=str(yaml_path))
        latex_code = generator.generate()
        
        # Save
        output_path.parent.mkdir(exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(latex_code)
        
        print(f"\n💾 Saved LaTeX to: {output_path.name}")
        print(f"   Full path: {output_path.absolute()}")
        
        print("\n" + "=" * 60)
        print("🚀 Next Steps:")
        print("=" * 60)
        print("1. Open: output/generated_resume.tex")
        print("2. Copy all content (Ctrl+A, Ctrl+C)")
        print("3. Go to Overleaf → New blank project")
        print("4. Paste content")
        print("5. Download PDF")
        print("\n✨ Professional resume ready!")
        
        return 0
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == '__main__':
    import sys
    sys.exit(main())
