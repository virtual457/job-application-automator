"""
Simple Resume Generator

Reads content from config/current_application.yaml
Applies it to templates/Chandan_Resume_Format.docx
Saves to output/Generated_Resume.docx

Usage:
    python simple_generator.py
"""

from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_TAB_ALIGNMENT, WD_TAB_LEADER
from docx.oxml.shared import OxmlElement
from docx.oxml.ns import qn
import yaml
from pathlib import Path
import os
import time


def add_text_with_bold_markers(paragraph, text, font_size=10, base_bold=False):
    """
    Add text with **bold** markers.
    Example: "Built **AWS Lambda** pipeline" → "Built AWS Lambda pipeline" (with AWS Lambda bold)
    
    Args:
        paragraph: The Word paragraph to add text to
        text: Text with **markers** for bold sections
        font_size: Font size for all text
        base_bold: If True, non-marked text is also bold (marked text becomes non-bold)
    """
    parts = text.split('**')
    
    for i, part in enumerate(parts):
        if not part:  # Skip empty parts
            continue
            
        run = paragraph.add_run(part)
        run.font.size = Pt(font_size)
        
        # Even indices (0, 2, 4...) = normal text
        # Odd indices (1, 3, 5...) = text between ** markers = bold
        if i % 2 == 1:
            run.bold = True
        else:
            run.bold = base_bold


def add_hyperlink(paragraph, text, url, font_size=None, bold=False, italic=False):
    """
    Add a hyperlink to a paragraph.
    Returns the hyperlink run so you can format it.
    """
    # Create the hyperlink element
    hyperlink = OxmlElement('w:hyperlink')
    hyperlink.set(qn('r:id'), paragraph.part.relate_to(url, 'http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink', is_external=True))
    
    # Create a new run for the hyperlink
    new_run = OxmlElement('w:r')
    rPr = OxmlElement('w:rPr')
    
    # Add bold if specified
    if bold:
        b = OxmlElement('w:b')
        rPr.append(b)
    
    # Add italic if specified
    if italic:
        i = OxmlElement('w:i')
        rPr.append(i)
    
    # Add underline and color (blue) for hyperlink style
    u = OxmlElement('w:u')
    u.set(qn('w:val'), 'single')
    rPr.append(u)
    
    color = OxmlElement('w:color')
    color.set(qn('w:val'), '0563C1')  # Blue color
    rPr.append(color)
    
    # Add font size if specified
    if font_size:
        sz = OxmlElement('w:sz')
        sz.set(qn('w:val'), str(font_size * 2))  # Word uses half-points
        rPr.append(sz)
    
    new_run.append(rPr)
    new_run.text = text
    hyperlink.append(new_run)
    
    paragraph._element.append(hyperlink)
    
    return hyperlink


def find_paragraph_by_text(doc, search_text):
    """Find a paragraph that contains the search text"""
    for i, para in enumerate(doc.paragraphs):
        if search_text in para.text:
            return i
    return None


def close_all_word_applications():
    """Close all Word applications using taskkill"""
    print("📋 Closing all Word applications...")
    try:
        os.system("taskkill /F /IM WINWORD.EXE >nul 2>&1")
        time.sleep(1.5)
        print("   ✅ Word closed\n")
        return True
    except Exception as e:
        print(f"   ⚠️  Could not close Word: {e}\n")
        return False


def update_header(doc, header_data):
    """Update the first 3 paragraphs (name, title, contact with hyperlinks)"""
    print("📝 Updating header...")
    
    if len(doc.paragraphs) >= 3:
        # Line 1: Name
        doc.paragraphs[0].text = header_data['name']
        
        # Line 2: Title  
        doc.paragraphs[1].text = header_data['title']
        
        # Line 3: Contact info with hyperlinks
        contact_para = doc.paragraphs[2]
        contact_para.clear()
        
        # Phone number (plain text)
        run = contact_para.add_run("+1 (857) 421-7469; ")
        run.font.size = Pt(10)
        
        # Email (hyperlink)
        add_hyperlink(contact_para, "chandan.keelara@gmail.com", "mailto:chandan.keelara@gmail.com", font_size=10)
        contact_para.add_run("; ")
        
        # LinkedIn (hyperlink)
        add_hyperlink(contact_para, "LinkedIn", "https://www.linkedin.com/in/chandan-gowda-k-s-765194186/", font_size=10)
        contact_para.add_run("; ")
        
        # Portfolio (hyperlink)
        add_hyperlink(contact_para, "Portfolio", "https://virtual457.github.io/", font_size=10)
        contact_para.add_run("; ")
        
        # GitHub (hyperlink)
        add_hyperlink(contact_para, "GitHub", "https://github.com/virtual457", font_size=10)
        contact_para.add_run(";")
        
        print("   ✅ Header updated (with hyperlinks)")
    else:
        print("   ⚠️  Warning: Not enough paragraphs for header")


def update_summary(doc, summary_text):
    """Find and update the summary paragraph with bold marker support"""
    print("📝 Updating summary...")
    
    # Find the paragraph that starts with "Software Engineer and MS CS student"
    for i, para in enumerate(doc.paragraphs):
        if para.text.strip().startswith("Software Engineer and MS CS student"):
            # Clear existing runs
            para.clear()
            # Add text with bold marker support
            add_text_with_bold_markers(para, summary_text, font_size=10)
            print("   ✅ Summary updated (with bold markers)")
            return
    
    print("   ⚠️  Warning: Could not find summary paragraph")


def update_skills(doc, skills_list):
    """Update the TECHNICAL SKILLS section with dynamic tab alignment"""
    print("📝 Updating technical skills...")
    
    # Find "TECHNICAL SKILLS" heading
    skills_idx = find_paragraph_by_text(doc, "TECHNICAL SKILLS")
    
    if skills_idx is None:
        print("   ⚠️  Warning: Could not find TECHNICAL SKILLS section")
        return
    
    # Calculate dynamic tab position based on longest category
    max_category_length = max(len(skill['category']) for skill in skills_list)
    
    # Estimate inches needed:
    # Average char width in 10pt Calibri bold - using 0.07 inches per char for tighter spacing
    # No gap - items start right after longest category
    estimated_width = max_category_length * 0.07
    tab_position = estimated_width
    
    print(f"   📏 Longest category: '{max(skills_list, key=lambda x: len(x['category']))['category']}' ({max_category_length} chars)")
    print(f"   📐 Tab position: {tab_position:.2f} inches (0.07 in/char, no gap)")
    
    # Update the next 7 paragraphs with skills
    for i, skill in enumerate(skills_list):
        para_idx = skills_idx + 1 + i
        if para_idx < len(doc.paragraphs):
            para = doc.paragraphs[para_idx]
            para.clear()
            
            # Set tab stop at calculated position
            tab_stops = para.paragraph_format.tab_stops
            tab_stops.add_tab_stop(Inches(tab_position), WD_TAB_ALIGNMENT.LEFT)
            
            # Add category (bold)
            category_run = para.add_run(skill['category'])
            category_run.bold = True
            category_run.font.size = Pt(10)
            
            # Add single tab (will align at calculated position)
            para.add_run("\t")
            
            # Add items (not bold)
            items_run = para.add_run(skill['items'])
            items_run.bold = False
            items_run.font.size = Pt(10)
    
    print(f"   ✅ Updated {len(skills_list)} skill categories (dynamic alignment)")


def update_projects(doc, projects_list):
    """Update the PROJECTS section with GitHub hyperlinks"""
    print("📝 Updating projects...")
    
    # GitHub URLs for projects
    github_urls = {
        "Dino Game Deep RL Agent": "https://github.com/virtual457/dino-game-AI",
        "Orion PaaS": "https://github.com/virtual457/Orion-platform",
        "Orion Platform": "https://github.com/virtual457/Orion-platform",
        "Calendly - Calendar Management System": "https://github.com/virtual457/Calendly",
        "Calendly": "https://github.com/virtual457/Calendly",
        "Maritime Logistics Platform": "https://github.com/virtual457/Port-Management-System",
        "Port Management System": "https://github.com/virtual457/Port-Management-System",
        "Large Scale Data Analysis": "https://github.com/virtual457/Data-analysis-on-pubg",
        "Data Analysis on PUBG": "https://github.com/virtual457/Data-analysis-on-pubg",
        "Face Recognition & Validation System": "https://github.com/virtual457/Recognition-and-Validation-of-Faces-using-Machine-Learning-and-Image-Processing",
        "Online Examination System": "https://github.com/virtual457/Online-examination-using-mongodb"
    }
    
    # Find "PROJECTS" heading
    projects_idx = find_paragraph_by_text(doc, "PROJECTS")
    
    if projects_idx is None:
        print("   ⚠️  Warning: Could not find PROJECTS section")
        return
    
    current_para = projects_idx + 1
    
    for project in projects_list:
        if current_para >= len(doc.paragraphs):
            print(f"   ⚠️  Warning: Not enough paragraphs for project: {project['title']}")
            break
        
        # Update title line with hyperlinked GitHub
        para = doc.paragraphs[current_para]
        para.clear()
        
        # Add project title as hyperlink (BOLD)
        if project['title'] in github_urls:
            add_hyperlink(para, project['title'], github_urls[project['title']], font_size=10, bold=True)
        else:
            title_run = para.add_run(project['title'])
            title_run.bold = True
            title_run.font.size = Pt(10)
        
        para.add_run(" | ")
        
        # Add tech stack (BOLD ITALIC)
        tech_run = para.add_run(project['tech'])
        tech_run.bold = True
        tech_run.italic = True
        tech_run.font.size = Pt(10)
        
        para.add_run(" | ")
        
        # Add GitHub text (also hyperlink)
        if project['title'] in github_urls:
            add_hyperlink(para, "GitHub", github_urls[project['title']], font_size=10)
        else:
            github_run = para.add_run("GitHub")
            github_run.font.size = Pt(10)
        
        current_para += 1
        
        # Update bullet 1 (template already has bullet)
        if current_para < len(doc.paragraphs):
            para = doc.paragraphs[current_para]
            para.clear()
            add_text_with_bold_markers(para, project['bullet1'], font_size=10)
            current_para += 1
        
        # Update bullet 2 (template already has bullet)
        if current_para < len(doc.paragraphs):
            para = doc.paragraphs[current_para]
            para.clear()
            add_text_with_bold_markers(para, project['bullet2'], font_size=10)
            current_para += 1
    
    print(f"   ✅ Updated {len(projects_list)} projects (with GitHub hyperlinks)")


def open_in_word(file_path):
    """Open the generated resume in Word"""
    print("\n📂 Opening resume in Word...")
    try:
        os.startfile(str(file_path))
        print("   ✅ Resume opened in Word")
        return True
    except Exception as e:
        print(f"   ⚠️  Could not open Word: {e}")
        return False


def generate_resume():
    """Main function to generate resume"""
    
    print("\n" + "="*60)
    print("SIMPLE RESUME GENERATOR")
    print("="*60 + "\n")
    
    # Close all Word applications FIRST
    close_all_word_applications()
    
    # Paths
    yaml_path = Path("config/current_application.yaml")
    template_path = Path("templates/Chandan_Resume_Format.docx")
    output_path = Path("output/Generated_Resume.docx")
    
    # Check if files exist
    if not yaml_path.exists():
        print(f"❌ Error: YAML file not found at {yaml_path}")
        return
    
    if not template_path.exists():
        print(f"❌ Error: Template not found at {template_path}")
        print("💡 Make sure Chandan_Resume_Format.docx is in templates/ folder")
        return
    
    # Create output directory
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Load content from YAML
    print("📂 Loading content from YAML...")
    with open(yaml_path, 'r') as f:
        content = yaml.safe_load(f)
    print("   ✅ Content loaded\n")
    
    # Load Word template
    print("📂 Loading Word template...")
    doc = Document(template_path)
    print(f"   ✅ Template loaded ({len(doc.paragraphs)} paragraphs)\n")
    
    # Update each section
    update_header(doc, content['header'])
    update_summary(doc, content['summary'])
    update_skills(doc, content['skills'])
    update_projects(doc, content['projects'])
    
    # Save output
    print("\n💾 Saving generated resume...")
    doc.save(str(output_path))
    print(f"   ✅ Saved to: {output_path}")
    
    # Open in Word
    open_in_word(output_path)
    
    print("\n" + "="*60)
    print("✅ RESUME GENERATION COMPLETE!")
    print("="*60)
    print(f"\n📄 Output file: {output_path.absolute()}")
    print("\n💡 Next steps:")
    print("   1. Review the formatting in Word")
    print("   2. Make manual adjustments if needed")
    print("   3. Save as PDF and apply!")


if __name__ == "__main__":
    try:
        generate_resume()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
