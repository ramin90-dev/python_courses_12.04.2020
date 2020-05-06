from django.contrib import admin
from django.urls import path



from students import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('generate-student/', views.generate_student),
    path('generate-students/', views.generate_students),

]
