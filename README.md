# Task Flow Management

## Priority helpers

Use `taskflow.priority.sort_tasks` to order task dictionaries by priority:

```python
from taskflow.priority import sort_tasks

tasks = sort_tasks([
    {"title": "Review", "priority": "medium"},
    {"title": "Deploy", "priority": "high"},
])
```

Tasks are returned in `high`, `medium`, then `low` priority order. The sort is
stable, so tasks with the same priority retain their original order. Unknown
priority values are placed after the known priorities.