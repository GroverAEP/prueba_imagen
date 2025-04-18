# urls.py de la app o del proyecto
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_productos, name='lista_productos'),
    path('addImages', views.cargar_productos_desde_static, name="addImages"),
 path('eliminar-imagenes/', views.eliminar_imagenes, name='eliminar_imagenes'),

]
