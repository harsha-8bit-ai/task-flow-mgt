from taskflow.priority import sort_tasks


def test_sort_tasks_orders_high_medium_and_low_priorities():
    tasks = [
        {"title": "Write notes", "priority": "low"},
        {"title": "Fix outage", "priority": "high"},
        {"title": "Review change", "priority": "medium"},
    ]

    assert [task["title"] for task in sort_tasks(tasks)] == [
        "Fix outage",
        "Review change",
        "Write notes",
    ]


def test_sort_tasks_preserves_order_within_same_priority():
    tasks = [
        {"title": "First high task", "priority": "high"},
        {"title": "Medium task", "priority": "medium"},
        {"title": "Second high task", "priority": "high"},
    ]

    assert [task["title"] for task in sort_tasks(tasks)] == [
        "First high task",
        "Second high task",
        "Medium task",
    ]


def test_sort_tasks_places_unknown_priorities_last():
    tasks = [
        {"title": "Unknown task", "priority": "urgent"},
        {"title": "High task", "priority": "high"},
    ]

    assert [task["title"] for task in sort_tasks(tasks)] == [
        "High task",
        "Unknown task",
    ]


def test_sort_tasks_handles_mixed_case_priorities():
    tasks = [
        {"title": "Low task", "priority": "lOw"},
        {"title": "High task", "priority": "High"},
        {"title": "Medium task", "priority": "MEDIUM"},
    ]

    assert [task["title"] for task in sort_tasks(tasks)] == [
        "High task",
        "Medium task",
        "Low task",
    ]


def test_sort_tasks_ignores_surrounding_whitespace():
    tasks = [
        {"title": "Low task", "priority": " low "},
        {"title": "High task", "priority": "\thigh\n"},
    ]

    assert [task["title"] for task in sort_tasks(tasks)] == [
        "High task",
        "Low task",
    ]


def test_sort_tasks_places_missing_and_none_priorities_last():
    tasks = [
        {"title": "Missing priority"},
        {"title": "None priority", "priority": None},
        {"title": "High task", "priority": "high"},
    ]

    assert [task["title"] for task in sort_tasks(tasks)] == [
        "High task",
        "Missing priority",
        "None priority",
    ]


def test_sort_tasks_is_stable_for_equivalent_priorities():
    tasks = [
        {"title": "First", "priority": "High"},
        {"title": "Second", "priority": " high "},
        {"title": "Third", "priority": "HIGH"},
    ]

    assert [task["title"] for task in sort_tasks(tasks)] == [
        "First",
        "Second",
        "Third",
    ]


def test_sort_tasks_does_not_mutate_input():
    tasks = [
        {"title": "Low task", "priority": " low "},
        {"title": "High task", "priority": "HIGH"},
    ]
    original_tasks = [task.copy() for task in tasks]

    result = sort_tasks(tasks)

    assert result is not tasks
    assert tasks == original_tasks
    assert all(result_task is not input_task for result_task, input_task in zip(result, tasks))
    assert all(task == original for task, original in zip(tasks, original_tasks))
