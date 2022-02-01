
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import *

# Create your views here.

class IndexView(APIView):
    def get(self, request):
        context={
            'ok':True,
            'message':'El servidor funciona'
                }
        return Response(context)
        
class MascotasView(APIView):
    def get(self, request):
        dataMascota=Mascotas.objects.all()
        serMascota=MascotasSerializer(dataMascota,many=True)
        return Response({'ok':True,
            'content':serMascota.data})
        
class MascotasPerfilView(APIView):
    def get(self, request,mascota_id):
        dataMascota=Mascotas.objects.get(pk=mascota_id)
        serMascota=MascotasSerializer(dataMascota)
        context={'ok':True,
            'content':serMascota.data}
        return Response(context)