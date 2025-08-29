#!/usr/bin/env python3
"""
Fast platform tester for QUANTFIN SOCIETY RESEARCH.
Quick validation of all components and dependencies.
"""

import sys
import os
import importlib

def test_dependencies():
    """Test all required dependencies"""
    
    print("🧪 Testing QUANTFIN SOCIETY RESEARCH dependencies...")
    
    dependencies = [
        'streamlit',
        'pandas', 
        'numpy',
        'plotly',
        'yfinance',
        'scipy',
        'openai',
        'requests',
        'trafilatura'
    ]
    
    failed = []
    
    for dep in dependencies:
        try:
            importlib.import_module(dep)
            print(f"✅ {dep}")
        except ImportError:
            print(f"❌ {dep}")
            failed.append(dep)
    
    return failed

def test_files():
    """Test if all required files exist"""
    
    print("\n📁 Testing required files...")
    
    required_files = [
        'main.py',
        'startup.py',
        'deploy_main.py',
        'requirements.txt',
        'README.md'
    ]
    
    missing = []
    
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file}")
        else:
            print(f"❌ {file}")
            missing.append(file)
    
    return missing

def test_environment():
    """Test environment configuration"""
    
    print("\n🔧 Testing environment...")
    
    # Test Python version
    if sys.version_info >= (3, 11):
        print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor}")
    else:
        print(f"❌ Python {sys.version_info.major}.{sys.version_info.minor} (need 3.11+)")
        return False
    
    # Test API keys
    if os.environ.get('OPENAI_API_KEY'):
        print("✅ OPENAI_API_KEY set")
    else:
        print("⚠️  OPENAI_API_KEY not set")
    
    if os.environ.get('ALPHA_VANTAGE_API_KEY'):
        print("✅ ALPHA_VANTAGE_API_KEY set")
    else:
        print("⚠️  ALPHA_VANTAGE_API_KEY not set")
    
    return True

def main():
    """Run all tests"""
    
    print("🚀 QUANTFIN SOCIETY RESEARCH - Platform Test")
    print("=" * 50)
    
    # Test dependencies
    failed_deps = test_dependencies()
    
    # Test files
    missing_files = test_files()
    
    # Test environment
    env_ok = test_environment()
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 Test Results:")
    
    if not failed_deps and not missing_files and env_ok:
        print("✅ All tests passed! Platform ready to use.")
        print("🚀 Run: python startup.py")
    else:
        print("❌ Some tests failed:")
        
        if failed_deps:
            print(f"  - Missing dependencies: {', '.join(failed_deps)}")
            print("  - Run: pip install -r requirements.txt")
        
        if missing_files:
            print(f"  - Missing files: {', '.join(missing_files)}")
        
        if not env_ok:
            print("  - Environment issues detected")

if __name__ == "__main__":
    main()
