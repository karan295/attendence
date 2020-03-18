from django.urls import path
from .import views

from attendenceapp.views import *
from rest_framework import routers
from rest_framework.routers import DefaultRouter
router=DefaultRouter()

router.register(r'login',login,basename='p')
router.register(r'teacher_create',teacher_create,basename='teacher')
router.register(r'login_teacher',login_teacher,basename='login_teacher')
router.register(r'create_admin',admin_create,basename='create_admin')
router.register(r'login_admin',admin_login,basename='login_admin')
router.register(r'subject',subject,basename='subject')
router.register(r'login_hod',login_hod,basename='login_hod')
router.register(r'Hod_create',Hod_create,basename='Hod_create')
router.register(r'admin_create',admin_create,basename='admin_create')
router.register(r'teacher_create',teacher_create,basename='teacher_create')
router.register(r'total departments',total_department,basename='td')
router.register(r'collage_create',collage_create,basename='collage_create')
router.register(r'department_create',department_create,basename=department_create)

urlpatterns = router.urls
print('hi')
