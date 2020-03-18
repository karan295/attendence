#from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class department(models.Model):
    department_name=models.CharField(max_length=100,unique=True)
    createdat=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now_add=True)
    department_unique_id=models.CharField(max_length=100,unique=True,null=True,blank=True)

class collage(models.Model):
    collage_name=models.CharField(max_length=100,unique=True)
    collage_unique_id=models.CharField(max_length=100,null=True,blank=True)
    collage_reg=models.CharField(max_length=100,unique=True)
    collage_address=models.CharField(max_length=100,unique=True)
    createdat=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    update=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    department_nmaes=models.ManyToManyField(department)

    def __str__(self):
        return self.collage_name



class sunbject(models.Model):
    sunbject_name=models.CharField(max_length=100,unique=True)
    sunbject_collage=models.ManyToManyField(collage)
    sunbject_department=models.ManyToManyField(department)
    subject_unique_id=models.CharField(max_length=100,null=True,blank=True)


class admin1(models.Model):
    admin_name=models.CharField(max_length=100)
    admin_id=models.CharField(max_length=100,null=True,blank=True)
    admin_collage=models.ForeignKey(collage,on_delete=models.CASCADE)
    createdat=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now_add=True)
    admin_email=models.EmailField()
    admin_age=models.IntegerField()
    special_status=models.BooleanField(null=True,blank=True)
    admin1_department=models.ManyToManyField(department)


class teacher(models.Model):
    teacher_name=models.CharField(max_length=100)
    teacher_id=models.CharField(max_length=100,null=True,blank=True)
    teacher_department=models.ForeignKey(department,on_delete=models.CASCADE)
    teacher_collage=models.ForeignKey(collage,on_delete=models.CASCADE)
    createdat=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now_add=True)
    teacher_email=models.EmailField(unique=True)
    teacher_age=models.IntegerField()
    teacher_subject=models.ManyToManyField(sunbject)
    created_by=models.ForeignKey(admin1,on_delete=models.CASCADE)
    special_status=models.BooleanField(null=True,blank=True)
    teacher_password=models.CharField(max_length=10,null=True,blank=True)



class hod(models.Model):
    hod_name=models.CharField(max_length=100)
    hod_department=models.OneToOneField(department,on_delete=models.CASCADE,unique=True  )
    hod_collage=models.ForeignKey(collage,on_delete=models.CASCADE)
    createdat=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now_add=True)
    hod_email=models.EmailField(unique=True)
    hod_id=models.CharField(max_length=100,null=True,blank=True)
    hod_age=models.IntegerField()
    hod_subject=models.ManyToManyField(sunbject)
    special_status=models.BooleanField(null=True,blank=True)
    created_by=models.ForeignKey(admin1,on_delete=models.CASCADE)
class attdence(models.Model):
    month=models.CharField(max_length=100)
    paid_leave=models.IntegerField()
    workingdays=models.IntegerField()
    count=models.IntegerField()
    teacher=models.ForeignKey(teacher,on_delete=models.CASCADE)
    createdat=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now_add=True)
    special_status=models.BooleanField(null=True,blank=True)


class batch(models.Model):
    batch_name=models.CharField(max_length=100)
    batch_collage=models.ForeignKey(collage,on_delete=models.CASCADE)
    batch_department=models.OneToOneField(department,on_delete=models.CASCADE)
    batch_id=models.CharField(max_length=100)
    batch_tutor=models.OneToOneField(teacher,on_delete=models.CASCADE)
    batch_total_student=models.IntegerField()
    batch_year=models.IntegerField()
    batch_sem=models.IntegerField()
    batch_createdat=models.CharField(max_length=100)

class student(models.Model):
    student_name=models.CharField(max_length=100)
    student_collage=models.ForeignKey(collage,on_delete=models.CASCADE)
    student_department=models.ForeignKey(department,on_delete=models.CASCADE)
    student_which_by=models.ForeignKey(User,on_delete=models.CASCADE)
    createdat=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now_add=True)
    student_email=models.EmailField(unique=True)
    student_id=models.CharField(max_length=100,null=True,blank=True)
    student_age=models.IntegerField()
    special_status=models.BooleanField(null=True,blank=True)
    created_by=models.ForeignKey(admin1,on_delete=models.CASCADE)
    student_class=models.ForeignKey(batch,on_delete=models.CASCADE)
    student_rol_no=models.CharField(max_length=100)

