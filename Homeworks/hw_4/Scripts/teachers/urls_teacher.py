from django.urls import path

from teachers import views

app_name = 'teachers'

urlpatterns = [
    path('list/', views.teacher_all, name='list'),
    path('create/', views.create_teachers, name='create'),
    path('edit/<int:pk>', views.edit_teachers, name='edit'),
    path('delete/<int:pk>', views.delete_teacher, name='delete'),
    path('email/', views.email, name='email'),
]
