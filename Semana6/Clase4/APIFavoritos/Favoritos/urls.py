from django.urls import path
from . import views

urlpatterns = [
    path('', views.FavoritosView.as_view(),name='favoritos'),
    path('delete/<int:favorito_id>', views.DeleteView.as_view(),name='delete'),
    path('put/<int:favorito_id>', views.ActualizarView.as_view(),name='actualizar'),
]
