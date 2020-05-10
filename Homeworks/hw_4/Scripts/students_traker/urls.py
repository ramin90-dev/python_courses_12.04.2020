from Scripts.students import views
from Scripts.teachers import views as t_views

from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('generate-student/', views.generate_student),
    path('generate-students/', views.generate_students),
    path('generate-teachers/', t_views.generate_teachers),

]
