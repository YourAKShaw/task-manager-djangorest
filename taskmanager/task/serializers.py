from rest_framework import serializers
from task.models import Task, Note


class NoteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Note
        fields = ('title', 'body')

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('id', 'title', 'description',
                  'deadline', 'notes', 'completed')


class CreateTaskSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100, required=True)
    description = serializers.CharField()
    deadline = serializers.RegexField(regex=r'^\d{2}\/\d{2}\/\d{4}$')
    notes = NoteSerializer(required=False, many=True)
