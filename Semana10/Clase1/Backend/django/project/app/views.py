
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from django.contrib.auth.models import User


from .serializer import *
# Create your views here.

# import serialser jwt
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
class indexView(APIView):
    def get(self,request):
        context={
            'status':True,
            'content':'api activo'
        }
        return Response(context)
 ############# endpoint jwt ###########################  
  
class UsuarioLoginView(TokenObtainPairView):
  
    permission_classes = (AllowAny,)
    serializer_class = UsuarioLoginSerializer

############# user ###########################
class UsuarioView(APIView):
    def get(self,request):
        usuarioData=User.objects.all()
        usuarioSer=UsuarioSerializer(usuarioData,many=True)
        context={
            'status':True,
            'content':usuarioSer.data
        }
        return Response(context)
    
    def post(self,request):
        usuarioSer=UsuarioSerializer(data=request.data)
        usuarioSer.is_valid(raise_exception=True)
        usuarioSer.save()
        context={
            'status':True,
            'content':usuarioSer.data
        }
        return Response(context)

############# cliente ##############################
class ClienteRegistroView(APIView):
    def post(self,request):
        clienteSer=ClienteRegistroSerializer(data=request.data)
        clienteSer.is_valid(raise_exception=True)
        clienteSer.save()
        context={
            'status':True,
            'content':clienteSer.data
        }
        return Response(context)
    
##### serielaizer para simple jwt ########

