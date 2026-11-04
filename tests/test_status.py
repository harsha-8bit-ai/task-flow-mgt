from taskflow.status import count_by_status


def test_count_by_status_accepts_an_iterable_of_task_dicts():
    tasks = ({"status": status} for status in ["todo", "done"])

    assert count_by_status(tasks) == {"todo": 1, "done": 1}


def test_count_by_status_reads_each_task_status():
    tasks = [{"status": "todo"}, {"status": "done"}]

    assert count_by_status(tasks) == {"todo": 1, "done": 1}


def test_count_by_status_strips_and_lowercases_string_statuses():
    tasks = [
        {"status": " TODO "},
        {"status": "todo"},
        {"status": "\tDone\n"},
    ]

    assert count_by_status(tasks) == {"todo": 2, "done": 1}


def test_count_by_status_uses_unknown_for_missing_empty_and_non_string_statuses():
    tasks = [
        {},
        {"status": None},
        {"status": ""},
        {"status": "   "},
        {"status": 1},
        {"status": ["todo"]},
    ]

    assert count_by_status(tasks) == {"unknown": 6}


def test_count_by_status_counts_each_status():
    tasks = [
        {"status": "todo"},
        {"status": "done"},
        {"status": "TODO"},
        {"status": "blocked"},
        {"status": "done"},
    ]

    assert count_by_status(tasks) == {"todo": 2, "done": 2, "blocked": 1}


def test_count_by_status_returns_empty_dict_for_empty_input():
    assert count_by_status([]) == {}


def test_count_by_status_does_not_modify_input_or_task_dicts():
    tasks = [{"status": " TODO ", "title": "Write tests"}, {"status": None}]
    original_tasks = [task.copy() for task in tasks]

    result = count_by_status(tasks)

    assert result == {"todo": 1, "unknown": 1}
    assert tasks == original_tasks
