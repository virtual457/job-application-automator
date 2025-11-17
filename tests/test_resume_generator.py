"""
Test Resume Generator Module

Run with: python -m pytest tests/test_resume_generator.py
Or simply: python tests/test_resume_generator.py
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from resume_generator import ResumeGenerator, list_available_roles
import yaml


def test_list_roles():
    """Test that we can list available roles"""
    print("Testing list_available_roles()...")
    
    config_path = Path(__file__).parent.parent / 'config' / 'resume_config.yaml'
    roles = list_available_roles(str(config_path))
    
    assert len(roles) > 0, "Should have at least one role defined"
    assert 'backend' in roles, "Should have 'backend' role"
    assert 'ml' in roles, "Should have 'ml' role"
    
    print(f"✅ Found {len(roles)} roles: {roles}")


def test_config_loading():
    """Test that config file is valid YAML"""
    print("\nTesting config file loading...")
    
    config_path = Path(__file__).parent.parent / 'config' / 'resume_config.yaml'
    
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    
    assert 'roles' in config, "Config should have 'roles' key"
    
    # Check each role has required fields
    for role_name, role_config in config['roles'].items():
        assert 'header' in role_config, f"Role {role_name} missing 'header'"
        assert 'summary' in role_config, f"Role {role_name} missing 'summary'"
        assert 'skills' in role_config, f"Role {role_name} missing 'skills'"
        assert 'projects' in role_config, f"Role {role_name} missing 'projects'"
        
        # Check summary has {company} placeholder
        assert '{company}' in role_config['summary'], f"Role {role_name} summary should have {{company}} placeholder"
    
    print(f"✅ Config valid with {len(config['roles'])} roles")


def test_generator_init():
    """Test that generator can be initialized"""
    print("\nTesting generator initialization...")
    
    # Create a dummy template if it doesn't exist
    template_path = Path(__file__).parent.parent / 'templates' / 'base_resume.docx'
    config_path = Path(__file__).parent.parent / 'config' / 'resume_config.yaml'
    
    if not template_path.exists():
        print("⚠️  Warning: No template found. Skipping generator initialization test.")
        print(f"   Create template at: {template_path}")
        return
    
    try:
        generator = ResumeGenerator(str(template_path), str(config_path))
        print(f"✅ Generator initialized successfully")
    except Exception as e:
        print(f"❌ Error initializing generator: {e}")
        raise


def run_all_tests():
    """Run all tests"""
    print("=" * 60)
    print("TESTING JOB APPLICATION AUTOMATOR")
    print("=" * 60)
    
    tests = [
        test_list_roles,
        test_config_loading,
        test_generator_init
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except Exception as e:
            print(f"❌ Test failed: {test.__name__}")
            print(f"   Error: {e}")
            failed += 1
    
    print("\n" + "=" * 60)
    print(f"RESULTS: {passed} passed, {failed} failed")
    print("=" * 60)
    
    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
