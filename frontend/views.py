from django.shortcuts import render, redirect, get_object_or_404
from api.models import Task



# READ (buildList equivalent)
def task_list(request):
    tasks = Task.objects.all()
    return render(request, "frontend/task_list.html", {"tasks": tasks})


# CREATE
def task_create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        Task.objects.create(title=title)
    return redirect("task-list")


# DELETE
def task_delete(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.delete()
    return redirect("task-list")


# TOGGLE COMPLETE (strike/unstrike)
def task_toggle(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.completed = not task.completed
    task.save()
    return redirect("task-list")

# EDIT
def task_edit(request, pk):
    task = get_object_or_404(Task, id=pk)

    if request.method == "POST":
        task.title = request.POST.get("title")

        # checkbox handling (IMPORTANT)
        task.completed = request.POST.get("completed") == "on"

        task.save()
        return redirect("task-list")

    return render(request, "frontend/task_edit.html", {"task": task})