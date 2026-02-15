# Python Project Template

A modern Python project template using **UV** - the blazingly fast Python package manager written in Rust (10-100x faster than pip!).

## 🚀 What is UV?

UV is a modern Python package and project manager that's incredibly fast thanks to being written in Rust. It handles virtual environments, dependency resolution, and package installation much faster than traditional tools like pip and virtualenv.

## 📦 Installing UV

### Windows (PowerShell)
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### macOS
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Linux
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

After installation, restart your terminal or run:
```bash
source $HOME/.cargo/env
```

## 🎯 Using This Template

1. Click the **"Use this template"** button at the top of this GitHub repository
2. Give your new repository a name
3. Clone your new repository to your local machine
4. Follow the setup instructions below

## 🛠️ Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd <your-repo-name>
   ```

2. **Install dependencies:**
   ```bash
   uv sync --all-extras
   ```
   This creates a virtual environment in `.venv/` and installs all dependencies.

3. **Run tests:**
   ```bash
   uv run pytest
   ```

That's it! No need to activate virtual environments manually - just use `uv run`.

## 📁 Project Structure

```
python-project-template/
├── src/                    # Main source code
│   ├── __init__.py
│   └── example.py          # Example module
├── tests/                  # Test files
│   ├── __init__.py
│   └── test_example.py     # Example tests
├── .github/
│   └── workflows/
│       └── tests.yml       # GitHub Actions CI/CD
├── .vscode/
│   └── settings.json       # VS Code configuration
├── .venv/                  # Virtual environment (created by UV)
├── .python-version         # Python version specification
├── pyproject.toml          # Project configuration & dependencies
├── uv.lock                 # Locked dependency versions
├── .gitignore
├── README.md
└── CONTRIBUTING.md
```

## 📚 Adding Dependencies

### Production Dependencies
```bash
uv add package-name
```

Examples:
```bash
uv add requests          # Add requests library
uv add pandas numpy      # Add multiple packages
uv add "flask>=3.0.0"    # Add with version constraint
```

### Development Dependencies
```bash
uv add --dev package-name
```

Examples:
```bash
uv add --dev mypy        # Add type checker
uv add --dev ipython     # Add interactive Python shell
```

## 🔧 Common Commands

### Running Code
```bash
uv run python script.py              # Run a Python script
uv run python -m module_name         # Run a module
uv run python                        # Start Python REPL
```

### Testing
```bash
uv run pytest                        # Run all tests
uv run pytest tests/test_file.py     # Run specific test file
uv run pytest -v                     # Verbose output
uv run pytest --cov=src              # Run with coverage report
```

### Code Quality
```bash
uv run black .                       # Format code with Black
uv run ruff check .                  # Lint code with Ruff
uv run ruff check --fix .            # Auto-fix linting issues
```

### Dependency Management
```bash
uv sync                              # Install dependencies from lockfile
uv sync --all-extras                 # Install all optional dependencies
uv add package-name                  # Add new package
uv remove package-name               # Remove package
uv lock                              # Update lockfile
uv tree                              # Show dependency tree
```

### Python Version Management
```bash
uv python install                    # Install Python version from .python-version
uv python list                       # List available Python versions
uv python install 3.11               # Install specific Python version
```

## 🎓 Why No Virtual Environment Activation?

With UV, you don't need to activate virtual environments manually. Just prefix your commands with `uv run`:

**Traditional way (with venv):**
```bash
source .venv/bin/activate  # Activate first
python script.py
pytest
deactivate
```

**UV way (simpler):**
```bash
uv run python script.py    # UV handles environment automatically
uv run pytest
```

UV automatically uses the `.venv/` environment when you use `uv run`.

## 🧪 Running Tests

This template comes with pytest configured. Run tests with:

```bash
uv run pytest                                    # Run all tests
uv run pytest --cov=src                         # With coverage
uv run pytest --cov=src --cov-report=html       # HTML coverage report
uv run pytest -v                                # Verbose mode
uv run pytest -k "test_name"                    # Run specific test
```

## 🎨 Code Formatting

This template uses Black for code formatting:

```bash
uv run black .              # Format all files
uv run black src/           # Format only src directory
uv run black --check .      # Check without modifying
```

## 🔍 Linting

This template uses Ruff for fast linting:

```bash
uv run ruff check .         # Check for issues
uv run ruff check --fix .   # Auto-fix issues
```

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for development setup and contribution guidelines.

## 📄 License

This template is provided as-is for use in your projects. Modify as needed!

## 🔗 Useful Links

- [UV Documentation](https://docs.astral.sh/uv/)
- [pytest Documentation](https://docs.pytest.org/)
- [Black Documentation](https://black.readthedocs.io/)
- [Ruff Documentation](https://docs.astral.sh/ruff/)
