# QUANTFIN SOCIETY RESEARCH - Deployment Guide

## Cloud Platform Deployment Configuration

This application is optimized for deployment on various cloud platforms with proper configuration.

## 🚀 Supported Platforms

### Render
- **Build Command**: `uv sync --frozen && uv cache prune --ci`
- **Start Command**: `./startup_render.sh`
- **Environment Variables**: Set `OPENAI_API_KEY` and `ALPHA_VANTAGE_API_KEY`

### Railway
- **Build Command**: `uv sync --frozen`
- **Start Command**: `streamlit run main.py --server.port $PORT`
- **Configuration**: Use `railway.json` for automatic setup

### Heroku
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `streamlit run main.py --server.port $PORT`
- **Configuration**: Use `Procfile` for process management

### Vercel
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `streamlit run main.py --server.port $PORT`
- **Configuration**: Use `vercel.json` for deployment settings

### Fly.io
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `streamlit run main.py --server.port $PORT`
- **Configuration**: Use `fly.toml` for deployment settings

## 🔧 Environment Configuration

### Required Environment Variables

```bash
OPENAI_API_KEY=your_openai_api_key_here
ALPHA_VANTAGE_API_KEY=your_alpha_vantage_key_here
PORT=5000  # Optional, auto-detected by most platforms
```

### Streamlit Server Configuration

The application uses the following Streamlit server settings:
- **Port**: 5000 (default) or `$PORT` environment variable
- **Address**: 0.0.0.0 (all interfaces)
- **Headless**: true (no browser launch)
- **CORS**: disabled
- **XSRF Protection**: disabled
- **Usage Stats**: disabled

## 📋 Deployment Steps

### 1. Platform Selection
Choose your preferred cloud platform from the supported options above.

### 2. Repository Connection
Connect your GitHub repository to the chosen platform:
- **Repository**: `https://github.com/QuantFin-Exeter/quant`
- **Branch**: `main`

### 3. Environment Variables
Set the required environment variables in your platform's dashboard:
- `OPENAI_API_KEY`
- `ALPHA_VANTAGE_API_KEY`

### 4. Build and Deploy
Use the platform-specific build and start commands listed above.

### 5. Domain Configuration
Configure your custom domain (e.g., `https://quantfin.it.com/`) in your platform's settings.

## 🛠️ Troubleshooting

### Common Issues

1. **Port Configuration**: Ensure the port matches your platform's requirements
2. **Environment Variables**: Verify all required variables are set
3. **Dependencies**: Check that all Python packages are properly installed
4. **API Keys**: Ensure API keys are valid and have sufficient quotas

### Platform-Specific Issues

- **Render**: Check build logs for dependency installation issues
- **Railway**: Verify `railway.json` configuration
- **Heroku**: Check `Procfile` format and dyno configuration
- **Vercel**: Review `vercel.json` settings
- **Fly.io**: Validate `fly.toml` configuration

## ✅ Success Indicators

After successful deployment:
- Application starts without errors
- All API endpoints respond correctly
- Custom domain resolves properly
- SSL certificate is active
- Application is accessible via web browser

The application is now fully configured for successful deployment on all supported cloud platforms.