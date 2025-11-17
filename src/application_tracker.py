"""
Application Tracker

Track all job applications in one place with dates, companies, roles, and key requirements.
"""

import pandas as pd
from datetime import datetime
from pathlib import Path
import yaml


class ApplicationTracker:
    """Track job applications with key details"""
    
    def __init__(self, tracker_file='data/applications.csv'):
        self.tracker_file = Path(tracker_file)
        self.tracker_file.parent.mkdir(parents=True, exist_ok=True)
        
        # Load existing data or create new
        if self.tracker_file.exists():
            self.df = pd.read_csv(self.tracker_file)
        else:
            self.df = pd.DataFrame(columns=[
                'date_applied',
                'company',
                'role',
                'location',
                'key_skills_required',
                'resume_type',
                'status',
                'referral_requested',
                'referral_name',
                'notes'
            ])
    
    def add_application(self, company, role, key_skills, location='Remote', 
                       resume_type='backend', referral_name='', notes=''):
        """Add a new application to tracker"""
        
        new_row = {
            'date_applied': datetime.now().strftime('%Y-%m-%d'),
            'company': company,
            'role': role,
            'location': location,
            'key_skills_required': key_skills,
            'resume_type': resume_type,
            'status': 'Applied',
            'referral_requested': 'Yes' if referral_name else 'No',
            'referral_name': referral_name,
            'notes': notes
        }
        
        # Add to dataframe
        self.df = pd.concat([self.df, pd.DataFrame([new_row])], ignore_index=True)
        
        # Save
        self.save()
        
        print(f"✅ Added: {company} - {role}")
        return new_row
    
    def save(self):
        """Save tracker to CSV"""
        self.df.to_csv(self.tracker_file, index=False)
    
    def get_stats(self):
        """Get application statistics"""
        return {
            'total_applications': len(self.df),
            'by_status': self.df['status'].value_counts().to_dict(),
            'by_resume_type': self.df['resume_type'].value_counts().to_dict(),
            'with_referrals': self.df['referral_requested'].value_counts().to_dict()
        }
    
    def display_summary(self):
        """Display summary of applications"""
        stats = self.get_stats()
        
        print("\n" + "="*60)
        print("APPLICATION TRACKER SUMMARY")
        print("="*60)
        print(f"\n📊 Total Applications: {stats['total_applications']}")
        
        print(f"\n📈 By Status:")
        for status, count in stats['by_status'].items():
            print(f"  • {status}: {count}")
        
        print(f"\n📝 By Resume Type:")
        for rtype, count in stats['by_resume_type'].items():
            print(f"  • {rtype}: {count}")
        
        print(f"\n🤝 Referrals:")
        for ref, count in stats['with_referrals'].items():
            print(f"  • {ref}: {count}")
        
        print("\n" + "="*60)
    
    def export_to_excel(self, output_file='data/applications.xlsx'):
        """Export to Excel for easier viewing"""
        self.df.to_excel(output_file, index=False)
        print(f"✅ Exported to: {output_file}")


if __name__ == "__main__":
    # Test the tracker
    tracker = ApplicationTracker()
    
    # Example: Add an application
    tracker.add_application(
        company="IBM",
        role="Software Developer Intern - EDA",
        key_skills="C++, Java, Python, Algorithms, AI/ML, Testing",
        location="Remote",
        resume_type="algorithms",
        notes="Focus on algorithms and testing discipline"
    )
    
    tracker.display_summary()
