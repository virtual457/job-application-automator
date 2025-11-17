"""
Quick Application Logger

Simple script to log applications after you apply.
Run after each application to track your progress.
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from application_tracker import ApplicationTracker


def quick_log():
    """Quick interactive logging"""
    
    print("\n" + "="*60)
    print("QUICK APPLICATION LOGGER")
    print("="*60 + "\n")
    
    tracker = ApplicationTracker()
    
    # Get input
    company = input("Company name: ")
    role = input("Role title: ")
    key_skills = input("Key skills required (comma-separated): ")
    location = input("Location (or press Enter for Remote): ") or "Remote"
    resume_type = input("Resume type used (backend/ml/data/algorithms/general): ") or "backend"
    referral_name = input("Referral name (or press Enter if none): ") or ""
    notes = input("Notes (optional): ") or ""
    
    # Add to tracker
    tracker.add_application(
        company=company,
        role=role,
        key_skills=key_skills,
        location=location,
        resume_type=resume_type,
        referral_name=referral_name,
        notes=notes
    )
    
    print(f"\n✅ Application logged!")
    
    # Show current stats
    tracker.display_summary()


if __name__ == "__main__":
    try:
        quick_log()
    except KeyboardInterrupt:
        print("\n\n❌ Cancelled")
    except Exception as e:
        print(f"\n❌ Error: {e}")
