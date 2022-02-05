from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import *

# Create your views here.

class FavoritosView(APIView):
    def get(self,request):
        dataFavorito=Favorito.objects.all()
        serFavorito=FavoritosSerializers(dataFavorito,many=True)
        return Response({'ok':True,
            'content':serFavorito.data})

    def post(self,request):
        serFavorito=FavoritosSerializers(data=request.data)
        serFavorito.is_valid(raise_exception=True)
        serFavorito.save()
        
        return Response({'ok':True,
            'content':serFavorito.data})
        
class ActualizarView(APIView):  
    def put(self, request,favorito_id):
        dataFavorito = Favorito.objects.get(pk=favorito_id)
        serFavorito = FavoritosSerializers(dataFavorito, data=request.data)
        serFavorito.is_valid(raise_exception=True)
        serFavorito.save()
        return Response({'ok':True,
            'content':serFavorito.data})

class DeleteView(APIView): 
    def delete(self,request,favorito_id):
        serFavorito=Favorito.objects.get(pk=favorito_id)
        serFavorito.delete()
        
        return Response({'ok':True,
            'content':'Eliminado'})
        