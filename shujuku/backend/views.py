from django.shortcuts              import       render
from django.http                   import       JsonResponse
from django.views.generic          import       View
from django_filters                import       rest_framework
from django.contrib.auth.hashers   import       hashlib
from django_filters.rest_framework import       DjangoFilterBackend
#----------------------------------------------------------------------------------------
from rest_framework                import       filters
from rest_framework.views          import       APIView
from rest_framework.response       import       Response
from rest_framework.decorators     import       api_view
from rest_framework                import       permissions,viewsets,renderers,generics,status,exceptions
#-----------------------------------------------------------------------------------------
import random
#导入序列化器
from .serializers import ServiceSerializer,UserSerializer,HealthSerializer,WaterSerializer,NoticeSerializer, ChangePasswordSerializer


#导入模型
from .models import Service,User,Health,Water,Notice

#导入过权限组



class  UserViewSet(viewsets.ModelViewSet):
    queryset           =  User.objects.all()
    serializer_class   =  UserSerializer
    filter_backends    =   (DjangoFilterBackend,)   
    filter_fields      =   ('uno',)
class ServiceViewSet(viewsets.ModelViewSet):
    queryset           = Service.objects.all()
    serializer_class   = ServiceSerializer

class HealthViewSet(viewsets.ModelViewSet):
    queryset           =   Health.objects.all()
    serializer_class   =   HealthSerializer
    filter_backends    =   (DjangoFilterBackend,)   
    filter_fields      =   ('dlou_id','dno_id',)
class WaterViewSet(viewsets.ModelViewSet):
    queryset           =  Water.objects.all()
    serializer_class   = WaterSerializer
    filter_backends    =   (DjangoFilterBackend,filters.)   
    filter_fields      =   ('dlou_id','dno_id',)

class NoticeViewSet(viewsets.ModelViewSet):
    queryset           =  Notice.objects.all()
    serializer_class   =  NoticeSerializer
    ordering_fields    =   ('-n_time',)


class UserAPIView(APIView):
    #---------------登录成功时为用户设置Token,返回并保存---------------
    queryset          =   User.objects.all()
    serializer_class  =   UserSerializer

    #重载GET方法
    def get(self,request,format=None):
        serializer    =   UserSerializer()
        return Response(serializer.data)

    #重载POST方法
    def post(self,request,format=None):
        data          =   request.data
        user          =   None
        try:
            flag = data.get('flag')
            user = User.objects.get(uno=data.get('uno'))
            password = data.get('password')
            # for i in range(2):
            #     password = hashlib.md5(password.encode('utf-8') + user.salt.encode('utf-8')).hexdigest()
            if (password  == user.password and flag ==  user.flag):
                random_list = 'abdjcniejknmdkjdj'
                ch = ''
                for i in range(10):
                    ch += (list(random_list)[random.randint(0,16)])
            
                flag = user.flag
                context = {'msg':'Succeeded','flag':flag}
                return JsonResponse(context)
        except:
            return Response({'msg':'ERROR Incorrect username or password'},status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordAPIView(APIView):
    #---------------An endpoint for changing password.-------------
    queryset          =   User.objects.all()
    serializer_class  =   ChangePasswordSerializer

 

    #重载GET方法
    def get(self,request,format=None):
        serializer    =  ChangePasswordSerializer()
        return Response(serializer.data)

    #重载POST方法
    def post(self,request,*args,**kwargs):
        data          =   request.data
        user          =   None
        try:
            
            user = User.objects.get(uno=data.get('uno'))
            password = data.get('password')
            password1 = data.get('password1')
            if (password  == user.password):
                user.password  = password1
                user.save()
                context = {'msg':'Succeeded',}
                return JsonResponse(context)
        except:
            return Response({'msg':'ERROR Incorrect username or password'},status=status.HTTP_400_BAD_REQUEST)