"""Helpers for ordering tasks by priority."""

from collections.abc import Iterable
from typing import Any


_PRIORITY_ORDER = {"high": 0, "medium": 1, "low": 2}


def sort_tasks(tasks: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
    """Return tasks ordered from high to low priority.

    Tasks with unknown priorities are placed after known priorities. Python's
    stable sort preserves the original order of tasks with equal priorities.
    """

    return sorted(tasks, key=lambda task: _PRIORITY_ORDER.get(task["priority"], 3))
