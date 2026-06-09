# Import validation functions
from task_manager.validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date
)

# Define tasks list
tasks = []


# Implement add_task function
def add_task(title, description, due_date):
    try:
        validate_task_title(title)
        validate_task_description(description)
        validate_due_date(due_date)
    except ValueError as error:
        print(f"Error: {error}")
        return False

    task = {
        "title": title.strip(),
        "description": description.strip(),
        "due_date": due_date,
        "completed": False
    }

    tasks.append(task)
    print("Task added successfully!")
    return True


# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    if len(tasks) == 0:
        print("No tasks available.")
        return False

    if index < 0 or index >= len(tasks):
        print("Invalid task number.")
        return False

    tasks[index]["completed"] = True
    print("Task marked as complete!")
    return True


# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    pending_tasks = []

    for task in tasks:
        if task["completed"] == False:
            pending_tasks.append(task)

    if len(pending_tasks) == 0:
        print("No pending tasks.")
    else:
        print("\nPending Tasks:")
        for i, task in enumerate(pending_tasks):
            print(f"{i + 1}. {task['title']}")
            print(f"   Description: {task['description']}")
            print(f"   Due Date: {task['due_date']}")

    return pending_tasks


# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    if len(tasks) == 0:
        return 0

    completed_tasks = 0

    for task in tasks:
        if task["completed"] == True:
            completed_tasks += 1

    progress = (completed_tasks / len(tasks)) * 100
    return progress
