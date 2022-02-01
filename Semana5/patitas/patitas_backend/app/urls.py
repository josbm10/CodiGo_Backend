from django.urls import path

from . import views

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('mascotas',views.MascotasView.as_view(),name='mascotas'),
    path('mascotas/<int:mascota_id>',views.MascotasPerfilView.as_view(),name='mascotas_perfil'),
]