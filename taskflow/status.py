"""Helpers for counting tasks by status."""

from collections.abc import Iterable
from typing import Any


def count_by_status(tasks: Iterable[dict[str, Any]]) -> dict[str, int]:
    """Return the number of tasks for each normalized status.

    Missing, empty, and non-string statuses are counted as ``"unknown"``.
    """
    counts: dict[str, int] = {}

    for task in tasks:
        status = task.get("status")
        if isinstance(status, str):
            status = status.strip().lower()
        if not status:
            status = "unknown"

        counts[status] = counts.get(status, 0) + 1

    return counts
