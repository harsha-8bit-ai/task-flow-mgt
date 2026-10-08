# Task Flow Management

## Priority helper

The `sort_tasks` helper sorts tasks by priority in the order high, medium, and low. Priority matching is case-insensitive and ignores surrounding whitespace. Tasks with an unknown, missing, or `None` priority are sorted last. Sorting is stable, so tasks with equivalent priorities retain their original order, and the input list and task dictionaries are not modified.
