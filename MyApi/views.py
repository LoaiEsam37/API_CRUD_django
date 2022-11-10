from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Create':'/task-create/',
        'Read':'/task-detail/<str:id>/',
        'overview':'/task-overview/',
        'Update':'/task-update/<str:id>/',
        'Delete':'/task-delete/<str:id>/'
    }
    return Response(api_urls)

# Create
@api_view(['POST'])
def TaskCreate(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# Read
@api_view(['GET'])
def TaskDetail(request, id):
    task = Task.objects.get(id=id)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)

# Read
@api_view(['GET'])
def TaskOverview(request):
    task = Task.objects.all()
    serializer = TaskSerializer(task, many=True)
    return Response(serializer.data)

# Update
@api_view(['POST'])
def TaskUpdate(request, id):
    task = Task.objects.get(id=id)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# Delete
@api_view(['DELETE'])
def TaskDelete(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return Response('Deleted Successfully!')