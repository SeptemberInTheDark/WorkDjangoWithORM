from django.shortcuts import render
from .models import Student


# Create your views here.
def students_list(request):
    template = 'school/students_list.html'
    ordering = 'group'
    
    students = Student.objects.all().order_by(ordering, 'name')
    context = {
        'object_list': students,
    }
    return render(request, template, context)