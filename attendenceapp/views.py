from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

# Create your views here.
import random,datetime

# Create your views here.
from attendence.serilizer import *
from attendenceapp.models import *
from django.contrib.auth.models import *
from rest_framework import viewsets
import random
from rest_framework.response import  Response
from django.contrib.auth.models import User



class first_viewsets(viewsets.ModelViewSet):
    queryset = admin1.objects.all()
    serializer_class = first_serializer
    http_method_names = ['get','post','patch']

class teacher_create(viewsets.ViewSet):
    def create(self,request):
        serializers=fifth_serializer(data=request.data)
        if serializers.is_valid():
            #serializers.save()

            print('by===============================================================================================================')
            p=serializers.data['teacher_name']
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++",p)
            p1=serializers.data['teacher_id']
            print("===========================================================================",p1)



            #print('===================================================================',u.username)
            p0=serializers.data['teacher_department']
            a=department.objects.get(id=p0)
            print(a.department_name)
            p3=serializers.data['teacher_collage']
            a1=collage.objects.get(id=p3)



            print('===================================================================',a1.collage_name)
            #print("error here========================================================================================")
           # p4=serializers.data['createdat']
            #print("error here========================================================================================")
            #print('=====================================================================',p4)
            #print("error here========================================================================================")
            #p5=serializers.data['update']
            #print('===========================================================================',p5)
            p6=serializers.data['teacher_email']
            print('=========================================================================',p6)
            p7=serializers.data['teacher_age']
            print('=========================================================================',p7)
            p8=serializers.data['teacher_subject']
            print('=============================================================================',p8)
            p9=serializers.data['created_by']
            a2=admin1.objects.get(id=p9)

            #m= a2.admin_name
            print(p9)
            #print(m,'ppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp')
            #print("===========================================================================",a2.department_name)
            p10=serializers.data['special_status']
            print("==========================================================================",p10)
            l=[]
            h=teacher.objects.all()
            print(h)


            for i in h:
                if(i.teacher_id==None):


                    pass

                else:
                    l.append(i.teacher_id)
                    k=0
            for i in l:

                if a.department_name  and a1.collage_name in i:
                    print(a.department_name,';;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;')
                    print(i,'++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

                    k=i.partition(a.department_name)
                    print(k,'=========================================================================================')
                    o=k[len(k)-1]
                    print(o,'=========================================================ooooooooooooooooooooooooooooooooo')
                    print(o)
                    k=o.partition(p)
                    print(k,'=======================================================kkkkkkkkkkkkkkkkkkkkkkkkkkkk')
                    j=k[len(k)-1]
                    print(j,'=============================================================================================')
                    k=1+1
                    print(k)
                    z=0
                else:
                    pass



            if(k!=0):
                h=a1.collage_name+'20'+a.department_name+p+str(k)
                print(h)
            else:

                h=a1.collage_name+'20'+a.department_name+p+'1'
                print(h)



            print('nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn')
            print(a.department_name)
            r= serializers.data['teacher_password']
            #User.objects.create(username=h,password=r)



            g=teacher.objects.create(teacher_name=p,teacher_id=h
            ,teacher_department=a,
            teacher_collage=a1,teacher_email=p6,
            teacher_age=p7,created_by=a2,special_status=p10,
            teacher_password=r)
            User.objects.create(username=h,password=r)

            #print(p8)
            for i in p8:
                g.teacher_subject.add(i)
                g.save()
            print('ok----------------------------------------------------------')


            print(']]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]')


            return Response("Ok")
        else:
            return Response(serializers.errors)



class login_teacher(viewsets.ViewSet):
    def create(self,request):
        serializers=loginteacher(data=request.data)
        if serializers.is_valid():
            print("==========================================================================================ok",)
            flag=serializers.data['Key']
            print("==========================================================================================ok",)

            flag1=serializers.data['password']
            p=admin1.objects.all()
            try:
                a=teacher.objects.get(teacher_email=flag)
                b=User.objects.get(username=a.teacher_id)


            except:
                try:

                    h=User.objects.get(usernmae=flag)
                except:
                    return Response('Invalid id')
            if h.check_password(flag1) ==True:
                return Response('Login Successfully')
            else:
                return Response('Password not valid ')
        else:
            return Response(serializers.errors)




class admin_create(viewsets.ViewSet):
    def create(self,request):
        print('hi=====================================================================================================')
        serializers=fourth_serializerl(data=request.data)
        print('=by=======================================================================================================')
        if serializers.is_valid():
            print('by===============================================================================================================')
            p=serializers.data['admin_name']
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++",p)
            p1=serializers.data['admin_id']
            print("===========================================================================",p1)
            p2=serializers.data['admin_which_by']
            a=User.objects.get(id=p2)

            print('===================================================================',a.username)
            p3=serializers.data['admin_collage']
            a1=collage.objects.get(id=p3)



            print('===================================================================',a1.collage_name)
            #print("error here========================================================================================")
           # p4=serializers.data['createdat']
            #print("error here========================================================================================")
            #print('=====================================================================',p4)
            #print("error here========================================================================================")
            #p5=serializers.data['update']
            #print('===========================================================================',p5)
            p6=serializers.data['admin_email']
            print('=========================================================================',p6)
            p7=serializers.data['admin_age']
            print('=========================================================================',p7)
            p9=serializers.data['special_status']
            print('=============================================================================',p9)
            p8=serializers.data['admin1_department']
            #a2=department.objects.get(id=p8)
            print(p8)
            #print("===========================================================================",a2.department_name)

            return Response("Ok")
        else:
            return Response(serializers.errors)







class admin_login(viewsets.ViewSet):
    def create(self,request):
        serializers=loginadmin(data=request.data)
        if serializers.is_valid():
            p=serializers.data['Key']
            i=serializers.data['password']
            try:
                a=admin1.objects.get(admin1_email=p)

            except:
                try:


                    a=admin1.objects.get(admin1_id=p)
                except:
                    return Response('Invalid admin')
            if a.check_password(i) ==True:
                return Response('Login Successfully')
            else:
                return Response('Password not valid ')
        else:
            return Response(serializers.errors)


class login(viewsets.ViewSet):
    def create(self,request):
        serializer=loginserial(data=request.data)
        if serializer.is_valid():
            flg=serializer.data['Key']
            password=serializer.data['password']
            try:
                usr=User.objects.get(username=flg)
            except:
                try:
                    usr=User.objects.get(email=flg)
                except:
                    return Response('invalid user')

            if usr.check_password(password) ==True:
                return Response('Login Successfully')
            else:
                return Response('Password not valid ')

        else:
            return Response(serializer.errors)







class subject(viewsets.ViewSet):
    def create(self,request):
        serializers=sixth_serializerl(data=request.data)
        if(serializers.is_valid()):
            subject_name=serializers.data['sunbject_name']
            print(subject_name)
            sunbject_collage=serializers.data['sunbject_collage']
           # a=collage.objects.get(id=sunbject_collage)
            print(sunbject_collage)
            #print(a.collage_name)
            sunbject_department=serializers.data['sunbject_department']
            #b=department.objects.get(id=sunbject_department)
            #print(b.department_name)
            print(sunbject_department)
            try:


                subject_unique_id=serializers.data['subject_unique_id']
                print(subject_unique_id)
                return Response('id not provide')
            except:
                return Response('id provide')
            return Response('ok')


        else:
           return Response(serializers.errors)



class Hod_create(viewsets.ViewSet):
    def create(self,request):
        l=[]
        p=hod.objects.all()
        print(p)
        for i in p:
            if(i.hod_id==None):
                n=0
            else:

                l.append(i.hod_id)
                print(l,'=======================================================================================321')
        print(l)
        serializer=third_serializer1(data=request.data)
        if serializer.is_valid():
            print('================================================235')
            serializer.save()


            #serializer=first_serializer(data=request.data)
            print("========================1111111111===========================")
            p1=serializer.data['hod_name']
            a2=serializer.data['hod_email']
            a3=serializer.data['hod_age']
            a4=serializer.data['hod_which_by']
            a5=serializer.data['hod_department']
            p2=department.objects.get(id=a5)
            z=department.objects.get(id=p2)
            a6=serializer.data['hod_collage']
            p3=collage.objects.get(id=a6)
            a7=serializer.data['created_by']
            z7=admin1.objects.get(id=a7)
            a8=serializer.data['hod_subject']
            print("ho++++++++++==========================================================================================")

            print(p1)
            print("=========================234 name",p1)
            g=User.objects.get(id=a4)
            print(g)


            print(p2,'collage===========================================================')
            print(p2.collage_unique_id,'========================================================')

            #print('=================================fsdcads=')



            z1='pce'+'18'+'hod'+p1

            for i in l:
                print(p1,'===========================================================================')
                lo=str(p1)
                print(type(p1),'==========')
                print(type(lo))


                if p1 in i:

                    z=i.partition(p1)
                    k=z[len(z)-1]
                else:
                    k=0
            k=0

            if(k):
                print('hi')
                n=int(k)+1
                g=z1+str(n)
                print('lllllllllllllllllllll')
                print(g,'++++++++++++++++++++++++++++')
                #serializer.save(hod_id=g)
                print('ok')

                x1=hod.objects.create(username=z1,hod_email=a2,hod_age=a2 , hod_which_by= g.username , hod_department= z.department_name , hod_collage= p3.collage_name ,created_by=z7.admin_name ,hod_subject= a8 )
                x1.save()



            else:
                z1=z1+'01'
                print('ppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp')
                print(z1,'========================================================================')


               # serializer.save(hod_id=z1)
                x1=hod.objects.create(username=z1,hod_email=a2,hod_age=a2 , hod_which_by= g.username , hod_department= z.department_name , hod_collage= p3.collage_name ,created_by=z7.admin_name ,hod_subject= a8 )
                x1.save()
            return Response('ok')
        else:
            return Response(serializer.errors)



class login_hod(viewsets.ViewSet):
    def create(self,request):
        serializers=loginhod
        if serializers.is_valid():
            flag=serializers.data['key']
            flag1=serializers.data['password']
            p=admin1.objects.all()
            try:
                a=teacher.objects.get(hod_email=flag)

            except:
                try:

                    a=teacher.objects.get(hod_id=flag)
                except:
                    return Response('Invalid id')
            if a.check_password(flag1) ==True:
                return Response('Login Successfully')
            else:
                return Response('Password not valid ')
        else:
            return Response(serializers.errors)




class total_department(viewsets.ViewSet):
    def get(self,request):
        serializers=total_department
        if serializers.is_valid():

            o=input('enter the collage name or id')
            l=[]
            p=0
            try:
                g=collage.objects.get(collage_name=o)

                print(g)
                l.append(g.department_nmaes)
                for i in l:
                    p=p+1
                l.append('Total no of departments : ')
                l.append(p)

                return Response(l)
            except:
                return Response('No collage exist')
        else:
            return Response(serializers.errors)



class collage_create(viewsets.ViewSet):
    def create(self,request):
        serializers=seventh_serializerl(data=request.data)
        if serializers.is_valid():
            serializers.save()
            p=serializers.data['collage_name']
            print(p)
            p1=serializers.data['collage_unique_id']
            print(p1)

            p2=serializers.data['collage_reg']
            print(p2)
            p3=serializers.data['collage_address']
            print(p3)
            p4=serializers.data['department_nmaes']
            print(p4)

            return Response('ok')

        else:
            return Response(serializers.errors)



class department_create(viewsets.ViewSet):
    def create_create(self,request):
        serializers=eight_serializerl(data=request.data)
        if serializers.is_valid():
            serializers.save()
            p=serializers.data['department_name']
            print(p)
            p1=serializers.data['department_unique_id']
            print(p1)
            return Response("OK")
        else:
            return Response(serializers.errors)


















