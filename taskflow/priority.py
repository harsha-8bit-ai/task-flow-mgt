"""Helpers for ordering tasks by priority."""

from collections.abc import Iterable
from typing import Any


_PRIORITY_ORDER = {"high": 0, "medium": 1, "low": 2}


def sort_tasks(tasks: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
    """Return tasks ordered from high to low priority.

    Priority matching is case-insensitive and ignores surrounding whitespace.
    Tasks with missing, None, or unknown priorities are placed after known
    priorities. Python's stable sort preserves the original order of tasks
    with equal priorities.
    """

    def priority_order(task: dict[str, Any]) -> int:
        priority = task.get("priority")
        if isinstance(priority, str):
            priority = priority.strip().lower()
        return _PRIORITY_ORDER.get(priority, 3)

    return sorted(tasks, key=priority_order)
