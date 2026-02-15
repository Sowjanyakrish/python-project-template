# Contributing to This Project

Thank you for your interest in contributing! This document provides guidelines and instructions for setting up your development environment and contributing to the project.

## 🚀 Quick Start

### Prerequisites

1. Install UV (the fast Python package manager):
   
   **macOS/Linux:**
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```
   
   **Windows (PowerShell):**
   ```powershell
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```

2. Ensure you have Git installed

### Setting Up the Development Environment

1. **Fork and clone the repository:**
   ```bash
   git clone https://github.com/YOUR-USERNAME/REPO-NAME.git
   cd REPO-NAME
   ```

2. **Install dependencies:**
   ```bash
   uv sync --all-extras
   ```
   
   This command:
   - Creates a virtual environment in `.venv/`
   - Installs all production dependencies
   - Installs all development dependencies (pytest, black, ruff, etc.)
   - Creates/updates the `uv.lock` file

3. **Verify the installation:**
   ```bash
   uv run pytest
   ```
   
   All tests should pass! ✅

## 🧪 Running Tests

### Run all tests:
```bash
uv run pytest
```

### Run tests with coverage:
```bash
uv run pytest --cov=src --cov-report=term-missing
```

### Run tests in verbose mode:
```bash
uv run pytest -v
```

### Run specific test file:
```bash
uv run pytest tests/test_example.py
```

### Run tests matching a pattern:
```bash
uv run pytest -k "test_add"
```

### Run tests with detailed output:
```bash
uv run pytest -vv
```

## 📦 Managing Dependencies

### Adding Production Dependencies

When your code needs a new package:

```bash
uv add package-name
```

Examples:
```bash
uv add requests                    # Add latest version
uv add "pandas>=2.0.0"            # Add with version constraint
uv add numpy scipy matplotlib      # Add multiple packages
```

This updates both `pyproject.toml` and `uv.lock`.

### Adding Development Dependencies

For tools used only in development (testing, linting, etc.):

```bash
uv add --dev package-name
```

Examples:
```bash
uv add --dev mypy                  # Add type checker
uv add --dev ipython               # Add better REPL
uv add --dev pytest-asyncio        # Add async testing support
```

### Removing Dependencies

```bash
uv remove package-name
```

### Updating Dependencies

```bash
uv lock --upgrade                  # Update all dependencies
uv lock --upgrade-package requests # Update specific package
```

## 🎨 Code Style

This project follows standard Python style guidelines:

### Formatting with Black

Black is configured to format code automatically:

```bash
# Format all files
uv run black .

# Format specific directory
uv run black src/

# Check formatting without making changes
uv run black --check .
```

**Configuration:** Line length is set to 88 characters (Black's default).

### Linting with Ruff

Ruff is a fast Python linter that checks for errors and style issues:

```bash
# Check all files
uv run ruff check .

# Auto-fix issues where possible
uv run ruff check --fix .

# Check specific directory
uv run ruff check src/
```

### Type Hints

- Use type hints for function arguments and return values
- Example:
  ```python
  def add(a: float, b: float) -> float:
      return a + b
  ```

### Docstrings

- Use Google-style or NumPy-style docstrings
- Document all public functions, classes, and modules
- Example:
  ```python
  def greet(name: str) -> str:
      """
      Generate a greeting message.
      
      Args:
          name: The name to greet.
      
      Returns:
          A greeting string.
      """
      return f"Hello, {name}!"
  ```

## 🔄 Development Workflow

1. **Create a new branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes:**
   - Write code
   - Add tests for new functionality
   - Update documentation if needed

3. **Format and lint your code:**
   ```bash
   uv run black .
   uv run ruff check --fix .
   ```

4. **Run tests:**
   ```bash
   uv run pytest --cov=src
   ```
   
   Ensure:
   - All tests pass ✅
   - Code coverage doesn't decrease
   - New features have tests

5. **Commit your changes:**
   ```bash
   git add .
   git commit -m "Add feature: description of your changes"
   ```
   
   **Commit message guidelines:**
   - Use present tense ("Add feature" not "Added feature")
   - Be descriptive but concise
   - Reference issue numbers if applicable (#123)

6. **Push to your fork:**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create a Pull Request:**
   - Go to the original repository on GitHub
   - Click "New Pull Request"
   - Select your branch
   - Fill in the PR template with:
     - Description of changes
     - Related issues
     - Testing done
     - Screenshots (if applicable)

## ✅ Pre-commit Checklist

Before submitting a pull request, ensure:

- [ ] Code is formatted with Black: `uv run black .`
- [ ] Code passes Ruff linting: `uv run ruff check .`
- [ ] All tests pass: `uv run pytest`
- [ ] New features have tests
- [ ] Documentation is updated
- [ ] Commit messages are clear and descriptive
- [ ] No unnecessary files are committed

## 🐛 Reporting Bugs

When reporting bugs, please include:

1. **Description:** Clear description of the bug
2. **Steps to reproduce:** Minimal steps to reproduce the issue
3. **Expected behavior:** What should happen
4. **Actual behavior:** What actually happens
5. **Environment:**
   - Python version: `python --version`
   - UV version: `uv --version`
   - OS: macOS/Linux/Windows
6. **Error messages:** Full error traceback if applicable

## 💡 Suggesting Features

We welcome feature suggestions! Please:

1. Check if the feature has already been requested
2. Describe the feature and its use case
3. Explain why it would be valuable
4. Provide examples of how it would work

## 📝 Writing Tests

### Test File Structure

- Place tests in the `tests/` directory
- Name test files `test_*.py`
- Name test functions `test_*`

### Test Example

```python
import pytest
from src.example import add

def test_add():
    """Test the add function."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_add_with_invalid_input():
    """Test that add raises TypeError with strings."""
    with pytest.raises(TypeError):
        add("hello", "world")
```

### Test Coverage

- Aim for >80% code coverage
- Test both success and failure cases
- Test edge cases and boundary conditions

## 🔧 Troubleshooting

### UV Commands Not Working

Ensure UV is in your PATH:
```bash
# Check UV installation
uv --version

# If not found, restart your terminal or run:
source $HOME/.cargo/env
```

### Virtual Environment Issues

Delete and recreate the environment:
```bash
rm -rf .venv
uv sync --all-extras
```

### Test Failures

Run tests in verbose mode to see details:
```bash
uv run pytest -vv
```

### Import Errors

Ensure dependencies are installed:
```bash
uv sync --all-extras
```

## 📚 Additional Resources

- [UV Documentation](https://docs.astral.sh/uv/)
- [pytest Documentation](https://docs.pytest.org/)
- [Black Documentation](https://black.readthedocs.io/)
- [Ruff Documentation](https://docs.astral.sh/ruff/)
- [Python Type Hints (PEP 484)](https://peps.python.org/pep-0484/)

## 🙏 Thank You!

Your contributions make this project better. We appreciate your time and effort!

---

**Questions?** Feel free to open an issue for discussion.
