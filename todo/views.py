
from django.shortcuts import render
from todo.models import ToDoList


def to_do_view(request):
    return render(request, 'web/to_do.html', {
        'to_do': ToDoList.to_do,
        'created_at': ToDoList.created_at,
        'until_date': ToDoList.until_date,
        'done': ToDoList.done
    })
