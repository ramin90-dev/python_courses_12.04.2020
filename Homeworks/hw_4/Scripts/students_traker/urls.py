from Scripts.group import views as g_views
from Scripts.students import views
from Scripts.teachers import views as t_views


from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', t_views.index),

    path('generate-student/', views.generate_student),
    path('generate-students/', views.generate_students),
    path('generate-teachers/', t_views.generate_teachers),

    path('create-teachers/', t_views.create_teachers),

    path('create-groups/', g_views.create_groups),

]
