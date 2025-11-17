"""
Application Tracker Viewer

View your application history in a clean table format.
"""

import pandas as pd
from pathlib import Path
import sys


def view_applications():
    """Display all applications in a formatted table"""
    
    tracker_file = Path('data/applications.csv')
    
    if not tracker_file.exists():
        print("❌ No applications tracked yet!")
        print("💡 Use quick_log.py to start tracking applications")
        return
    
    # Load data
    df = pd.read_csv(tracker_file)
    
    print("\n" + "="*100)
    print("APPLICATION TRACKER")
    print("="*100 + "\n")
    
    # Display summary stats
    print(f"📊 TOTAL APPLICATIONS: {len(df)}\n")
    
    print(f"📈 BY STATUS:")
    for status, count in df['status'].value_counts().items():
        print(f"  • {status}: {count}")
    
    print(f"\n📝 BY RESUME TYPE:")
    for rtype, count in df['resume_type'].value_counts().items():
        print(f"  • {rtype}: {count}")
    
    print(f"\n🤝 WITH REFERRALS: {df['referral_requested'].value_counts().get('Yes', 0)}")
    
    print("\n" + "="*100)
    print("DETAILED VIEW")
    print("="*100 + "\n")
    
    # Display table
    display_cols = ['date_applied', 'company', 'role', 'key_skills_required', 'resume_type', 'status']
    
    # Set display options for better formatting
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 50)
    
    print(df[display_cols].to_string(index=False))
    
    print("\n" + "="*100)
    
    # Recent applications
    if len(df) > 0:
        print("\n🕐 MOST RECENT APPLICATIONS:\n")
        recent = df.sort_values('date_applied', ascending=False).head(5)
        for _, row in recent.iterrows():
            print(f"  • {row['date_applied']} - {row['company']:20s} - {row['role']}")
    
    print("\n")


def export_to_excel():
    """Export to Excel for easier viewing"""
    
    tracker_file = Path('data/applications.csv')
    output_file = Path('data/applications.xlsx')
    
    if not tracker_file.exists():
        print("❌ No applications to export!")
        return
    
    df = pd.read_csv(tracker_file)
    df.to_excel(output_file, index=False, sheet_name='Applications')
    
    print(f"✅ Exported to: {output_file}")
    print(f"📊 Total applications: {len(df)}")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'excel':
        export_to_excel()
    else:
        view_applications()
