from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from teachers.forms import TeachersCreateForm
from teachers.models import teachers


def teacher_all(request):
    params = [
        'tech_name',
        'tech_surn',
        'tech_gend',
        'tech_city',
        'tech_age',
        'tech_date',

    ]
    teachers_queryset = teachers.objects.all()
    for param in params:
        value = request.GET.get(param)
        if value:
            teachers_queryset = teachers_queryset.filter(**{param: value})
    count = teachers_queryset.count()
    return render(request, 'teachers-list.html', context={'teachers': teachers_queryset, 'count': count})


def index(request):
    return render(request, "index.html", context={})


def create_teachers(request):
    if request.method == 'POST':
        form = TeachersCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(reverse('teachers:list'))
    elif request.method == 'GET':
        form = TeachersCreateForm()

    context = {'create_form': form}
    return render(request, "create_teachers.html", context=context)


def edit_teachers(request, pk):
    teacher = get_object_or_404(teachers, id=pk)

    if request.method == 'POST':
        form = TeachersCreateForm(request.POST, instance=teacher)

        if form.is_valid():
            form.save()
            return redirect(reverse('teachers:list'))
    elif request.method == 'GET':
        form = TeachersCreateForm(instance=teacher)

    context = {'edit_form': form,
               'teacher': teacher,
               }
    return render(request, "edit_teachers.html", context=context)


def delete_teacher(request, pk):
    teacher = get_object_or_404(teachers, id=pk)
    teacher.delete()
    return redirect(reverse('teachers:list'))
