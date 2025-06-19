from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer

@api_view(['GET', 'POST'])
def task_list(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response({
            'status': 'success',
            'data': serializer.data,
            'message': 'Tasks retrieved successfully'
        })
    
    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': 'success',
                'data': serializer.data,
                'message': 'Task created successfully'
            }, status=status.HTTP_201_CREATED)
        return Response({
            'status': 'error',
            'errors': serializer.errors,
            'message': 'Task creation failed'
        }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def health_check(request):
    return Response({
        'status': 'success',
        'message': 'API is healthy',
        'version': '1.0.0'
    })