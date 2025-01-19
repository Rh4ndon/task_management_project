from django.shortcuts import render
from django.http import JsonResponse
from .models import User, Task
import json
from django.views.decorators.csrf import csrf_exempt

# Get all users
def get_users(request):
    users = list(User.objects.values('id', 'username', 'email', 'created_at'))
    return JsonResponse(users, safe=False)

# Create a new user
@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = User.objects.create(username=data['username'], email=data['email'])
        return JsonResponse({'id': user.id, 'message': 'User created successfully'}, status=201)

# Get all tasks
def get_tasks(request):
    tasks = list(Task.objects.values('id', 'title', 'description', 'is_completed', 'user', 'created_at'))
    return JsonResponse(tasks, safe=False)

# Create a new task
@csrf_exempt
def create_task(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = User.objects.get(id=data['user'])
        task = Task.objects.create(title=data['title'], description=data.get('description', ''), user=user)
        return JsonResponse({'id': task.id, 'message': 'Task created successfully'}, status=201)
