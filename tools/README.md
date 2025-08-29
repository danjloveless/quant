# Tools - Utility Scripts and Management

This directory contains utility scripts for managing, maintaining, and operating the QUANTFIN SOCIETY RESEARCH platform.

## Available Tools

### 🚀 Platform Management
- **run_platform.py** - Platform launcher and development server
- **quick_start.py** - Quick setup and initialization script
- **test_platform.py** - Platform testing and validation utilities

### 🔧 Maintenance and Operations
- **monitor.py** - Platform monitoring and health checks
- **backup.py** - Data backup and restore utilities
- **update.py** - Update and optimization scripts
- **clear_cache.py** - Cache management and cleanup

### 📦 Dependencies and Installation
- **install_requirements.py** - Dependency installation and management

### 📚 Documentation
- **docs.py** - Documentation generation and management

## Usage

### Platform Operations

#### Start the Platform
```bash
# Quick start with default settings
python tools/run_platform.py

# Or use the setup script for first-time users
python tools/quick_start.py setup
```

#### Health Monitoring
```bash
# Check platform health
python tools/monitor.py

# Monitor continuously
python tools/monitor.py --continuous
```

#### Testing
```bash
# Run platform tests
python tools/test_platform.py

# Test specific components
python tools/test_platform.py --component analysis
python tools/test_platform.py --component data
```

### Maintenance Tasks

#### Backups
```bash
# Create a backup
python tools/backup.py create

# List available backups
python tools/backup.py list

# Restore from backup
python tools/backup.py restore <backup_file>
```

#### Updates and Optimization
```bash
# Update dependencies
python tools/update.py dependencies

# Optimize performance
python tools/update.py optimize

# Clean cache
python tools/update.py cache

# Full system update
python tools/update.py all
```

#### Cache Management
```bash
# Clear all caches
python tools/clear_cache.py

# Clear specific cache types
python tools/clear_cache.py --type streamlit
python tools/clear_cache.py --type data
```

### Documentation Management

#### Generate Documentation
```bash
# Generate all documentation
python tools/docs.py all

# Generate specific documentation
python tools/docs.py quick      # Quick start guide
python tools/docs.py api        # API documentation
python tools/docs.py user       # User guide
python tools/docs.py deploy     # Deployment guide
```

### Development Utilities

#### Installation Management
```bash
# Install all requirements
python tools/install_requirements.py

# Install with specific options
python tools/install_requirements.py --dev      # Include development dependencies
python tools/install_requirements.py --upgrade  # Upgrade existing packages
```

## Tool Descriptions

### run_platform.py
**Purpose**: Main platform launcher  
**Features**: 
- Automatic environment detection
- Multiple startup modes (development, production)
- Port and configuration management
- Error handling and logging

### quick_start.py
**Purpose**: First-time setup and quick start  
**Features**:
- Environment setup
- Dependency installation
- Configuration validation
- Initial platform test

### monitor.py
**Purpose**: Platform health monitoring  
**Features**:
- Health endpoint checks
- Performance metrics
- Resource usage monitoring
- Alert notifications

### backup.py
**Purpose**: Data backup and recovery  
**Features**:
- Automated backups
- Incremental backup support
- Backup verification
- Restore functionality

### update.py
**Purpose**: System updates and optimization  
**Features**:
- Dependency updates
- Performance optimization
- Cache management
- Security updates

### test_platform.py
**Purpose**: Platform testing and validation  
**Features**:
- Component testing
- Integration tests
- Performance benchmarks
- Regression testing

## Best Practices

1. **Regular Monitoring**: Run `monitor.py` regularly to ensure platform health
2. **Backup Strategy**: Create backups before major updates using `backup.py`
3. **Performance Optimization**: Use `update.py optimize` periodically
4. **Cache Management**: Clear caches when experiencing issues
5. **Documentation**: Keep documentation updated with `docs.py`

## Error Handling

All tools include comprehensive error handling and logging. Check logs for detailed error information:
- Development: Console output
- Production: Log files in appropriate directories

## Integration

These tools are designed to work with:
- The main platform (`src/`)
- Infrastructure components (`infrastructure/`)
- Mobile applications (`mobile/`)
- Documentation system (`docs/`)

Use these tools as part of your development and operational workflow for optimal platform management.