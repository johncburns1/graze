"""Tests for graze."""

import graze


def test_version() -> None:
    """Test that version is defined."""
    assert graze.__version__ == "0.1.0"
