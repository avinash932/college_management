"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from main import views as main_views
from student import views as student_views
from faculty import views as faculty_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path("",main_views.index,name="index"),
    path("about",main_views.about,name="about"),
    path("student",student_views.student,name="student"),
    path("add/student",student_views.add_student_view,name="add_student"),
    path("courses_offered",main_views.courses_offered,name="courses"),
    path("events",main_views.cultural_events,name="events"),
    path("placement",main_views.placement_view,name="placement"),
    path("student/delete/<int:student_id>/", student_views.delete_student, name="delete_student"),
    path("student/edit/<int:student_id>/", student_views.edit_student, name="edit_student"),
    path("student/add", student_views.add_student_view, name="add_student"),
    path("student/edit/<str:student_id>", student_views.edit_student, name="edit_student"),
    path("faculty",faculty_views.faculty_view,name="faculty"),
    path("fees",student_views.fee_view,name="fee"),
    path("fee/structure",main_views.fee_structure_view,name="fee_structure"),
    path("login",main_views.login_view,name='login'),
    path("register",main_views.register_view,name='register'),
    path("logout/",main_views.logout_view,name='logout'),
    path("tour",main_views.tour,name="tour"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


