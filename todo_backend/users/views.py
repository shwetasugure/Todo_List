from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Task
from .forms import TaskForm
from django.contrib.auth.forms import UserCreationForm
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

# User login view
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # Log in the user
            # Generate JWT token
            refresh = RefreshToken.for_user(user)
            request.session['refresh'] = str(refresh)
            request.session['access'] = str(refresh.access_token)
            return redirect('task_list')  # Redirect to task list after login
        else:
            return render(request, 'users/login.html', {'error': 'Invalid credentials'})  # Display error

    return render(request, 'users/login.html')

# User signup view
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('task_list')  # Redirect to task list after signup
    else:
        form = UserCreationForm()
    return render(request, 'users/signup.html', {'form': form})

# User logout view
@login_required
def user_logout(request):
    logout(request)
    return redirect('login')  # Redirect after logout

# Task list view
@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    refresh_token = request.session.get('refresh')
    access_token = request.session.get('access')

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()

    return render(request, 'users/task_list.html', {
        'tasks': tasks,
        'form': form,
        'refresh_token': refresh_token,
        'access_token': access_token
    })

# Delete task view
@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.delete()
    return redirect('task_list')

# Update task view
@login_required
def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'users/update_task.html', {'form': form, 'task': task})

# Task list API view
class TaskListView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tasks = Task.objects.filter(user=request.user)
        task_data = [{'id': task.id, 'title': task.title} for task in tasks]  # Customize fields as needed
        return Response({'tasks': task_data})

    def post(self, request):
        form = TaskForm(request.data)  # Use request.data for DRF
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return Response({'message': 'Task added successfully'})
        return Response({'error': 'Form is invalid'}, status=400)
