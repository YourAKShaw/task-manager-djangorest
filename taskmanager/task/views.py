from common.helpers.deadline_validator import deadline_validator
from common.helpers.generate_id import generate_id
from rest_framework import status, viewsets
from rest_framework.exceptions import APIException, ParseError, ValidationError
from rest_framework.response import Response
from taskmanager.utils import Logger

from task.serializers import TaskSerializer
from task.validators import validate_create_task_request_data

tasks = []


class TaskViewSet(viewsets.ViewSet):
    queryset = tasks

    def list(self, request):
        serializer_class = TaskSerializer(self.queryset, many=True)
        return Response(serializer_class.data, status=status.HTTP_200_OK)

    def create(self, request):
        try:
            validation_result = validate_create_task_request_data(request.data)
            if (not validation_result["success"]):
                raise ParseError(detail=validation_result["errors"])
            deadline = request.data.get("deadline")
            if (deadline and not deadline_validator(deadline)):
                raise ValidationError(detail="Invalid deadline")
            task = {
                "id": generate_id(),
                "title": request.data.get("title"),
                "description": request.data.get("description"),
                "deadline": request.data.get("deadline"),
                "notes": request.data.get("notes") or [],
                "completed": False
            }
            tasks.append(task)
            Logger.info(msg=f'task created with id {task["id"]}')
            serializer_class = TaskSerializer(data=task)
            serializer_class.is_valid()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            Logger.error(msg=str(e))
            raise APIException(detail=str(e))

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
