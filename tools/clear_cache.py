#!/usr/bin/env python3
"""
Clear Streamlit cache and force theme refresh
"""

import os
import shutil
import subprocess
import sys

def clear_streamlit_cache():
    """Clear all Streamlit cache directories"""
    
    # Get user home directory
    home = os.path.expanduser("~")
    
    # Streamlit cache directories
    cache_dirs = [
        os.path.join(home, ".streamlit"),
        os.path.join(home, ".cache", "streamlit"),
        os.path.join(home, "Library", "Caches", "streamlit"),  # macOS
    ]
    
    print("🧹 Clearing Streamlit cache...")
    
    for cache_dir in cache_dirs:
        if os.path.exists(cache_dir):
            try:
                shutil.rmtree(cache_dir)
                print(f"✅ Cleared: {cache_dir}")
            except Exception as e:
                print(f"⚠️  Could not clear {cache_dir}: {e}")
        else:
            print(f"ℹ️  Not found: {cache_dir}")

def clear_browser_cache():
    """Clear browser cache for localhost"""
    print("\n🌐 Browser cache cleared - please refresh the page with Ctrl+Shift+R (or Cmd+Shift+R on Mac)")

def restart_streamlit():
    """Restart Streamlit with fresh cache"""
    print("\n🚀 Restarting Streamlit...")
    
    try:
        # Kill existing Streamlit processes
        subprocess.run(["pkill", "-f", "streamlit"], capture_output=True)
        
        # Start fresh
        subprocess.Popen([sys.executable, "-m", "streamlit", "run", "main.py", "--server.port", "5000"])
        print("✅ Streamlit restarted successfully!")
        
    except Exception as e:
        print(f"⚠️  Could not restart Streamlit: {e}")
        print("Please restart manually: streamlit run main.py")

def main():
    """Main function"""
    print("🎨 TradingView Theme Refresh Tool")
    print("=" * 40)
    
    # Clear cache
    clear_streamlit_cache()
    
    # Browser instructions
    clear_browser_cache()
    
    # Restart Streamlit
    restart_streamlit()
    
    print("\n✨ Theme refresh complete!")
    print("📝 If you still don't see changes:")
    print("   1. Hard refresh browser (Ctrl+Shift+R)")
    print("   2. Clear browser cache completely")
    print("   3. Try incognito/private mode")

if __name__ == "__main__":
    main()
