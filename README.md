# Task Flow Management

## Priority helper

The `sort_tasks` helper sorts tasks by priority in the order high, medium, and low. Priority matching is case-insensitive and ignores surrounding whitespace. Tasks with an unknown, missing, or `None` priority are sorted last. Sorting is stable, so tasks with equivalent priorities retain their original order, and the input list and task dictionaries are not modified.

## Status counts

The `count_by_status` helper returns the number of tasks for each status. Statuses are matched case-insensitively after surrounding whitespace is removed; missing, empty, and non-string statuses are counted as `unknown`.
