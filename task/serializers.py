from rest_framework import serializers
from task.models import Task, Note


class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'


class CreateTaskSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100, required=True)
    description = serializers.CharField(required=False)
    deadline = serializers.RegexField(
        regex=r'^\d{2}\/\d{2}\/\d{4}$', required=False)
    notes = NoteSerializer(required=False, many=True)


class UpdateTaskSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100, required=False)
    description = serializers.CharField(required=False)
    deadline = serializers.RegexField(
        regex=r'^\d{2}\/\d{2}\/\d{4}$', required=False)
    notes = NoteSerializer(required=False, many=True)
    completed = serializers.BooleanField(required=False)
