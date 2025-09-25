# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.gis.db import models


class Municipios(models.Model):

    id = models.IntegerField(primary_key=True)
    the_geom = models.MultiPolygonField(srid=6372, blank=True, null=True)
    cvegeo = models.CharField(db_column='CVEGEO', max_length=15, blank=True, null=True)  # Field name made lowercase.
    cve_ent = models.CharField(db_column='CVE_ENT', max_length=15, blank=True, null=True)  # Field name made lowercase.
    cve_mun = models.CharField(db_column='CVE_MUN', max_length=15, blank=True, null=True)  # Field name made lowercase.
    nomgeo = models.CharField(db_column='NOMGEO', max_length=80, blank=True, null=True)  # Field name made lowercase.
    oid = models.IntegerField(db_column='OID', blank=True, null=True)  # Field name made lowercase.
    dato = models.FloatField(db_column='DATO', blank=True, null=True)  # Field name made lowercase.
    intervalo = models.CharField(db_column='INTERVALO', max_length=254, blank=True, null=True)  # Field name made lowercase.
    orden = models.FloatField(db_column='ORDEN', blank=True, null=True)  # Field name made lowercase.
    edad = models.CharField(db_column='EDAD', max_length=254, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'municipios'

class Marginacion(models.Model):
    id = models.IntegerField(primary_key=True)
    the_geom = models.MultiPolygonField(srid=6372, blank=True, null=True)
    objectid = models.BigIntegerField(db_column='OBJECTID', blank=True, null=True)  # Field name made lowercase.
    cve_col = models.CharField(db_column='CVE_COL', max_length=12, blank=True, null=True)  # Field name made lowercase.
    id_col = models.IntegerField(db_column='ID_COL', blank=True, null=True)  # Field name made lowercase.
    colonia = models.CharField(db_column='COLONIA', max_length=99, blank=True, null=True)  # Field name made lowercase.
    cp = models.CharField(db_column='CP', max_length=7, blank=True, null=True)  # Field name made lowercase.
    cve_ent = models.CharField(db_column='CVE_ENT', max_length=2, blank=True, null=True)  # Field name made lowercase.
    nom_ent = models.CharField(db_column='NOM_ENT', max_length=31, blank=True, null=True)  # Field name made lowercase.
    mun = models.CharField(db_column='MUN', max_length=3, blank=True, null=True)  # Field name made lowercase.
    cve_mun = models.CharField(db_column='CVE_MUN', max_length=5, blank=True, null=True)  # Field name made lowercase.
    nom_mun = models.CharField(db_column='NOM_MUN', max_length=80, blank=True, null=True)  # Field name made lowercase.
    loc = models.CharField(db_column='LOC', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cve_loc = models.CharField(db_column='CVE_LOC', max_length=9, blank=True, null=True)  # Field name made lowercase.
    nom_loc = models.CharField(db_column='NOM_LOC', max_length=98, blank=True, null=True)  # Field name made lowercase.
    sun_2018 = models.CharField(db_column='SUN_2018', max_length=6, blank=True, null=True)  # Field name made lowercase.
    nom_sun = models.CharField(db_column='NOM_SUN', max_length=35, blank=True, null=True)  # Field name made lowercase.
    pobtot = models.DecimalField(db_column='POBTOT', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.
    p6a14nae = models.DecimalField(db_column='P6A14NAE', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.
    sbasc = models.DecimalField(db_column='SBASC', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.
    psdss = models.DecimalField(db_column='PSDSS', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.
    ovsde = models.DecimalField(db_column='OVSDE', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.
    ovsee = models.DecimalField(db_column='OVSEE', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.
    ovsae = models.DecimalField(db_column='OVSAE', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.
    ovpt = models.DecimalField(db_column='OVPT', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.
    ovhac = models.DecimalField(db_column='OVHAC', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.
    ovsref = models.DecimalField(db_column='OVSREF', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.
    ovsint = models.DecimalField(db_column='OVSINT', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.
    ovscel = models.DecimalField(db_column='OVSCEL', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.
    im_2020 = models.DecimalField(db_column='IM_2020', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.
    gm_2020 = models.CharField(db_column='GM_2020', max_length=9, blank=True, null=True)  # Field name made lowercase.
    imn_2020 = models.DecimalField(db_column='IMN_2020', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.
    clasif = models.CharField(db_column='CLASIF', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'marginacion'


class Ayudantias(models.Model):
    id = models.BigIntegerField(primary_key=True)
    the_geom = models.PointField(srid=6372, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ayudantias'

class Hospitales(models.Model):
    id = models.BigIntegerField(primary_key=True)
    the_geom = models.PointField(srid=6372, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hospitales'


class Semaforos(models.Model):
    id = models.BigIntegerField(primary_key=True)
    the_geom = models.PointField(srid=6372, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'semaforos'


class TiraderoMunicipal(models.Model):
    id = models.BigIntegerField(primary_key=True)
    the_geom = models.MultiPolygonField(srid=6372, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tiradero_municipal'


class Vialidades(models.Model):
    id = models.IntegerField(primary_key=True)
    the_geon = models.MultiLineStringField(srid=6372, blank=True, null=True)
    identifica = models.IntegerField(db_column='IDENTIFICA', blank=True, null=True)  # Field name made lowercase.
    cvevial = models.CharField(db_column='CVEVIAL', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tipovial = models.CharField(db_column='TIPOVIAL', max_length=15, blank=True, null=True)  # Field name made lowercase.
    nomvial = models.CharField(db_column='NOMVIAL', max_length=110, blank=True, null=True)  # Field name made lowercase.
    sentido = models.CharField(db_column='SENTIDO', max_length=15, blank=True, null=True)  # Field name made lowercase.
    dist_mts = models.FloatField(db_column='DIST MTS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    layer = models.CharField(max_length=254, blank=True, null=True)
    path = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vialidades'

class Puntos(models.Model):
    id = models.IntegerField(primary_key=True)
    the_geom = models.MultiPointField(blank=True, null=True)
    id_0 = models.BigIntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase. Field renamed because of name conflict.
    oid = models.IntegerField(db_column='OID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'puntos'
