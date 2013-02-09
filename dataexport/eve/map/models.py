from django.db import models

class CelestialStatistic(models.Model):
    celestial           = models.ForeignKey("map.Denormalize", primary_key=True, db_column='celestialID') # Field name made lowercase.
    temperature         = models.FloatField(null=True, blank=True)
    spectralclass       = models.CharField(max_length=30, db_column='spectralClass', blank=True) # Field name made lowercase.
    luminosity          = models.FloatField(null=True, blank=True)
    age                 = models.FloatField(null=True, blank=True)
    life                = models.FloatField(null=True, blank=True)
    orbitradius         = models.FloatField(null=True, db_column='orbitRadius', blank=True) # Field name made lowercase.
    eccentricity        = models.FloatField(null=True, blank=True)
    massdust            = models.FloatField(null=True, db_column='massDust', blank=True) # Field name made lowercase.
    massgas             = models.FloatField(null=True, db_column='massGas', blank=True) # Field name made lowercase.
    fragmented          = models.IntegerField(null=True, blank=True)
    density             = models.FloatField(null=True, blank=True)
    surfacegravity      = models.FloatField(null=True, db_column='surfaceGravity', blank=True) # Field name made lowercase.
    escapevelocity      = models.FloatField(null=True, db_column='escapeVelocity', blank=True) # Field name made lowercase.
    orbitperiod         = models.FloatField(null=True, db_column='orbitPeriod', blank=True) # Field name made lowercase.
    rotationrate        = models.FloatField(null=True, db_column='rotationRate', blank=True) # Field name made lowercase.
    locked              = models.IntegerField(null=True, blank=True)
    pressure            = models.FloatField(null=True, blank=True)
    radius              = models.FloatField(null=True, blank=True)
    mass                = models.FloatField(null=True, blank=True)
    class Meta:
        db_table        = u'mapCelestialStatistics'

class ConstellationJump(models.Model):
    fromregion          = models.ForeignKey("map.Region", null=True, db_column='fromRegionID', blank=True, related_name='+') # Field name made lowercase.
    fromconstellation   = models.ForeignKey("map.Constellation", primary_key=True, db_column='fromConstellationID', related_name='jumps') # Field name made lowercase.
    toconstellation     = models.ForeignKey("map.Constellation", primary_key=True, db_column='toConstellationID', related_name='+') # Field name made lowercase.
    toregion            = models.ForeignKey("map.Region", null=True, db_column='toRegionID', blank=True, related_name='+') # Field name made lowercase.
    class Meta:
        db_table        = u'mapConstellationJumps'

class Constellation(models.Model):
    regionid            = models.ForeignKey("map.Region", null=True, db_column='regionID', blank=True) # Field name made lowercase.
    id                  = models.IntegerField(primary_key=True, db_column='constellationID') # Field name made lowercase.
    name                = models.CharField(max_length=300, db_column='constellationName', blank=True) # Field name made lowercase.
    x                   = models.FloatField(null=True, blank=True)
    y                   = models.FloatField(null=True, blank=True)
    z                   = models.FloatField(null=True, blank=True)
    xmin                = models.FloatField(null=True, db_column='xMin', blank=True) # Field name made lowercase.
    xmax                = models.FloatField(null=True, db_column='xMax', blank=True) # Field name made lowercase.
    ymin                = models.FloatField(null=True, db_column='yMin', blank=True) # Field name made lowercase.
    ymax                = models.FloatField(null=True, db_column='yMax', blank=True) # Field name made lowercase.
    zmin                = models.FloatField(null=True, db_column='zMin', blank=True) # Field name made lowercase.
    zmax                = models.FloatField(null=True, db_column='zMax', blank=True) # Field name made lowercase.
    faction             = models.ForeignKey("chr.Faction", null=True, db_column='factionID', blank=True) # Field name made lowercase.
    radius              = models.FloatField(null=True, blank=True)
    class Meta:
        db_table        = u'mapConstellations'

class Denormalize(models.Model):
    id                  = models.IntegerField(primary_key=True, db_column='itemID') # Field name made lowercase.
    type                = models.ForeignKey("inv.Type", null=True, db_column='typeID', blank=True) # Field name made lowercase.
    group               = models.ForeignKey("inv.Group", null=True, db_column='groupID', blank=True) # Field name made lowercase.
    solarsystem         = models.ForeignKey("map.SolarSystem", null=True, db_column='solarSystemID', blank=True) # Field name made lowercase.
    constellation       = models.ForeignKey("map.Constellation", null=True, db_column='constellationID', blank=True) # Field name made lowercase.
    region              = models.ForeignKey("map.Region", null=True, db_column='regionID', blank=True) # Field name made lowercase.
    orbit               = models.ForeignKey("self", null=True, db_column='orbitID', blank=True) # Field name made lowercase.
    x                   = models.FloatField(null=True, blank=True)
    y                   = models.FloatField(null=True, blank=True)
    z                   = models.FloatField(null=True, blank=True)
    radius              = models.FloatField(null=True, blank=True)
    itemname            = models.CharField(max_length=300, db_column='itemName', blank=True) # Field name made lowercase.
    security            = models.FloatField(null=True, blank=True)
    celestialindex      = models.IntegerField(null=True, db_column='celestialIndex', blank=True) # Field name made lowercase.
    orbitindex          = models.IntegerField(null=True, db_column='orbitIndex', blank=True) # Field name made lowercase.
    class Meta:
        db_table        = u'mapDenormalize'

class Jump(models.Model):
    stargate            = models.ForeignKey("map.Denormalize", primary_key=True, db_column='stargateID', related_name='+') # Field name made lowercase.
    celestial           = models.ForeignKey("map.Denormalize", null=True, db_column='celestialID', blank=True, related_name='+') # Field name made lowercase.
    class Meta:
        db_table        = u'mapJumps'

class Landmark(models.Model):
    id                  = models.IntegerField(primary_key=True, db_column='landmarkID') # Field name made lowercase.
    name                = models.CharField(max_length=300, db_column='landmarkName', blank=True) # Field name made lowercase.
    description         = models.CharField(max_length=21000, blank=True)
    location            = models.ForeignKey("map.SolarSystem", null=True, db_column='locationID', blank=True) # Field name made lowercase.
    x                   = models.FloatField(null=True, blank=True)
    y                   = models.FloatField(null=True, blank=True)
    z                   = models.FloatField(null=True, blank=True)
    radius              = models.FloatField(null=True, blank=True)
    icon                = models.ForeignKey("eve.Icon", null=True, db_column='iconID', blank=True)
    importance          = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table        = u'mapLandmarks'

class LocationScene(models.Model):
    location            = models.ForeignKey("map.Denormalize", primary_key=True, db_column='locationID') # Field name made lowercase.
    graphic             = models.ForeignKey("eve.Graphic", null=True, db_column='graphicID', blank=True)
    class Meta:
        db_table        = u'mapLocationScenes'

class LocationWormholeClass(models.Model):
    location            = models.ForeignKey("map.Denormalize", primary_key=True, db_column='locationID') # Field name made lowercase.
    wormholeclass       = models.IntegerField(null=True, db_column='wormholeClassID', blank=True) # Field name made lowercase.
    class Meta:
        db_table        = u'mapLocationWormholeClasses'

class RegionJump(models.Model):
    fromregion          = models.ForeignKey("map.Region", primary_key=True, db_column='fromRegionID', related_name='jumps') # Field name made lowercase.
    toregion            = models.ForeignKey("map.Region", primary_key=True, db_column='toRegionID', related_name='+') # Field name made lowercase.
    class Meta:
        db_table        = u'mapRegionJumps'

class Region(models.Model):
    id                  = models.IntegerField(primary_key=True, db_column='regionID') # Field name made lowercase.
    name                = models.CharField(max_length=300, db_column='regionName', blank=True) # Field name made lowercase.
    x                   = models.FloatField(null=True, blank=True)
    y                   = models.FloatField(null=True, blank=True)
    z                   = models.FloatField(null=True, blank=True)
    xmin                = models.FloatField(null=True, db_column='xMin', blank=True) # Field name made lowercase.
    xmax                = models.FloatField(null=True, db_column='xMax', blank=True) # Field name made lowercase.
    ymin                = models.FloatField(null=True, db_column='yMin', blank=True) # Field name made lowercase.
    ymax                = models.FloatField(null=True, db_column='yMax', blank=True) # Field name made lowercase.
    zmin                = models.FloatField(null=True, db_column='zMin', blank=True) # Field name made lowercase.
    zmax                = models.FloatField(null=True, db_column='zMax', blank=True) # Field name made lowercase.
    faction             = models.ForeignKey("chr.Faction", null=True, db_column='factionID', blank=True) # Field name made lowercase.
    radius              = models.FloatField(null=True, blank=True)
    class Meta:
        db_table        = u'mapRegions'

class SolarsystemJump(models.Model):
    fromregion          = models.ForeignKey("map.Region", null=True, db_column='fromRegionID', blank=True, related_name='+') # Field name made lowercase.
    fromconstellation   = models.ForeignKey("map.Constellation", null=True, db_column='fromConstellationID', blank=True, related_name='+') # Field name made lowercase.
    fromsolarsystem     = models.ForeignKey("map.SolarSystem", primary_key=True, db_column='fromSolarSystemID', related_name='jumps') # Field name made lowercase.
    tosolarsystem       = models.ForeignKey("map.SolarSystem", primary_key=True, db_column='toSolarSystemID', related_name='+') # Field name made lowercase.
    toconstellation     = models.ForeignKey("map.Constellation", null=True, db_column='toConstellationID', blank=True, related_name='+') # Field name made lowercase.
    toregion            = models.ForeignKey("map.Region", null=True, db_column='toRegionID', blank=True, related_name='+') # Field name made lowercase.
    class Meta:
        db_table        = u'mapSolarSystemJumps'

class SolarSystem(models.Model):
    regionid            = models.ForeignKey("map.Region", null=True, db_column='regionID', blank=True) # Field name made lowercase.
    constellation       = models.ForeignKey("map.Constellation", null=True, db_column='constellationID', blank=True) # Field name made lowercase.
    id                  = models.IntegerField(primary_key=True, db_column='solarSystemID') # Field name made lowercase.
    name                = models.CharField(max_length=300, db_column='solarSystemName', blank=True) # Field name made lowercase.
    x                   = models.FloatField(null=True, blank=True)
    y                   = models.FloatField(null=True, blank=True)
    z                   = models.FloatField(null=True, blank=True)
    xmin                = models.FloatField(null=True, db_column='xMin', blank=True) # Field name made lowercase.
    xmax                = models.FloatField(null=True, db_column='xMax', blank=True) # Field name made lowercase.
    ymin                = models.FloatField(null=True, db_column='yMin', blank=True) # Field name made lowercase.
    ymax                = models.FloatField(null=True, db_column='yMax', blank=True) # Field name made lowercase.
    zmin                = models.FloatField(null=True, db_column='zMin', blank=True) # Field name made lowercase.
    zmax                = models.FloatField(null=True, db_column='zMax', blank=True) # Field name made lowercase.
    luminosity          = models.FloatField(null=True, blank=True)
    border              = models.NullBooleanField(null=True, blank=True)
    fringe              = models.NullBooleanField(null=True, blank=True)
    corridor            = models.NullBooleanField(null=True, blank=True)
    hub                 = models.NullBooleanField(null=True, blank=True)
    international       = models.NullBooleanField(null=True, blank=True)
    regional            = models.NullBooleanField(null=True, blank=True)
    constellation       = models.NullBooleanField(null=True, blank=True)
    security            = models.FloatField(null=True, blank=True)
    faction             = models.ForeignKey("chr.Faction", null=True, db_column='factionID', blank=True, related_name='owned_solarsystems') # Field name made lowercase.
    radius              = models.FloatField(null=True, blank=True)
    suntype             = models.ForeignKey("inv.Type", null=True, db_column='sunTypeID', blank=True) # Field name made lowercase.
    securityclass       = models.CharField(max_length=6, db_column='securityClass', blank=True) # Field name made lowercase.
    class Meta:
        db_table        = u'mapSolarSystems'

class Universe(models.Model):
    id                  = models.IntegerField(primary_key=True, db_column='universeID') # Field name made lowercase.
    name                = models.CharField(max_length=300, db_column='universeName', blank=True) # Field name made lowercase.
    x                   = models.FloatField(null=True, blank=True)
    y                   = models.FloatField(null=True, blank=True)
    z                   = models.FloatField(null=True, blank=True)
    xmin                = models.FloatField(null=True, db_column='xMin', blank=True) # Field name made lowercase.
    xmax                = models.FloatField(null=True, db_column='xMax', blank=True) # Field name made lowercase.
    ymin                = models.FloatField(null=True, db_column='yMin', blank=True) # Field name made lowercase.
    ymax                = models.FloatField(null=True, db_column='yMax', blank=True) # Field name made lowercase.
    zmin                = models.FloatField(null=True, db_column='zMin', blank=True) # Field name made lowercase.
    zmax                = models.FloatField(null=True, db_column='zMax', blank=True) # Field name made lowercase.
    radius              = models.FloatField(null=True, blank=True)
    class Meta:
        db_table        = u'mapUniverse'