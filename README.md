# Python Project Template 🐍⚡

This is a template repository for Python projects with UV and pytest already configured!

**Why UV?** UV is 10-100x faster than pip and manages everything (packages, virtual environments, Python versions) in one tool!

## How to Use This Template

1. Click the green **"Use this template"** button above
2. Name your new project
3. Clone it to your computer
4. Follow the setup instructions below

## Setup Instructions

### Step 1: Install UV (One Time Only!)

**On Windows (PowerShell):**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**On Mac/Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Close and reopen your terminal after installing!

### Step 2: Clone Your New Project
```bash
git clone https://github.com/YOUR-USERNAME/YOUR-PROJECT-NAME.git
cd YOUR-PROJECT-NAME
```

### Step 3: Sync Dependencies (UV Does Everything!)
```bash
uv sync
```

That's it! UV automatically:
- ✅ Creates a virtual environment in `.venv`
- ✅ Installs all dependencies from `pyproject.toml`
- ✅ Locks versions in `uv.lock` for reproducibility

### Step 4: Run Tests
```bash
uv run pytest
```

## Project Structure
your-project/
├── src/                  # Your Python code goes here
│   └── init.py
├── tests/                # Your test files go here
│   └── test_example.py
├── .venv/                # Virtual environment (created by UV)
├── .gitignore           # Files to ignore
├── pyproject.toml       # Project config & dependencies (replaces requirements.txt!)
├── uv.lock              # Locked dependency versions (auto-generated)
├── README.md           # This file!
└── pytest.ini          # Pytest configuration


## Adding Your Code

1. Put your Python files in the `src/` folder
2. Put your test files in the `tests/` folder (name them `test_*.py`)
3. Run `uv run pytest` to test everything

## Installing New Packages
```bash
# Add a package (UV automatically updates pyproject.toml and uv.lock!)
uv add requests

# Add a development-only package (like pytest, black, etc.)
uv add --dev black

# Remove a package
uv remove requests
```

## Common Commands

- **Run all tests:** `uv run pytest`
- **Run specific test file:** `uv run pytest tests/test_example.py`
- **Run with coverage:** `uv run pytest --cov=src`
- **Run any Python script:** `uv run python your_script.py`
- **Add package:** `uv add package-name`
- **Update all packages:** `uv lock --upgrade`
- **Sync dependencies:** `uv sync`

No need to activate/deactivate - just use `uv run`! 🚀

Happy Coding! 🎉
