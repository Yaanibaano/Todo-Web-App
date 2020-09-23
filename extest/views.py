from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serialize import TaskSerializer
from .models import Task

@api_view(["GET"])
def do_this(request):
    api_response = {
        "hello":"oh hi hello",
        "ok":"ok bye"
    }
    return Response(api_response)

@api_view(["Get"])
def TaskView(request):
    task = Task.objects.all()
    serializer = TaskSerializer(task,many=True)
    return Response(serializer.data)


@api_view(["GET"])
def task_detail(request,task_id):
    task = Task.objects.get(id=task_id)
    serializer = TaskSerializer(task,many=False)
    return Response(serializer.data)

@api_view(["POST"])
def task_create(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(["POST"])
def task_update(request,task_id):
    item = Task.objects.get(id=task_id)
    serializer = TaskSerializer(instance = item ,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(["DELETE"])
def task_delete(request,task_id):
    item = Task.objects.get(id=task_id)
    item.delete()
    return Response("Item deleted")
