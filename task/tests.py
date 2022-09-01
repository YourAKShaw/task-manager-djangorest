from django.test import TestCase
from task.service import TaskService


class TaskTestCase(TestCase):

    def test_a_create_task(self):
        task = TaskService.create_task(
            {
                "title": "Test Task",
                "description": "Test Description",
                "deadline": "01/01/2020",
                "notes": []
            })

        self.assertEqual(len(str(task["id"])), 6)
        self.assertEqual(task["title"], "Test Task")
        self.assertEqual(task["description"], "Test Description")
        self.assertEqual(task["deadline"], "01/01/2020")
        self.assertEqual(task["notes"], [])
        self.assertEqual(task["completed"], False)

        task2 = TaskService.create_task(
            {
                "title": "Test Task 2",
                "description": "Test Description 2",
                "deadline": "01/01/2020",
                "notes": [
                    {
                        "title": "Test Note",
                        "body": "Test Body"
                    }
                ]
            })

        self.assertEqual(len(str(task2["id"])), 6)
        self.assertEqual(task2["title"], "Test Task 2")
        self.assertEqual(task2["description"], "Test Description 2")
        self.assertEqual(task2["deadline"], "01/01/2020")
        self.assertEqual(task2["notes"], [
            {
                "title": "Test Note",
                "body": "Test Body"
            }
        ])
        self.assertEqual(task2["completed"], False)

    def test_b_get_tasks(self):
        tasks = TaskService.get_tasks()
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[1]["title"], "Test Task 2")
        self.assertEqual(tasks[1]["description"], "Test Description 2")
        self.assertEqual(tasks[1]["deadline"], "01/01/2020")
        self.assertEqual(tasks[1]["notes"], [
            {
                "title": "Test Note",
                "body": "Test Body"
            }
        ])
        self.assertEqual(tasks[1]["completed"], False)

    def test_c_get_task(self):
        task = TaskService.get_tasks()[1]
        taskId = task["id"]
        task = TaskService.get_task(taskId)
        self.assertEquals(task["id"], taskId)
        self.assertEquals(task["title"], "Test Task 2")
        self.assertEquals(task["description"], "Test Description 2")
        self.assertEquals(task["deadline"], "01/01/2020")
        self.assertEquals(task["notes"], [
            {
                "title": "Test Note",
                "body": "Test Body"
            }
        ])
        self.assertEquals(task["completed"], False)

    def test_d_update_task(self):
        task = TaskService.get_tasks()[1]
        taskId = task["id"]
        task = TaskService.update_task(taskId, {
            "title": "Test Task 2 Updated",
            "description": "Test Description 2 Updated",
            "deadline": "01/01/2022",
            "notes": [
                {
                    "title": "Test Note Updated",
                    "body": "Test Body Updated"
                }
            ],
            "completed": True
        })
        self.assertEquals(task["id"], taskId)
        self.assertEquals(task["title"], "Test Task 2 Updated")
        self.assertEquals(task["description"], "Test Description 2 Updated")
        self.assertEquals(task["deadline"], "01/01/2022")
        self.assertEquals(task["notes"], [
            {
                "title": "Test Note Updated",
                "body": "Test Body Updated"
            }
        ])
        self.assertEquals(task["completed"], True)

    def test_e_get_task_completed_true(self):
        tasks = TaskService.get_tasks(completed='true')
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["title"], "Test Task 2 Updated")
        self.assertEqual(tasks[0]["description"], "Test Description 2 Updated")
        self.assertEqual(tasks[0]["deadline"], "01/01/2022")
        self.assertEqual(tasks[0]["notes"], [
            {
                "title": "Test Note Updated",
                "body": "Test Body Updated"
            }
        ])
        self.assertEqual(tasks[0]["completed"], True)

    def test_f_get_task_completed_false(self):
        tasks = TaskService.get_tasks(completed='false')
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["title"], "Test Task")
        self.assertEqual(tasks[0]["description"], "Test Description")
        self.assertEqual(tasks[0]["deadline"], "01/01/2020")
        self.assertEqual(tasks[0]["notes"], [])
        self.assertEqual(tasks[0]["completed"], False)

    def test_g_delete_task(self):
        task = TaskService.get_tasks()[1]
        taskId = task["id"]
        TaskService.delete_task(taskId)
        task = TaskService.get_task(taskId)
        self.assertEquals(task, None)
        tasks = TaskService.get_tasks()
        self.assertEqual(len(tasks), 1)
