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

## Test-Driven Development

This project follows a **test-driven development (TDD)** approach for core product functionality:

### TDD Workflow

1. **Write tests first** - Write unit tests that capture the desired functionality before implementation
2. **Implement to pass** - Write code to make the tests pass
3. **Verify completeness** - Run tests to verify the code works as expected

### When to Use TDD

- **Core product functionality** - All business logic, recommendation engines, data processing, etc.
- **Complex algorithms** - Multi-step processes where edge cases matter
- **API integrations** - External service interactions (with mocked responses for unit tests)

### When Tests Can Follow Code

- **Data models and types** - Simple classes, dataclasses, type definitions (but add tests afterward)
- **Configuration files** - Settings, constants, simple configs
- **Obvious utilities** - Straightforward helper functions

### Test Writing Approach

- **Write in batches** - Create multiple related tests for a component at once to think through edge cases and core functionality before implementing
- **Think through scenarios** - Consider happy path, edge cases, error conditions, and boundary values upfront
- **Small, testable units** - Design code to be testable: prefer interfaces, small modular functions, and functional programming style

### Test Organization

Use industry-standard pytest organization:

- `tests/` directory mirrors `src/graze/` structure
- `tests/test_foo.py` tests `src/graze/foo.py`
- Group related tests in classes when helpful
- Use descriptive test names: `test_<function>_<scenario>_<expected>`

### Test Types

**Unit Tests** (primary focus):

- Test single, modular functions in isolation
- Mock external dependencies (APIs, file I/O, etc.)
- Fast execution, no network calls
- Use pytest fixtures for test data and mocks

**Integration Tests** (broader scope):

- Test multiple components working together
- Can hit real APIs (Yelp, LLM providers)
- Slower, more comprehensive
- Test end-to-end workflows

### Coverage Target

- **90% code coverage** as the goal
- Focus on critical paths and business logic
- Not every line needs testing, but make a good effort
- Use `uv run pytest` to see coverage reports

## Code Architecture

### Hexagonal Architecture with Domain-Driven Design

This project uses **hexagonal architecture** (Ports and Adapters) combined with **Domain-Driven Design** patterns:

- **Domain models** represent business entities and logic, kept pure and framework-agnostic
- **Ports** define interfaces between domain and external systems
- **Adapters** implement ports for specific technologies (databases, APIs, etc.)
- **Repositories** handle persistence, translating between domain models and database models
- **Dependencies point inward**: domain code depends only on interfaces, never on implementations

Domain models are never persisted directly. Repository adapters contain separate persistence models and handle translation.

### Project Structure

- `src/graze/` - Main package source code
  - `domain/` - Domain models and business logic
  - `ports/` - Interface definitions
  - `adapters/` - Concrete implementations
  - `application/` - Use cases and application services
  - `__init__.py` - Package initialization and version
  - `__main__.py` - CLI entry point (invokable via `graze` command)
- `tests/` - Test suite (mirrors src structure)
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
