
from logging import raiseExceptions
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Serie
from .serializers import SerieSerializers
# Create your views here.

class IndexView(APIView):
    def get(self,request):
        context={'mensaje':'Servidor Activo'}
        return Response(context)

class SeriesView(APIView):
    
    def get(self,request):
        dataSerie=Serie.objects.all()
        serSeries=SerieSerializers(dataSerie,many=True)
        return Response(serSeries.data)
    
    def post(self,request):
        serSeries=SerieSerializers(data=request.data)
        serSeries.is_valid(raise_exception=True)
        serSeries.save()
        return Response(serSeries.data)

class SeriesDetailView(APIView):
    
    def get(self,request,serie_id):
        dataSerie=Serie.objects.get(pk=serie_id)
        serSeries=SerieSerializers(dataSerie)
        return Response(serSeries.data)
    def put(self,request,serie_id):
        dataSerie=Serie.objects.get(pk=serie_id)
        serSeries=SerieSerializers(dataSerie,data=request.data)
        serSeries.is_valid(raise_exception=True)
        serSeries.save()
        return Response(serSeries.data)
    def delete(self,request,serie_id):
        dataSerie=Serie.objects.get(pk=serie_id)
        serSeries=SerieSerializers(dataSerie)
        dataSerie.delete()
        return Response(serSeries.data)