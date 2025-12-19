#!/usr/bin/env python3
"""
Resume YAML Validator

Validates current_application.yaml against constraints defined in config/constraints.yaml
Usage: python validate_yaml.py
"""

import yaml
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Any


class Colors:
    """ANSI color codes for terminal output"""
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    END = '\033[0m'


def count_bold_markers(text: str) -> int:
    """Count the number of bold markers (**text**) in a string"""
    return text.count('**') // 2


def load_yaml_file(filepath: Path) -> Dict:
    """Load and parse a YAML file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        print(f"{Colors.RED}❌ Error: File not found: {filepath}{Colors.END}")
        sys.exit(1)
    except yaml.YAMLError as e:
        print(f"{Colors.RED}❌ Error parsing YAML: {e}{Colors.END}")
        sys.exit(1)


def validate_summary(data: Dict, constraints: Dict) -> Tuple[bool, List[str]]:
    """Validate summary section"""
    errors = []
    summary = data.get('summary', '')

    if not summary:
        errors.append("Summary is missing")
        return False, errors

    # Character count (max only)
    char_count = len(summary)
    max_chars = constraints.get('max_chars', 999)

    if char_count > max_chars:
        errors.append(f"Character count {char_count} (max {max_chars})")

    # Bold markers (max only)
    bold_count = count_bold_markers(summary)
    max_bold = constraints.get('max_bold', 999)

    if bold_count > max_bold:
        errors.append(f"Bold markers {bold_count} (max {max_bold})")

    # Required keywords
    for keyword in constraints.get('required_keywords', []):
        if keyword not in summary:
            errors.append(f"Missing required keyword: '{keyword}'")

    return len(errors) == 0, errors


def validate_skills(data: Dict, constraints: Dict) -> Tuple[bool, List[str]]:
    """Validate skills section"""
    errors = []
    skills = data.get('skills', [])

    # Exact category count
    exact_count = constraints['exact_categories']
    if len(skills) != exact_count:
        errors.append(f"Category count {len(skills)} (must be exactly {exact_count})")

    # Validate each category
    for i, skill in enumerate(skills, 1):
        category_name = skill.get('category', f'Category {i}')
        items = skill.get('items', '')

        # Check category name length
        category_name_max = constraints.get('category_name_max_chars', 999)
        if len(category_name) > category_name_max:
            errors.append(f"{category_name}: category name {len(category_name)} chars (max {category_name_max})")

        # Check items length
        item_length = len(items)
        min_chars = constraints.get('items_min_chars', 0)  # Default to 0 if not specified
        max_chars = constraints.get('items_max_chars', 999)  # Default to 999 if not specified

        # Only check min if it's specified
        if min_chars > 0 and item_length < min_chars:
            errors.append(f"{category_name}: items {item_length} chars (minimum {min_chars})")

        # Only check max if specified
        if max_chars < 999 and item_length > max_chars:
            errors.append(f"{category_name}: items {item_length} chars (maximum {max_chars})")

    return len(errors) == 0, errors


def validate_experience(data: Dict, constraints: Dict) -> Tuple[bool, List[str]]:
    """Validate experience section"""
    errors = []
    experiences = data.get('experience', [])

    for exp in experiences:
        company = exp.get('company', 'Unknown Company')

        # Check if company has constraints defined
        if company not in constraints['companies']:
            continue

        company_constraints = constraints['companies'][company]

        # Validate required fields
        for field, expected_value in company_constraints.get('required_fields', {}).items():
            actual_value = exp.get(field, '')
            if actual_value != expected_value:
                errors.append(f"{company}: {field} mismatch (expected '{expected_value}', got '{actual_value}')")

        # Validate bullets
        bullets = exp.get('bullets', [])
        exact_bullets = company_constraints['exact_bullets']

        if len(bullets) != exact_bullets:
            errors.append(f"{company}: {len(bullets)} bullets (must be exactly {exact_bullets})")

        # Validate each bullet (max only)
        for i, bullet in enumerate(bullets, 1):
            bullet_length = len(bullet)
            bold_count = count_bold_markers(bullet)

            max_chars = company_constraints.get('bullet_max_chars', 999)
            max_bold = company_constraints.get('bullet_max_bold', 999)

            if bullet_length > max_chars:
                errors.append(f"{company} bullet {i}: {bullet_length} chars (max {max_chars})")

            if bold_count > max_bold:
                errors.append(f"{company} bullet {i}: {bold_count} bold (max {max_bold})")

    return len(errors) == 0, errors


def validate_projects(data: Dict, constraints: Dict) -> Tuple[bool, List[str]]:
    """Validate projects section"""
    errors = []
    projects = data.get('projects', [])

    # Exact project count
    exact_count = constraints['exact_count']
    if len(projects) != exact_count:
        errors.append(f"Project count {len(projects)} (must be exactly {exact_count})")

    # Validate each project
    for i, project in enumerate(projects, 1):
        title = project.get('title', f'Project {i}')

        # Check required fields
        for field in constraints.get('required_fields', []):
            if field not in project:
                errors.append(f"{title}: Missing required field '{field}'")

        # Tech line length
        tech = project.get('tech', '')
        tech_max = constraints['tech_max_chars']
        if len(tech) > tech_max:
            errors.append(f"{title}: Tech line {len(tech)} chars (max {tech_max})")

        # Validate bullet1 and bullet2
        for bullet_field in constraints.get('bullet_fields', []):
            bullet = project.get(bullet_field, '')

            if not bullet:
                errors.append(f"{title}: Missing '{bullet_field}'")
                continue

            bullet_length = len(bullet)
            bold_count = count_bold_markers(bullet)

            max_chars = constraints.get('bullet_max_chars', 999)
            max_bold = constraints.get('bullet_max_bold', 999)

            if bullet_length > max_chars:
                errors.append(f"{title} {bullet_field}: {bullet_length} chars (max {max_chars})")

            if bold_count > max_bold:
                errors.append(f"{title} {bullet_field}: {bold_count} bold (max {max_bold})")

    return len(errors) == 0, errors


def validate_header(data: Dict, constraints: Dict) -> Tuple[bool, List[str]]:
    """Validate header section"""
    errors = []
    header = data.get('header', {})

    # Check required fields
    for field in constraints.get('required_fields', []):
        if field not in header:
            errors.append(f"Header: Missing required field '{field}'")

    # Check exact values if specified
    if 'name_exact' in constraints and header.get('name') != constraints['name_exact']:
        errors.append(f"Header name mismatch (expected '{constraints['name_exact']}')")

    if 'contact_exact' in constraints and header.get('contact') != constraints['contact_exact']:
        errors.append(f"Header contact mismatch")

    return len(errors) == 0, errors


def print_section_result(section_name: str, passed: bool, errors: List[str]):
    """Print validation results for a section"""
    status = f"{Colors.GREEN}[PASS]{Colors.END}" if passed else f"{Colors.RED}[FAIL]{Colors.END}"
    print(f"\n{Colors.BOLD}{section_name}{Colors.END}: {status}")

    if errors:
        for error in errors:
            print(f"  {Colors.RED}-{Colors.END} {error}")


def print_summary_stats(data: Dict):
    """Print summary statistics"""
    print(f"\n{Colors.BLUE}{'='*60}{Colors.END}")
    print(f"{Colors.BOLD}Summary Statistics:{Colors.END}")
    print(f"{Colors.BLUE}{'='*60}{Colors.END}")

    summary = data.get('summary', '')
    print(f"Summary: {len(summary)} chars, {count_bold_markers(summary)} bold markers")

    skills = data.get('skills', [])
    print(f"\nSkills: {len(skills)} categories")
    for skill in skills:
        items_len = len(skill.get('items', ''))
        print(f"  - {skill.get('category', 'Unknown')}: {items_len} chars")

    experiences = data.get('experience', [])
    print(f"\nExperience: {len(experiences)} companies")
    for exp in experiences:
        company = exp.get('company', 'Unknown')
        bullets = exp.get('bullets', [])
        print(f"  - {company}: {len(bullets)} bullets")
        for i, bullet in enumerate(bullets, 1):
            print(f"    - Bullet {i}: {len(bullet)} chars, {count_bold_markers(bullet)} bold")

    projects = data.get('projects', [])
    print(f"\nProjects: {len(projects)} projects")
    for proj in projects:
        title = proj.get('title', 'Unknown')
        tech_len = len(proj.get('tech', ''))
        b1_len = len(proj.get('bullet1', ''))
        b2_len = len(proj.get('bullet2', ''))
        b1_bold = count_bold_markers(proj.get('bullet1', ''))
        b2_bold = count_bold_markers(proj.get('bullet2', ''))
        print(f"  - {title}:")
        print(f"    - Tech: {tech_len} chars")
        print(f"    - Bullet1: {b1_len} chars, {b1_bold} bold")
        print(f"    - Bullet2: {b2_len} chars, {b2_bold} bold")


def main():
    """Main validation function"""
    # Set up paths
    base_dir = Path(__file__).parent
    yaml_file = base_dir / 'config' / 'current_application.yaml'
    constraints_file = base_dir / 'config' / 'constraints.yaml'

    print(f"{Colors.BOLD}{Colors.BLUE}")
    print("=" * 60)
    print("         RESUME YAML VALIDATION TOOL")
    print("=" * 60)
    print(f"{Colors.END}")

    # Load files
    print(f"\n{Colors.YELLOW}Loading files...{Colors.END}")
    print(f"  - YAML: {yaml_file}")
    print(f"  - Constraints: {constraints_file}")

    data = load_yaml_file(yaml_file)
    constraints = load_yaml_file(constraints_file)

    # Run validations
    print(f"\n{Colors.BOLD}Running validations...{Colors.END}")

    all_passed = True

    # Validate header
    passed, errors = validate_header(data, constraints.get('header', {}))
    print_section_result("Header", passed, errors)
    all_passed = all_passed and passed

    # Validate summary
    passed, errors = validate_summary(data, constraints.get('summary', {}))
    print_section_result("Summary", passed, errors)
    all_passed = all_passed and passed

    # Validate skills
    passed, errors = validate_skills(data, constraints.get('skills', {}))
    print_section_result("Skills", passed, errors)
    all_passed = all_passed and passed

    # Validate experience
    passed, errors = validate_experience(data, constraints.get('experience', {}))
    print_section_result("Experience", passed, errors)
    all_passed = all_passed and passed

    # Validate projects
    passed, errors = validate_projects(data, constraints.get('projects', {}))
    print_section_result("Projects", passed, errors)
    all_passed = all_passed and passed

    # Print detailed statistics (commented out - too verbose for reviser feedback)
    # print_summary_stats(data)

    # Final result
    print(f"\n{Colors.BLUE}{'='*60}{Colors.END}")
    if all_passed:
        print(f"{Colors.GREEN}{Colors.BOLD}>>> ALL VALIDATIONS PASSED <<<{Colors.END}")
        print(f"{Colors.GREEN}Resume is ready for generation!{Colors.END}")
        sys.exit(0)
    else:
        print(f"{Colors.RED}{Colors.BOLD}>>> VALIDATION FAILED <<<{Colors.END}")
        print(f"{Colors.RED}Please fix the errors above before generating resume.{Colors.END}")
        sys.exit(1)


if __name__ == '__main__':
    main()
