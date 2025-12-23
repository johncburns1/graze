# Architecture

## System Overview

Graze is a CLI tool that learns dining preferences and provides personalized restaurant/bar recommendations.

```text
┌─────────────────────────────────────────────────────────────┐
│                       CLI Interface                          │
└────────────┬────────────────────────────────┬───────────────┘
             │                                │
             ▼                                ▼
    ┌────────────────┐              ┌─────────────────┐
    │ Profile Manager│              │ Recommendation  │
    │                │              │    Engine       │
    └────────┬───────┘              └────────┬────────┘
             │                               │
             ▼                               ▼
    ┌────────────────┐              ┌─────────────────┐
    │ Storage Layer  │              │  Data Sources   │
    │  (JSON Files)  │              │  (Yelp API)     │
    └────────────────┘              └─────────────────┘
```

## Core Components

1. **CLI Interface** - User commands (add, recommend, profile, etc.)
2. **Profile Manager** - Build and maintain user preference profiles
3. **Data Sources** - Fetch establishment data (Yelp API for MVP)
4. **Recommendation Engine** - Generate personalized recommendations
5. **Storage** - Persist profiles and cache data (JSON files)

## Recommendation Approach

Two-phase pipeline:

1. **ML Similarity** - Fast filtering based on attributes → top 20-30 candidates
2. **LLM Refinement** - Analyze atmosphere, generate customer profiles → final 10 recommendations

## Key Data Models

```python
@dataclass
class Establishment:
    id: str
    name: str
    location: Location
    price_level: int  # 1-4
    cuisine_types: list[str]
    rating: float

@dataclass
class UserProfile:
    name: str
    liked_establishments: list[str]
    preferences: ProfilePreferences  # Computed from liked places

@dataclass
class Recommendation:
    establishment: Establishment
    score: float
    customer_profile: str  # e.g., "finance bros", "bedstuy locals"
    explanation: str
```

## Design Principles

- **Simplicity First** - Start simple, add complexity only when needed
- **Pluggable** - Use protocols so components can be swapped
- **Type Safe** - Full type annotations with mypy
- **Testable** - Small functions, dependency injection

## Technology Stack (MVP)

- Python 3.13 + uv
- Yelp Fusion API
- JSON file storage
- pytest for testing
- TBD: CLI framework, ML library, LLM provider

---

**Last Updated**: 2025-12-22
