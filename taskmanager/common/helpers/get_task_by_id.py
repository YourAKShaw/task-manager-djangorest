def get_task_by_id(tasks, id):
    for task in tasks:
        if (task["id"] == id):
            return task
    return None
