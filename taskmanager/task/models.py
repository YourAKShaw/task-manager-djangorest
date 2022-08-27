# from django.db import models

"""NOTE:
Since this project revolves around an in memory (NO DATABASE) app, we don't need to use django models
"""


class Note:
    title = ""
    body = ""

    def __init__(self, title, body):
        self.title = title
        self.body = body


class Task:
    id = 0
    title = ""
    description = ""
    deadline = "28/08/2022"
    notes = []
    completed = False

    def __init__(self, id, title, description, deadline, notes, completed):
        self.id = id
        self.title = title
        self.description = description
        self.deadline = deadline
        self.notes = notes
        self.completed = completed
