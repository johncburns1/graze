# Product Definition

## Product Vision

Graze is a personalized restaurant and bar recommendation tool that learns your dining preferences and helps you discover new places you'll love in any area.

## Problem Statement

### What problem are we solving?

Finding new restaurants and bars that match your personal taste is time-consuming and hit-or-miss. Existing recommendation systems are generic and don't learn from your actual preferences. People end up visiting the same familiar places or wasting time and money on disappointing experiences.

### Who experiences this problem?

Food enthusiasts, travelers, and anyone who wants to discover great dining experiences that match their specific preferences for cuisine, atmosphere, price point, and style.

### Why is this problem worth solving?

Dining out is a significant investment of time and money. Poor recommendations lead to disappointing experiences, while good personalized recommendations can help people discover hidden gems and expand their culinary horizons with confidence.

## Target Users

### Primary Users

Individuals who dine out regularly and want personalized recommendations based on their proven preferences. They value discovering new places that match their taste rather than relying on generic "top rated" lists.

### Secondary Users

Travelers and food enthusiasts exploring new cities who want recommendations that align with their established preferences from home.

## Product Goals

1. Build accurate user preference profiles from liked establishments
2. Provide personalized restaurant/bar recommendations for any geographic area
3. Save users time and reduce disappointment by matching their taste preferences
4. Create a flexible, extensible architecture that can evolve (recommendation engines, data sources, interfaces)

## Core Features

### Must Have (MVP)

- [ ] Accept user input of restaurant/bar names they like
- [ ] Fetch establishment data from Yelp Fusion API
- [ ] Build and store user preference profile locally (JSON file)
- [ ] Generate customer profiles for establishments (e.g., "tourist", "finance bro", "bedstuy local")
- [ ] Accept queries for recommendations in a specific geographic area
- [ ] Generate personalized recommendations (multi-phase: ML similarity + LLM filtering)
- [ ] Output recommendations to JSON file with attributes and customer profiles
- [ ] CLI interface for all interactions

### Should Have

- [ ] Support for multiple profiles (different users or different "moods")
- [ ] Ability to remove/update establishments in profile
- [ ] View current profile summary
- [ ] Filter recommendations by specific criteria (price, cuisine, distance)
- [ ] Export/import profile data

### Nice to Have

- [ ] Gather establishment feedback from public forums (Reddit, etc.) for authentic user opinions
- [ ] Web UI interface
- [ ] Multiple data source support (Google Places, Foursquare)
- [ ] Database storage for profiles
- [ ] Multi-user support with accounts
- [ ] Mobile app
- [ ] Integration with reservation systems
- [ ] Photo-based preference learning

## User Stories

1. As a food enthusiast, I want to add restaurants I love to my profile so that Graze learns my preferences
2. As a traveler, I want to ask for recommendations in a new city so that I can find places I'll enjoy
3. As a user, I want the system to consider price, cuisine, and atmosphere so that recommendations match my complete preferences
4. As a user, I want to see what kind of crowd frequents a place (e.g., "finance bros", "tourists") so that I know if it's my scene
5. As a user, I want to view my taste profile so that I understand what Graze has learned about me
6. As a user, I want recommendations based on real community feedback so that I avoid tourist traps and find authentic experiences
7. As a user, I want recommendations exported to a JSON file so that I can review them and integrate with other tools

## Success Metrics

- **Profile Quality**: User can successfully build a profile with 10+ establishments
- **Recommendation Relevance**: Recommendations match user preferences (manual validation initially)
- **User Satisfaction**: Users try recommended places and add them to their profile
- **Response Time**: Recommendations generated in < 10 seconds
- **API Reliability**: < 5% failure rate when fetching establishment data

## Out of Scope

*For MVP, we are explicitly NOT building:*

- User accounts or authentication
- Database storage (using local files only)
- Web or mobile interfaces (CLI only)
- Real-time data sync
- Social features (sharing profiles, following friends)
- Reservation booking
- Payment or monetization features
- AI-generated reviews or content moderation
- Multiple data sources beyond Yelp

## Technical Considerations

### Constraints

- Python 3.13+
- Command-line interface
- Local file storage (JSON or similar)
- API rate limits (Yelp: 5,000 calls/day on free tier)
- LLM API costs and rate limits

### Dependencies

- **Yelp Fusion API**: Restaurant/bar data, ratings, attributes, location info
- **ML Model**: For initial similarity matching (cheaper, faster)
- **LLM API**: For atmosphere/sentiment filtering and customer profiling
- **Python libraries**: HTTP client, JSON parsing, CLI framework

### Architecture Principles

- **Multi-phase recommendation**:
  - Phase 1: ML-based similarity matching (cost-effective filtering)
  - Phase 2: LLM-based refinement (atmosphere, sentiment, customer profiling)
- **Pluggable recommendation engine**: Interface-based design to swap ML/LLM providers
- **Pluggable data sources**: Design to support adding Google Places, Foursquare, etc. later
- **Simple first**: Start with straightforward implementations, add complexity only when needed
- **Type safety**: Full type annotations with mypy checking

### Performance Requirements

- Recommendations generated in < 10 seconds
- Support profiles with 100+ establishments
- Handle API failures gracefully with retries
- Minimize redundant API calls (caching where appropriate)

## Open Questions

- [ ] Which ML model for similarity matching? (scikit-learn, sentence transformers, embeddings API?)
- [ ] Which LLM API for refinement phase? (OpenAI GPT-4, Claude, other?)
- [ ] How do we handle ambiguous restaurant names? (multiple matches in Yelp - show user a list to choose from?)
- [ ] What attributes should we track in user profile?
  - Confirmed: price level, cuisine type, atmosphere
  - To consider: distance preferences, meal type (brunch, dinner), noise level, dietary restrictions?
- [ ] How do we generate customer profiles? (LLM analysis of reviews, manual categorization, hybrid?)
- [ ] Should recommendations include explanations of why they were suggested?
- [ ] What's the JSON output schema for recommendations?

## Data Models

### Recommendation Output (JSON)

Each recommendation should include:

- **name**: Establishment name
- **location**: Address and/or coordinates
- **price_level**: $ to $$$$ (or 1-4 numeric)
- **cuisine_type**: List of cuisine categories
- **atmosphere**: Description or tags (e.g., "casual", "upscale", "dive bar")
- **rating**: Yelp rating
- **customer_profile**: Colloquial description of typical clientele (e.g., "finance bros", "bedstuy locals", "tourists", "artists", "college students")
- **why_recommended**: Optional explanation of match to user preferences
- **source**: "yelp" (for future: "google", "reddit", etc.)

### Customer Profile Examples

Simple, colloquial terms that capture the vibe:

- "tourists"
- "finance bros"
- "bedstuy locals"
- "brooklyn creatives"
- "college students"
- "young families"
- "food nerds"
- "late night crowd"
- "brunch crowd"
- "neighborhood regulars"

## Timeline & Milestones

### Phase 1: MVP (CLI + Basic Recommendations)

- Core CLI interface
- Yelp API integration
- User profile management (add/view establishments)
- LLM-based recommendations
- Local file storage

### Phase 2: Enhanced Data & Recommendations

- Reddit/forum integration for authentic user feedback
- Profile editing and management
- Better attribute tracking
- Recommendation filtering

**Phase 3: Future Expansion**

- Multiple profile support
- Web UI
- Additional data sources (Google Places, Foursquare)
- Database storage

---

**Last Updated:** 2025-12-21
**Status:** Draft
