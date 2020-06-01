from Scripts.students import views
from Scripts.teachers import views as t_views

from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', t_views.index, name='Index'),

    path('generate-student/', views.generate_student),
    path('generate-students/', views.generate_students),
    path('teachers/', include('teachers.urls_teacher')),
    path('group/', include('group.urls_group')),
    path('email/', views.email, name='email'),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

urlpatterns += [url(r'^silk/', include('silk.urls', namespace='silk'))]
