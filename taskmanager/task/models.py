from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(null=True)

    def __str__(self):
        return self.title


class Task(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    deadline = models.CharField(max_length=10)
    notes = models.ManyToManyField(Note)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
