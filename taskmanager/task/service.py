from common.helpers.generate_id import generate_id


class TaskService:
    tasks = []

    @classmethod
    def create_task(cls, create_task_dto):
        task = {
            "id": generate_id(),
            "title": create_task_dto.get("title"),
            "description": create_task_dto.get("description"),
            "deadline": create_task_dto.get("deadline"),
            "notes": create_task_dto.get("notes") or [],
            "completed": False
        }
        TaskService.tasks.append(task)
        return task

    @classmethod
    def get_tasks(cls, completed=None):
        if (completed is None):
            return TaskService.tasks
        completed = completed == 'true'
        filtered_tasks = []
        for task in TaskService.tasks:
            if task["completed"] == completed:
                filtered_tasks.append(task)
        return filtered_tasks

    @classmethod
    def get_task(cls, taskId):
        return next((task for task in TaskService.tasks if task["id"] == taskId), None)

    @classmethod
    def update_task(cls, taskId, update_task_dto):
        task = TaskService.get_task(taskId)
        if (task is None):
            return None
        task.update(update_task_dto)
        return task

    @classmethod
    def delete_task(cls, taskId):
        task = TaskService.get_task(taskId)
        try:
            TaskService.tasks.remove(task)
        except:
            pass
        return task
