# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Graze is a Python 3.13 project managed with `uv` (modern Python package manager). The project uses:

- Hatchling for builds
- Ruff for linting and formatting
- mypy for static type checking
- pytest with coverage reporting
- pre-commit hooks for automated checks

## Development Commands

### Environment Setup

```bash
uv sync  # Install dependencies and set up virtual environment
```

### Testing

```bash
uv run pytest                    # Run all tests with coverage
uv run pytest tests/test_foo.py  # Run a specific test file
uv run pytest -k test_name       # Run tests matching pattern
```

### Linting and Formatting

```bash
uv run ruff check .      # Check for linting issues
uv run ruff check --fix  # Auto-fix linting issues
uv run ruff format .     # Format code
```

### Type Checking

```bash
uv run mypy src  # Run type checker on source code
```

### Building

```bash
uv build  # Build distribution packages
```

### Pre-commit Hooks

```bash
uv run pre-commit install       # Install git hooks
uv run pre-commit run --all-files  # Run hooks manually
```

## Development Philosophy

**Simplicity First**: This project values simple solutions to complex problems. Less code is better. Only add complexity when it's truly needed. Prefer:
- Direct, straightforward implementations over clever abstractions
- Fewer lines of code over elaborate patterns
- Built-in Python features over external dependencies
- Simple conditionals over complex class hierarchies

When solving a problem, start with the simplest approach that works. Add complexity only when requirements demand it, not in anticipation of future needs.

## Code Architecture

### Project Structure

- `src/graze/` - Main package source code
  - `__init__.py` - Package initialization and version
  - `__main__.py` - CLI entry point (invokable via `graze` command)
- `tests/` - Test suite
- `pyproject.toml` - Project configuration and dependencies

### Type Annotations

All functions must have type annotations. The mypy configuration enforces `disallow_untyped_defs = true`.

### Code Quality Standards

- Line length: 88 characters
- Python target: 3.13
- Ruff enforces: pycodestyle (E/W), pyflakes (F), isort (I), pyupgrade (UP), flake8-bugbear (B)
- Double quotes for strings

### Test Coverage

Tests use pytest with coverage reporting. Coverage is configured to track `src/` directory and exclude test files.
