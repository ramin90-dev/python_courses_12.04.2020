from django.http import HttpResponse
from students.models import Students
from faker import Faker
import random
#from Scripts.students.parser import generate_students
import string



def generate_student(request):
    fake = Faker()
    random_age = random.randint(18, 55) #интервал возвраста студента
    student = Students.objects.create(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        age=random_age,
                                       ) # генерим и записываем значения
    response = f'Random student : <br/> id  first_name last_name age <br/>{student.info()}' # готовим ответ из models.py def info

    return HttpResponse(response)

def student_generate(count: int = 1) -> str:
    fake = Faker()
    result = ''

    for i in range(int(count)):
        student = Students.objects.create(first_name=fake.first_name(), last_name=fake.last_name(),
                                         age=(random.randrange(17, 45, 1)))
        response = f'Random student: {student.info()} <br/>'
        result += response

    return HttpResponse(result)


def generate_students(request):
    count_val = request.GET['count']
    if count_val.isdigit() and 1 <= int(count_val) <= 100:
        return HttpResponse(student_generate(int(request.GET['count'])))
    else:
        return HttpResponse(f'count value {count_val} not in range 1-100')