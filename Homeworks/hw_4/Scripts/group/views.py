from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from group.forms import GroupCreateForm
from group.models import Group


def group_all(request):
    groups = Group.objects.all()
    count = groups.count()
    return render(request, 'group-list.html', context={'groups': groups,
                                                       'count': count
                                                       }
                  )


def index(request):
    return render(request, "index.html", context={})


def create_group(request):
    if request.method == 'POST':
        form = GroupCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(reverse('group:list'))
    elif request.method == 'GET':
        form = GroupCreateForm()

    context = {'create_form': form}
    return render(request, "create_groups_temp.html", context=context)


def edit_group(request, pk):
    group = get_object_or_404(Group, id=pk)

    if request.method == 'POST':
        form = GroupCreateForm(request.POST, instance=group)

        if form.is_valid():
            form.save()
            return redirect(reverse('group:list'))
    elif request.method == 'GET':
        form = GroupCreateForm(instance=group)

    context = {'edit_form': form,
               'group': group,
               }
    return render(request, "edit_group.html", context=context)


def delete_group(request, pk):
    group = get_object_or_404(Group, id=pk)
    group.delete()
    return redirect(reverse('group:list'))
