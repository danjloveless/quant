# Infrastructure - Deployment and Configuration

This directory contains all infrastructure-related files for deployment, configuration, and platform management.

## Directory Structure

### 🚀 deployment/
Contains scripts and configuration files for deploying to various cloud platforms:

- **startup.py** - Production environment startup script
- **deploy_main.py** - Main deployment entry point
- **startup_render.sh** - Render cloud platform startup script
- **deploy.sh** - Shell script for deployment automation
- **deploy_all.py** - Multi-platform deployment utility
- **Procfile** - Heroku process configuration

#### Supported Platforms
- **Render** - Primary deployment target
- **Railway** - Alternative cloud platform
- **Heroku** - Traditional PaaS deployment
- **Vercel** - Serverless deployment
- **Fly.io** - Modern cloud platform

### ⚙️ config/
Contains configuration files and dependency management:

- **pyproject.toml** - Python project metadata and dependencies
- **requirements.txt** - Python package requirements (for platforms that need it)
- **manifest.json** - Progressive Web App manifest
- **.streamlit/** - Streamlit server configuration
- **uv.lock** - UV package manager lock file for reproducible builds

## Usage

### Deployment

#### Quick Deploy to Render (Recommended)
```bash
python infrastructure/deployment/deploy_all.py render
```

#### Deploy to Multiple Platforms
```bash
# Deploy to all supported platforms
python infrastructure/deployment/deploy_all.py all

# Deploy to specific platform
python infrastructure/deployment/deploy_all.py railway
python infrastructure/deployment/deploy_all.py vercel
python infrastructure/deployment/deploy_all.py fly
```

#### Manual Deployment
```bash
# Use platform-specific startup script
./infrastructure/deployment/startup_render.sh

# Or use the main deployment script
python infrastructure/deployment/deploy_main.py
```

### Configuration Management

#### Environment Variables
Required environment variables (set in your platform's dashboard):
```env
OPENAI_API_KEY=your_openai_api_key_here
ALPHA_VANTAGE_API_KEY=your_alpha_vantage_key_here
PORT=5000  # Optional, auto-detected by most platforms
```

#### Streamlit Configuration
The platform uses optimized Streamlit settings in `config/.streamlit/config.toml`:
- Port: 5000 (default) or `$PORT` environment variable
- Address: 0.0.0.0 (all interfaces)
- Headless mode enabled
- CORS disabled for cloud deployment
- Usage stats disabled for privacy

### Dependency Management

#### Using UV (Recommended)
```bash
# Install dependencies
uv sync --frozen

# Add new dependency
uv add package_name

# Update lock file
uv lock
```

#### Using Pip (Fallback)
```bash
# Install from requirements
pip install -r infrastructure/config/requirements.txt
```

## Platform-Specific Notes

### Render
- Uses `startup_render.sh` for initialization
- Automatic environment variable detection
- Built-in SSL and domain management

### Railway
- Uses `railway.json` for configuration
- Automatic port detection from `$PORT`
- Git-based deployment

### Heroku
- Uses `Procfile` for process management
- Requires `requirements.txt`
- Buildpack: Python

### Vercel
- Serverless deployment model
- Uses `vercel.json` for configuration
- Function-based execution

### Fly.io
- Uses `fly.toml` for configuration
- Docker-based deployment
- Global edge deployment

## Monitoring and Maintenance

Use the tools in the `tools/` directory for ongoing maintenance:
- `python tools/monitor.py` - Health checks
- `python tools/update.py optimize` - Performance optimization
- `python tools/backup.py create` - Create backups

## Security

- Never commit API keys or sensitive data
- Use environment variables for all secrets
- Keep dependencies updated regularly
- Monitor for security vulnerabilities