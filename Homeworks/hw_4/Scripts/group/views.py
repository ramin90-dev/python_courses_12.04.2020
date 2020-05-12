from django.http import HttpResponse, HttpResponseRedirect # noqa imported unused
from django.shortcuts import render


def create_groups(request):
    from group.forms import GroupCreateForm

    if request.method == 'POST':
        form = GroupCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    elif request.method == 'GET':
        form = GroupCreateForm()

    context = {'create_form': form}
    return render(request, "create_groups.html", context=context)
