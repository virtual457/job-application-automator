"""
Main CLI for Job Application Automator

Usage:
    python main.py generate-resume --company Salesforce --role backend
    python main.py batch-generate companies.yaml
    python main.py list-roles
"""

import click
from resume_generator import ResumeGenerator, list_available_roles
import yaml
from pathlib import Path
from colorama import init, Fore, Style

# Initialize colorama for colored output
init()


@click.group()
def cli():
    """Job Application Automator - Automate your 2026 co-op hunt"""
    pass


@cli.command()
@click.option('--company', required=True, help='Target company name (e.g., Salesforce, Microsoft)')
@click.option('--role', default='backend', help='Role type: backend, ml, data, algorithms, general')
@click.option('--format', default='docx', help='Output format: docx or pdf')
def generate_resume(company, role, format):
    """Generate a single tailored resume"""
    
    template_path = 'templates/base_resume.docx'
    config_path = 'config/resume_config.yaml'
    
    # Check if template exists
    if not Path(template_path).exists():
        click.echo(f"{Fore.RED}❌ Error: Template not found at {template_path}{Style.RESET_ALL}")
        click.echo(f"{Fore.YELLOW}💡 Create a base resume template first!{Style.RESET_ALL}")
        return
    
    try:
        generator = ResumeGenerator(template_path, config_path)
        output_path = generator.generate(company, role, format)
        
        click.echo(f"\n{Fore.GREEN}✅ Success!{Style.RESET_ALL}")
        click.echo(f"Resume generated: {Fore.CYAN}{output_path}{Style.RESET_ALL}")
        
    except Exception as e:
        click.echo(f"{Fore.RED}❌ Error: {e}{Style.RESET_ALL}")


@cli.command()
@click.argument('applications_file')
def batch_generate(applications_file):
    """
    Generate multiple resumes from a YAML file
    
    Example YAML format:
    ```
    applications:
      - company: Salesforce
        role_type: backend
      - company: ByteDance
        role_type: ml
    ```
    """
    
    template_path = 'templates/base_resume.docx'
    config_path = 'config/resume_config.yaml'
    
    # Load applications list
    try:
        with open(applications_file, 'r') as f:
            data = yaml.safe_load(f)
            applications = data.get('applications', [])
    except FileNotFoundError:
        click.echo(f"{Fore.RED}❌ Error: File not found: {applications_file}{Style.RESET_ALL}")
        return
    except yaml.YAMLError as e:
        click.echo(f"{Fore.RED}❌ Error parsing YAML: {e}{Style.RESET_ALL}")
        return
    
    if not applications:
        click.echo(f"{Fore.YELLOW}⚠️  No applications found in {applications_file}{Style.RESET_ALL}")
        return
    
    # Generate resumes
    try:
        generator = ResumeGenerator(template_path, config_path)
        results = generator.batch_generate(applications)
        
        # Show results
        successful = [r for r in results if r['status'] == 'success']
        failed = [r for r in results if r['status'] == 'failed']
        
        click.echo(f"\n{Fore.GREEN}✅ Generated {len(successful)} resumes{Style.RESET_ALL}")
        
        if failed:
            click.echo(f"{Fore.RED}❌ Failed: {len(failed)} resumes{Style.RESET_ALL}")
            for f in failed:
                click.echo(f"  - {f['company']}: {f['error']}")
        
        # Show stats
        stats = generator.get_stats()
        click.echo(f"\n{Fore.CYAN}📊 Total resumes generated: {stats['total_generated']}{Style.RESET_ALL}")
        
    except Exception as e:
        click.echo(f"{Fore.RED}❌ Error: {e}{Style.RESET_ALL}")


@cli.command()
def list_roles():
    """List all available role types"""
    
    config_path = 'config/resume_config.yaml'
    
    try:
        roles = list_available_roles(config_path)
        
        click.echo(f"\n{Fore.CYAN}📋 Available Role Types:{Style.RESET_ALL}\n")
        
        for role in roles:
            click.echo(f"  • {Fore.GREEN}{role}{Style.RESET_ALL}")
        
        click.echo(f"\n{Fore.YELLOW}Usage:{Style.RESET_ALL}")
        click.echo(f"  python main.py generate-resume --company Salesforce --role backend")
        
    except Exception as e:
        click.echo(f"{Fore.RED}❌ Error: {e}{Style.RESET_ALL}")


@cli.command()
def init():
    """Initialize the project structure"""
    
    click.echo(f"{Fore.CYAN}🚀 Initializing Job Application Automator...{Style.RESET_ALL}\n")
    
    # Check/create directories
    dirs = [
        'templates',
        'output/resumes',
        'config',
        'logs'
    ]
    
    for dir_path in dirs:
        p = Path(dir_path)
        if not p.exists():
            p.mkdir(parents=True, exist_ok=True)
            click.echo(f"{Fore.GREEN}✅ Created: {dir_path}{Style.RESET_ALL}")
        else:
            click.echo(f"{Fore.YELLOW}⏭️  Already exists: {dir_path}{Style.RESET_ALL}")
    
    # Check for base template
    template_path = Path('templates/base_resume.docx')
    if not template_path.exists():
        click.echo(f"\n{Fore.YELLOW}⚠️  No base resume template found{Style.RESET_ALL}")
        click.echo(f"💡 Copy your resume to: {Fore.CYAN}{template_path}{Style.RESET_ALL}")
    else:
        click.echo(f"\n{Fore.GREEN}✅ Base template exists{Style.RESET_ALL}")
    
    click.echo(f"\n{Fore.GREEN}✅ Initialization complete!{Style.RESET_ALL}")
    click.echo(f"\n{Fore.CYAN}Next steps:{Style.RESET_ALL}")
    click.echo("  1. Copy your base resume to templates/base_resume.docx")
    click.echo("  2. Run: python main.py list-roles")
    click.echo("  3. Generate a test resume: python main.py generate-resume --company TestCo --role backend")


@cli.command()
def stats():
    """Show generation statistics"""
    
    log_file = Path('output/generation_log.txt')
    
    if not log_file.exists():
        click.echo(f"{Fore.YELLOW}⚠️  No resumes generated yet{Style.RESET_ALL}")
        return
    
    # Read log file
    with open(log_file, 'r') as f:
        lines = f.readlines()
    
    # Parse statistics
    companies = {}
    roles = {}
    
    for line in lines:
        parts = line.strip().split('|')
        if len(parts) >= 3:
            company = parts[1].strip()
            role = parts[2].strip()
            
            companies[company] = companies.get(company, 0) + 1
            roles[role] = roles.get(role, 0) + 1
    
    click.echo(f"\n{Fore.CYAN}📊 Resume Generation Statistics{Style.RESET_ALL}\n")
    
    click.echo(f"{Fore.GREEN}Total Resumes Generated: {len(lines)}{Style.RESET_ALL}\n")
    
    click.echo(f"{Fore.YELLOW}By Role Type:{Style.RESET_ALL}")
    for role, count in sorted(roles.items(), key=lambda x: x[1], reverse=True):
        click.echo(f"  • {role:15s}: {count}")
    
    click.echo(f"\n{Fore.YELLOW}Top Companies:{Style.RESET_ALL}")
    for company, count in sorted(companies.items(), key=lambda x: x[1], reverse=True)[:10]:
        click.echo(f"  • {company:20s}: {count}")


if __name__ == '__main__':
    cli()
