from django.http import JsonResponse
from .models import Municipios, Puntos, Marginacion
from django.contrib.gis.db.models.functions import MakeValid, AsGeoJSON, Transform
import json

def municipios_geojson(request):
    municipios = Municipios.objects.exclude(the_geom__isnull=True).annotate(
        valid_geom=MakeValid('the_geom'),
        geom_json=AsGeoJSON(Transform('the_geom', 4326))   # reproyectamos
    )

    features = []
    for municipio in municipios:
        if municipio.geom_json:
            feature = {
                "type": "Feature",
                "geometry": json.loads(municipio.geom_json),
                "properties": {
                    "id": municipio.id,
                    "nomgeo": municipio.nomgeo,
                    "cvegeo": municipio.cvegeo,
                    "oid": municipio.oid,
                },
            }
            features.append(feature)

    return JsonResponse({"type": "FeatureCollection", "features": features})


def buscar_municipios(request):
    query = request.GET.get('q', '')

    if query:
        municipios = Municipios.objects.filter(
            nomgeo__icontains=query
        ).annotate(
            valid_geom=MakeValid('the_geom'),
            geom_json=AsGeoJSON(Transform('the_geom', 4326))
        )
    else:
        municipios = Municipios.objects.none()

    features = []
    for municipio in municipios:
        if municipio.geom_json:
            feature = {
                "type": "Feature",
                "geometry": json.loads(municipio.geom_json),
                "properties": {
                    "id": municipio.id,
                    "nomgeo": municipio.nomgeo,
                    "cvegeo": municipio.cvegeo,
                    "oid": municipio.oid,
                },
            }
            features.append(feature)

    return JsonResponse({"type": "FeatureCollection", "features": features})


def puntos_en_municipio(request, municipio_id):
    try:
        municipio = Municipios.objects.get(id=municipio_id)

        puntos = Puntos.objects.filter(
            the_geom__within=municipio.the_geom
        ).annotate(
            valid_geom=MakeValid('the_geom'),
            geom_json=AsGeoJSON(Transform('the_geom', 4326))
        )

        features = []
        for punto in puntos:
            if punto.geom_json:
                feature = {
                    "type": "Feature",
                    "geometry": json.loads(punto.geom_json),
                    "properties": {
                        "id": punto.id,
                        "oid_externo": punto.oid_externo,
                        "id_externo": punto.id_externo,
                    },
                }
                features.append(feature)

        return JsonResponse({"type": "FeatureCollection", "features": features})

    except Municipios.DoesNotExist:
        return JsonResponse({'error': 'Municipio no encontrado'}, status=404)


# geodata/views.py

from django.http import JsonResponse
from .models import Marginacion
from django.contrib.gis.db.models.functions import Transform # <-- 1. IMPORTAMOS TRANSFORM
import json

def marginacion_geojson(request):
    # 2. AÑADIMOS .annotate() PARA TRANSFORMAR LA GEOMETRÍA A SRID 4326
    marginacion = Marginacion.objects.annotate(geom_4326=Transform('the_geom', 4326))

    features = []
    for area in marginacion:
        # Añadimos una comprobación para asegurar que la geometría no sea nula
        if area.geom_4326:
            features.append({
                "type": "Feature",
                # 3. USAMOS LA NUEVA GEOMETRÍA TRANSFORMADA
                "geometry": json.loads(area.geom_4326.geojson),
                "properties": { 
                    "id": area.id, 
                    "colonia": area.colonia,
                    "gm_2020": area.gm_2020 
                },
            })
            
    return JsonResponse({ "type": "FeatureCollection", "features": features })