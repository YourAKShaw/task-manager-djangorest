from common.helpers.deadline_validator import deadline_validator
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.exceptions import APIException, ParseError, ValidationError, NotFound
from rest_framework.response import Response
from taskmanager.utils import Logger

from task.serializers import TaskSerializer
from task.service import TaskService
from task.validators import validate_create_task_request_data, validate_update_task_request_data


class TaskViewSet(viewsets.ViewSet):

    def list(self, request):
        try:
            serializer_class = TaskSerializer(TaskService.get_tasks(
                completed=request.query_params.get('completed')), many=True)
            return Response(serializer_class.data, status=status.HTTP_200_OK)
        except Exception as e:
            Logger.error(msg=str(e))
            raise APIException(detail=str(e))

    def create(self, request):
        try:
            validation_result = validate_create_task_request_data(request.data)
            if (not validation_result["success"]):
                raise ParseError(detail=validation_result["errors"])
            deadline = request.data.get("deadline")
            if (deadline and not deadline_validator(deadline)):
                raise ValidationError(detail="Invalid deadline")
            task = TaskService.create_task(create_task_dto=request.data)
            Logger.info(msg=f'task created with id {task["id"]}')
            serializer_class = TaskSerializer(data=task)
            serializer_class.is_valid()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        except ParseError as e:
            Logger.error(msg=str(e))
            return Response({
                "status": e.status_code,
                "message": e.detail
            }, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError as e:
            Logger.error(msg=str(e))
            return Response({
                "status": e.status_code,
                "message": e.detail
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            Logger.error(msg=str(e))
            raise APIException(detail=str(e))

    def retrieve(self, request, pk=None):
        try:
            task = TaskService.get_task(taskId=int(pk))
            if (not task):
                raise NotFound(detail=f'task with id {pk} not found')
            serializer_class = TaskSerializer(task)
            return Response(serializer_class.data, status=status.HTTP_200_OK)
        except NotFound as e:
            Logger.error(msg=str(e))
            return Response({
                "status": e.status_code,
                "message": e.detail
            }, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            Logger.error(msg=str(e))
            raise APIException(detail=str(e))

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        try:
            validation_result = validate_update_task_request_data(request.data)
            if (not validation_result["success"]):
                raise ParseError(detail=validation_result["errors"])
            deadline = request.data.get("deadline")
            if (deadline and not deadline_validator(deadline)):
                raise ValidationError(detail="Invalid deadline")
            task = TaskService.update_task(
                taskId=int(pk), update_task_dto=request.data)
            if (not task):
                raise NotFound(detail=f'task with id {pk} not found')
            Logger.info(msg=f'task updated with id {task["id"]}')
            serializer_class = TaskSerializer(data=task)
            serializer_class.is_valid()
            return Response(serializer_class.data, status=status.HTTP_200_OK)
        except ParseError as e:
            Logger.error(msg=str(e))
            return Response({
                "status": e.status_code,
                "message": e.detail
            }, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError as e:
            Logger.error(msg=str(e))
            return Response({
                "status": e.status_code,
                "message": e.detail
            }, status=status.HTTP_400_BAD_REQUEST)
        except NotFound as e:
            Logger.error(msg=str(e))
            return Response({
                "status": e.status_code,
                "message": e.detail
            }, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            Logger.error(msg=str(e))
            raise APIException(detail=str(e))

    def destroy(self, request, pk=None):
        pass
