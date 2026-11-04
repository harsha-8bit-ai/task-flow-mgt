"""Helpers for finding overdue tasks."""

from collections.abc import Iterable
from datetime import date, datetime
from typing import Any


def _parse_due_date(value: Any) -> date | None:
    if isinstance(value, date) and not isinstance(value, datetime):
        return value
    if isinstance(value, str):
        try:
            return date.fromisoformat(value)
        except ValueError:
            return None
    return None


def overdue_tasks(tasks: Iterable[dict[str, Any]], today: date) -> list[dict[str, Any]]:
    """Return unfinished tasks whose due dates precede ``today``.

    Due dates may be ``date`` objects or ISO-formatted date strings. Tasks with
    missing or invalid due dates, and tasks marked done, are ignored. Sorting
    is stable, so tasks with equal due dates retain their input order.
    """

    overdue: list[tuple[date, dict[str, Any]]] = []
    for task in tasks:
        status = task.get("status")
        if isinstance(status, str) and status.strip().lower() == "done":
            continue

        due_date = _parse_due_date(task.get("due_date"))
        if due_date is not None and due_date < today:
            overdue.append((due_date, task))

    return [task for _, task in sorted(overdue, key=lambda item: item[0])]
