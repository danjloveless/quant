#!/usr/bin/env python3
"""
Test script for the reorganized QUANTFIN SOCIETY RESEARCH platform
"""

import sys
import os
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

def test_imports():
    """Test all major imports work correctly"""
    print("🧪 Testing reorganized structure...")
    
    try:
        # Test frontend imports
        print("  📱 Testing frontend imports...")
        from src.frontend.main import setup_production
        print("    ✅ main.py imports successful")
        
        # Test backend imports
        print("  🧠 Testing backend imports...")
        from src.backend.analysis import EventStudyAnalyzer
        from src.backend.advanced_gpt_analyst import AdvancedGPTAnalyst
        print("    ✅ analysis modules import successful")
        
        # Test data imports
        print("  📊 Testing data imports...")
        from src.data.market import MarketAnalyzer
        print("    ✅ data modules import successful")
        
        print("✅ All imports successful!")
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def test_structure():
    """Test directory structure is correct"""
    print("🏗️ Testing directory structure...")
    
    required_dirs = [
        "src/frontend",
        "src/backend", 
        "src/data",
        "infrastructure/deployment",
        "infrastructure/config",
        "tools",
        "docs",
        "assets",
        "mobile"
    ]
    
    all_good = True
    for dir_path in required_dirs:
        full_path = project_root / dir_path
        if full_path.exists():
            print(f"  ✅ {dir_path}")
        else:
            print(f"  ❌ {dir_path} - missing")
            all_good = False
    
    return all_good

def test_key_files():
    """Test key files are in correct locations"""
    print("📁 Testing key file locations...")
    
    key_files = [
        ("src/frontend/main.py", "Main application"),
        ("src/backend/analysis.py", "Analysis engine"),
        ("src/data/market.py", "Market data handler"),
        ("infrastructure/deployment/startup.py", "Startup script"),
        ("infrastructure/config/pyproject.toml", "Project config"),
        ("tools/run_platform.py", "Platform launcher"),
        ("README.md", "Main README"),
    ]
    
    all_good = True
    for file_path, description in key_files:
        full_path = project_root / file_path
        if full_path.exists():
            print(f"  ✅ {description}: {file_path}")
        else:
            print(f"  ❌ {description}: {file_path} - missing")
            all_good = False
    
    return all_good

def main():
    """Run all tests"""
    print("🚀 QUANTFIN SOCIETY RESEARCH - Structure Validation")
    print("=" * 50)
    
    tests = [
        ("Directory Structure", test_structure),
        ("Key Files", test_key_files), 
        ("Import System", test_imports),
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"\n{test_name}:")
        result = test_func()
        results.append((test_name, result))
    
    print("\n" + "=" * 50)
    print("📊 Test Results:")
    
    all_passed = True
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"  {status} {test_name}")
        if not result:
            all_passed = False
    
    if all_passed:
        print("\n🎉 All tests passed! Repository reorganization successful.")
        print("\n🚀 You can now run the platform with:")
        print("   python tools/run_platform.py")
    else:
        print("\n⚠️  Some tests failed. Please check the issues above.")
    
    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())