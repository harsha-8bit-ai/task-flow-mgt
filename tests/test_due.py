from datetime import date

from taskflow.due import overdue_tasks


def test_overdue_tasks_accepts_date_objects_and_iso_strings():
    tasks = [
        {"title": "Date task", "due_date": date(2024, 1, 1)},
        {"title": "String task", "due_date": "2024-01-02"},
        {"title": "Today", "due_date": date(2024, 1, 3)},
        {"title": "Future", "due_date": "2024-01-04"},
    ]

    assert [task["title"] for task in overdue_tasks(tasks, date(2024, 1, 3))] == [
        "Date task",
        "String task",
    ]


def test_overdue_tasks_accepts_any_iterable():
    tasks = ({"title": "Old", "due_date": "2024-01-01"},)

    assert overdue_tasks(iter(tasks), date(2024, 1, 2)) == list(tasks)


def test_overdue_tasks_skips_missing_none_and_invalid_due_dates():
    tasks = [
        {"title": "Missing"},
        {"title": "None", "due_date": None},
        {"title": "Invalid", "due_date": "not-a-date"},
        {"title": "Valid", "due_date": "2024-01-01"},
    ]

    assert [task["title"] for task in overdue_tasks(tasks, date(2024, 1, 2))] == [
        "Valid"
    ]


def test_overdue_tasks_skips_done_status_case_insensitively_and_with_whitespace():
    tasks = [
        {"title": "Done lower", "status": "done", "due_date": "2024-01-01"},
        {"title": "Done mixed", "status": "  DoNe ", "due_date": "2024-01-01"},
        {"title": "Open", "status": "in progress", "due_date": "2024-01-01"},
    ]

    assert [task["title"] for task in overdue_tasks(tasks, date(2024, 1, 2))] == [
        "Open"
    ]


def test_overdue_tasks_sorts_oldest_first_and_is_stable_for_equal_dates():
    tasks = [
        {"title": "Newer", "due_date": "2024-01-03"},
        {"title": "First same", "due_date": "2024-01-01"},
        {"title": "Second same", "due_date": date(2024, 1, 1)},
        {"title": "Older", "due_date": "2023-12-31"},
    ]

    assert [task["title"] for task in overdue_tasks(tasks, date(2024, 1, 4))] == [
        "Older",
        "First same",
        "Second same",
        "Newer",
    ]


def test_overdue_tasks_does_not_modify_input_list_or_dicts():
    tasks = [
        {"title": "Later", "due_date": "2024-01-02"},
        {"title": "Earlier", "due_date": "2024-01-01"},
    ]
    original_tasks = [task.copy() for task in tasks]

    result = overdue_tasks(tasks, date(2024, 1, 3))

    assert result is not tasks
    assert tasks == original_tasks
    assert [task["title"] for task in result] == ["Earlier", "Later"]
