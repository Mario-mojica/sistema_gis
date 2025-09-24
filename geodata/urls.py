from django.urls import path
from . import views

urlpatterns = [
    # URL para obtener TODOS los municipios
    # Ejemplo: GET /api/municipios/
    path('municipios/', views.municipios_geojson, name='municipios_geojson'),
    
    # URL para BUSCAR municipios por nombre
    # Ejemplo: GET /api/municipios/buscar/?q=Cuautla
    path('municipios/buscar/', views.buscar_municipios, name='buscar_municipios'),
    
    # URL para obtener los PUNTOS DENTRO de un municipio por su OID
    # Ejemplo: GET /api/municipios/123/puntos/  (donde 123 es el 'oid' del municipio)
    path('municipios/<int:municipio_id>/puntos/', views.puntos_en_municipio, name='puntos_en_municipio'),
   
    path('marginacion/', views.marginacion_geojson, name='marginacion_geojson'),
]