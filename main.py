"""
Simple counter tool for testing persistent mode.
State is maintained in memory between calls.
"""

import json

# Global state - persists between calls in persistent mode
_counter = 0


def get() -> str:
    """Get the current counter value."""
    return json.dumps({"value": _counter})


def increment(n: int = 1) -> str:
    """Increment the counter by n."""
    global _counter
    _counter += n
    return json.dumps({"value": _counter})


def decrement(n: int = 1) -> str:
    """Decrement the counter by n."""
    global _counter
    _counter -= n
    return json.dumps({"value": _counter})


def reset(value: int = 0) -> str:
    """Reset the counter to a value."""
    global _counter
    _counter = value
    return json.dumps({"value": _counter})


def health() -> str:
    """Health check."""
    return json.dumps({"status": "ok"})
