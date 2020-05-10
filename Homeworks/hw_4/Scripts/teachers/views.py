from django.http import HttpResponse

from teachers.models import teachers


def generate_teachers(request):
    tech_age = request.GET.get('tech_age')
    tech_name = request.GET.get('tech_name')
    last_name = request.GET.get('tech_surn')

    teachers_filter = teachers.objects.all()
    if tech_age:
        teachers_filter = teachers_filter.filter(tech_age=tech_age)
    if tech_name:
        teachers_filter = teachers_filter.filter(tech_name=tech_name)
    if last_name:
        teachers_filter = teachers_filter.filter(last_name=last_name)
    response = f'teachers: {teachers_filter.count()}<br/>'
    for teacher in teachers_filter:
        response += teacher.full_info() + '<br/>'
    return HttpResponse(response)
