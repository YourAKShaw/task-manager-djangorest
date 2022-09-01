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
        return filter(lambda task: task["completed"] == completed, TaskService.tasks)

    @classmethod
    def get_task(cls, taskId):
        return next((task for task in TaskService.tasks if task["id"] == taskId), None)

    @classmethod
    def update_task(cls, taskId, update_task_dto):
        pass

    @classmethod
    def delete_task(cls, taskId):
        pass
