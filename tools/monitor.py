#!/usr/bin/env python3
"""
Fast platform monitor for QUANTFIN SOCIETY RESEARCH.
Quick health check and performance monitoring.
"""

import os
import sys
import time
import psutil
import requests
from datetime import datetime

def check_system_resources():
    """Check system resource usage"""
    
    print("💻 System Resources:")
    
    # CPU usage
    cpu_percent = psutil.cpu_percent(interval=1)
    print(f"  CPU: {cpu_percent:.1f}%")
    
    # Memory usage
    memory = psutil.virtual_memory()
    print(f"  Memory: {memory.percent:.1f}% ({memory.used // 1024**3}GB / {memory.total // 1024**3}GB)")
    
    # Disk usage
    disk = psutil.disk_usage('/')
    print(f"  Disk: {disk.percent:.1f}% ({disk.used // 1024**3}GB / {disk.total // 1024**3}GB)")
    
    return cpu_percent < 80 and memory.percent < 80 and disk.percent < 90

def check_platform_status():
    """Check if platform is running"""
    
    print("\n🌐 Platform Status:")
    
    try:
        # Check if port 5000 is in use
        response = requests.get('http://localhost:5000', timeout=5)
        if response.status_code == 200:
            print("  ✅ Platform is running on port 5000")
            return True
        else:
            print(f"  ⚠️  Platform responded with status {response.status_code}")
            return False
    except requests.exceptions.RequestException:
        print("  ❌ Platform is not running on port 5000")
        return False

def check_api_keys():
    """Check API key configuration"""
    
    print("\n🔑 API Keys:")
    
    openai_key = os.environ.get('OPENAI_API_KEY')
    alpha_key = os.environ.get('ALPHA_VANTAGE_API_KEY')
    
    if openai_key and len(openai_key) > 10:
        print("  ✅ OpenAI API key configured")
    else:
        print("  ❌ OpenAI API key not configured")
    
    if alpha_key and len(alpha_key) > 10:
        print("  ✅ Alpha Vantage API key configured")
    else:
        print("  ❌ Alpha Vantage API key not configured")
    
    return bool(openai_key and alpha_key)

def check_dependencies():
    """Quick dependency check"""
    
    print("\n📦 Dependencies:")
    
    required = ['streamlit', 'pandas', 'numpy', 'plotly', 'yfinance', 'openai']
    
    for dep in required:
        try:
            __import__(dep)
            print(f"  ✅ {dep}")
        except ImportError:
            print(f"  ❌ {dep}")
            return False
    
    return True

def main():
    """Run platform monitoring"""
    
    print("🔍 QUANTFIN SOCIETY RESEARCH - Platform Monitor")
    print(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    
    # Run all checks
    system_ok = check_system_resources()
    platform_ok = check_platform_status()
    api_ok = check_api_keys()
    deps_ok = check_dependencies()
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 Monitor Summary:")
    
    if all([system_ok, platform_ok, api_ok, deps_ok]):
        print("✅ Platform is healthy and ready!")
    else:
        print("⚠️  Some issues detected:")
        
        if not system_ok:
            print("  - System resources need attention")
        
        if not platform_ok:
            print("  - Platform is not running")
        
        if not api_ok:
            print("  - API keys need configuration")
        
        if not deps_ok:
            print("  - Dependencies need installation")

if __name__ == "__main__":
    main()
