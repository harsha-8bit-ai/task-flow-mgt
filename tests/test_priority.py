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
        {"title": "Another unknown task", "priority": "custom"},
    ]

    assert [task["title"] for task in sort_tasks(tasks)] == [
        "High task",
        "Unknown task",
        "Another unknown task",
    ]
