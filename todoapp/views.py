from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import TodoListItem

def todoappView(request):
    """View that sends all todo list items."""
    all_todo_items = TodoListItem.objects.all()
    return render(
        request, 
        'todolist.html', 
        {'all_items': all_todo_items}
    )


def addTodoView(request):
    """Action for creating a new todo item."""
    x = request.POST['content']
    new_item = TodoListItem(content=x)
    new_item.save()
    return HttpResponseRedirect('/todoapp/')


def deleteTodoView(request, i):
    """Action for deleting a todo item."""
    item = TodoListItem.objects.get(id=i)
    item.delete()
    return HttpResponseRedirect('/todoapp/')
