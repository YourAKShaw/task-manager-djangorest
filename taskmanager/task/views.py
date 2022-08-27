from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

tasks = []


@api_view(['GET'])
def get_all_tasks(req):
    return Response({
        "statusCode": 200,
        "message": "success",
        "data": tasks
    })
