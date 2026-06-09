from datetime import datetime


def validate_task_title(title):
    if title is None:
        raise ValueError("Task title cannot be empty.")

    title = title.strip()

    if len(title) == 0:
        raise ValueError("Task title cannot be empty.")

    return True


def validate_task_description(description):
    if description is None:
        raise ValueError("Task description cannot be empty.")

    description = description.strip()

    if len(description) == 0:
        raise ValueError("Task description cannot be empty.")

    return True


def validate_due_date(due_date):
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Due date must be in YYYY-MM-DD format.")

    return True
