#!/usr/bin/env python3
"""
Fast multi-platform deployer for QUANTFIN SOCIETY RESEARCH platform.
Quick deployment to all supported cloud platforms.
"""

import os
import sys
import subprocess
from pathlib import Path

def create_deployment_files():
    """Create all necessary deployment files"""
    
    print("📁 Creating deployment files...")
    
    # Create render.yaml
    render_yaml = """services:
  - type: web
    name: quantfin-society-research
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: ./startup_render.sh
    envVars:
      - key: OPENAI_API_KEY
        sync: false
      - key: ALPHA_VANTAGE_API_KEY
        sync: false
"""
    
    with open('render.yaml', 'w') as f:
        f.write(render_yaml)
    
    # Create railway.json
    railway_json = """{
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "startCommand": "streamlit run main.py --server.port $PORT --server.address 0.0.0.0 --server.headless true --server.enableCORS false --server.enableXsrfProtection false",
    "healthcheckPath": "/",
    "healthcheckTimeout": 300,
    "restartPolicyType": "ON_FAILURE"
  }
}
"""
    
    with open('railway.json', 'w') as f:
        f.write(railway_json)
    
    # Create vercel.json
    vercel_json = """{
  "builds": [
    {
      "src": "main.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "main.py"
    }
  ],
  "env": {
    "STREAMLIT_SERVER_PORT": "5000",
    "STREAMLIT_SERVER_ADDRESS": "0.0.0.0",
    "STREAMLIT_SERVER_HEADLESS": "true",
    "STREAMLIT_SERVER_ENABLE_CORS": "false",
    "STREAMLIT_SERVER_ENABLE_XSRF_PROTECTION": "false"
  }
}
"""
    
    with open('vercel.json', 'w') as f:
        f.write(vercel_json)
    
    # Create fly.toml
    fly_toml = """app = "quantfin-society-research"
primary_region = "iad"

[env]
  STREAMLIT_SERVER_PORT = "8080"
  STREAMLIT_SERVER_ADDRESS = "0.0.0.0"
  STREAMLIT_SERVER_HEADLESS = "true"
  STREAMLIT_SERVER_ENABLE_CORS = "false"
  STREAMLIT_SERVER_ENABLE_XSRF_PROTECTION = "false"

[[services]]
  internal_port = 8080
  protocol = "tcp"

  [[services.ports]]
    port = 80
    handlers = ["http"]
  [[services.ports]]
    port = 443
    handlers = ["tls", "http"]

  [services.concurrency]
    type = "connections"
    hard_limit = 25
    soft_limit = 20

  [[services.tcp_checks]]
    interval = "15s"
    timeout = "2s"
    grace_period = "1s"
    restart_limit = 0
"""
    
    with open('fly.toml', 'w') as f:
        f.write(fly_toml)
    
    print("✅ Deployment files created!")

def deploy_to_render():
    """Deploy to Render"""
    
    print("🚀 Deploying to Render...")
    
    # Check if render CLI is installed
    try:
        subprocess.run(['render', '--version'], check=True, capture_output=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Render CLI not found. Install with: npm install -g @render/cli")
        return False
    
    try:
        subprocess.run(['render', 'deploy'], check=True)
        print("✅ Deployed to Render successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Render deployment failed: {e}")
        return False

def deploy_to_railway():
    """Deploy to Railway"""
    
    print("🚀 Deploying to Railway...")
    
    # Check if railway CLI is installed
    try:
        subprocess.run(['railway', '--version'], check=True, capture_output=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Railway CLI not found. Install with: npm install -g @railway/cli")
        return False
    
    try:
        subprocess.run(['railway', 'deploy'], check=True)
        print("✅ Deployed to Railway successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Railway deployment failed: {e}")
        return False

def deploy_to_vercel():
    """Deploy to Vercel"""
    
    print("🚀 Deploying to Vercel...")
    
    # Check if vercel CLI is installed
    try:
        subprocess.run(['vercel', '--version'], check=True, capture_output=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Vercel CLI not found. Install with: npm install -g vercel")
        return False
    
    try:
        subprocess.run(['vercel', '--prod'], check=True)
        print("✅ Deployed to Vercel successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Vercel deployment failed: {e}")
        return False

def deploy_to_fly():
    """Deploy to Fly.io"""
    
    print("🚀 Deploying to Fly.io...")
    
    # Check if fly CLI is installed
    try:
        subprocess.run(['fly', 'version'], check=True, capture_output=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Fly CLI not found. Install with: curl -L https://fly.io/install.sh | sh")
        return False
    
    try:
        subprocess.run(['fly', 'deploy'], check=True)
        print("✅ Deployed to Fly.io successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Fly.io deployment failed: {e}")
        return False

def main():
    """Main deployment utility"""
    
    if len(sys.argv) < 2:
        print("🚀 QUANTFIN SOCIETY RESEARCH - Multi-Platform Deployer")
        print("Usage:")
        print("  python deploy_all.py files     - Create deployment files")
        print("  python deploy_all.py render    - Deploy to Render")
        print("  python deploy_all.py railway   - Deploy to Railway")
        print("  python deploy_all.py vercel    - Deploy to Vercel")
        print("  python deploy_all.py fly       - Deploy to Fly.io")
        print("  python deploy_all.py all       - Deploy to all platforms")
        return
    
    command = sys.argv[1]
    
    if command == "files":
        create_deployment_files()
    elif command == "render":
        deploy_to_render()
    elif command == "railway":
        deploy_to_railway()
    elif command == "vercel":
        deploy_to_vercel()
    elif command == "fly":
        deploy_to_fly()
    elif command == "all":
        print("🚀 Deploying to all platforms...")
        create_deployment_files()
        deploy_to_render()
        deploy_to_railway()
        deploy_to_vercel()
        deploy_to_fly()
        print("✅ All deployments completed!")
    else:
        print(f"❌ Unknown command: {command}")

if __name__ == "__main__":
    main()
