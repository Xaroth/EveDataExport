from django.db import models

class Mapcelestialstatistics(models.Model):
    celestialid = models.IntegerField(primary_key=True, db_column='celestialID') # Field name made lowercase.
    temperature = models.FloatField(null=True, blank=True)
    spectralclass = models.CharField(max_length=30, db_column='spectralClass', blank=True) # Field name made lowercase.
    luminosity = models.FloatField(null=True, blank=True)
    age = models.FloatField(null=True, blank=True)
    life = models.FloatField(null=True, blank=True)
    orbitradius = models.FloatField(null=True, db_column='orbitRadius', blank=True) # Field name made lowercase.
    eccentricity = models.FloatField(null=True, blank=True)
    massdust = models.FloatField(null=True, db_column='massDust', blank=True) # Field name made lowercase.
    massgas = models.FloatField(null=True, db_column='massGas', blank=True) # Field name made lowercase.
    fragmented = models.IntegerField(null=True, blank=True)
    density = models.FloatField(null=True, blank=True)
    surfacegravity = models.FloatField(null=True, db_column='surfaceGravity', blank=True) # Field name made lowercase.
    escapevelocity = models.FloatField(null=True, db_column='escapeVelocity', blank=True) # Field name made lowercase.
    orbitperiod = models.FloatField(null=True, db_column='orbitPeriod', blank=True) # Field name made lowercase.
    rotationrate = models.FloatField(null=True, db_column='rotationRate', blank=True) # Field name made lowercase.
    locked = models.IntegerField(null=True, blank=True)
    pressure = models.FloatField(null=True, blank=True)
    radius = models.FloatField(null=True, blank=True)
    mass = models.FloatField(null=True, blank=True)
    class Meta:
        db_table = u'mapCelestialStatistics'

class Mapconstellationjumps(models.Model):
    fromregionid = models.IntegerField(null=True, db_column='fromRegionID', blank=True) # Field name made lowercase.
    fromconstellationid = models.IntegerField(primary_key=True, db_column='fromConstellationID') # Field name made lowercase.
    toconstellationid = models.IntegerField(primary_key=True, db_column='toConstellationID') # Field name made lowercase.
    toregionid = models.IntegerField(null=True, db_column='toRegionID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'mapConstellationJumps'

class Mapconstellations(models.Model):
    regionid = models.IntegerField(null=True, db_column='regionID', blank=True) # Field name made lowercase.
    constellationid = models.IntegerField(primary_key=True, db_column='constellationID') # Field name made lowercase.
    constellationname = models.CharField(max_length=300, db_column='constellationName', blank=True) # Field name made lowercase.
    x = models.FloatField(null=True, blank=True)
    y = models.FloatField(null=True, blank=True)
    z = models.FloatField(null=True, blank=True)
    xmin = models.FloatField(null=True, db_column='xMin', blank=True) # Field name made lowercase.
    xmax = models.FloatField(null=True, db_column='xMax', blank=True) # Field name made lowercase.
    ymin = models.FloatField(null=True, db_column='yMin', blank=True) # Field name made lowercase.
    ymax = models.FloatField(null=True, db_column='yMax', blank=True) # Field name made lowercase.
    zmin = models.FloatField(null=True, db_column='zMin', blank=True) # Field name made lowercase.
    zmax = models.FloatField(null=True, db_column='zMax', blank=True) # Field name made lowercase.
    factionid = models.IntegerField(null=True, db_column='factionID', blank=True) # Field name made lowercase.
    radius = models.FloatField(null=True, blank=True)
    class Meta:
        db_table = u'mapConstellations'

class Mapdenormalize(models.Model):
    itemid = models.IntegerField(primary_key=True, db_column='itemID') # Field name made lowercase.
    typeid = models.IntegerField(null=True, db_column='typeID', blank=True) # Field name made lowercase.
    groupid = models.IntegerField(null=True, db_column='groupID', blank=True) # Field name made lowercase.
    solarsystemid = models.IntegerField(null=True, db_column='solarSystemID', blank=True) # Field name made lowercase.
    constellationid = models.IntegerField(null=True, db_column='constellationID', blank=True) # Field name made lowercase.
    regionid = models.IntegerField(null=True, db_column='regionID', blank=True) # Field name made lowercase.
    orbitid = models.IntegerField(null=True, db_column='orbitID', blank=True) # Field name made lowercase.
    x = models.FloatField(null=True, blank=True)
    y = models.FloatField(null=True, blank=True)
    z = models.FloatField(null=True, blank=True)
    radius = models.FloatField(null=True, blank=True)
    itemname = models.CharField(max_length=300, db_column='itemName', blank=True) # Field name made lowercase.
    security = models.FloatField(null=True, blank=True)
    celestialindex = models.IntegerField(null=True, db_column='celestialIndex', blank=True) # Field name made lowercase.
    orbitindex = models.IntegerField(null=True, db_column='orbitIndex', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'mapDenormalize'

class Mapjumps(models.Model):
    stargateid = models.IntegerField(primary_key=True, db_column='stargateID') # Field name made lowercase.
    celestialid = models.IntegerField(null=True, db_column='celestialID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'mapJumps'

class Maplandmarks(models.Model):
    landmarkid = models.IntegerField(primary_key=True, db_column='landmarkID') # Field name made lowercase.
    landmarkname = models.CharField(max_length=300, db_column='landmarkName', blank=True) # Field name made lowercase.
    description = models.CharField(max_length=21000, blank=True)
    locationid = models.IntegerField(null=True, db_column='locationID', blank=True) # Field name made lowercase.
    x = models.FloatField(null=True, blank=True)
    y = models.FloatField(null=True, blank=True)
    z = models.FloatField(null=True, blank=True)
    radius = models.FloatField(null=True, blank=True)
    iconid = models.IntegerField(null=True, db_column='iconID', blank=True) # Field name made lowercase.
    importance = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'mapLandmarks'

class Maplocationscenes(models.Model):
    locationid = models.IntegerField(primary_key=True, db_column='locationID') # Field name made lowercase.
    graphicid = models.IntegerField(null=True, db_column='graphicID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'mapLocationScenes'

class Maplocationwormholeclasses(models.Model):
    locationid = models.IntegerField(primary_key=True, db_column='locationID') # Field name made lowercase.
    wormholeclassid = models.IntegerField(null=True, db_column='wormholeClassID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'mapLocationWormholeClasses'

class Mapregionjumps(models.Model):
    fromregionid = models.IntegerField(primary_key=True, db_column='fromRegionID') # Field name made lowercase.
    toregionid = models.IntegerField(primary_key=True, db_column='toRegionID') # Field name made lowercase.
    class Meta:
        db_table = u'mapRegionJumps'

class Mapregions(models.Model):
    regionid = models.IntegerField(primary_key=True, db_column='regionID') # Field name made lowercase.
    regionname = models.CharField(max_length=300, db_column='regionName', blank=True) # Field name made lowercase.
    x = models.FloatField(null=True, blank=True)
    y = models.FloatField(null=True, blank=True)
    z = models.FloatField(null=True, blank=True)
    xmin = models.FloatField(null=True, db_column='xMin', blank=True) # Field name made lowercase.
    xmax = models.FloatField(null=True, db_column='xMax', blank=True) # Field name made lowercase.
    ymin = models.FloatField(null=True, db_column='yMin', blank=True) # Field name made lowercase.
    ymax = models.FloatField(null=True, db_column='yMax', blank=True) # Field name made lowercase.
    zmin = models.FloatField(null=True, db_column='zMin', blank=True) # Field name made lowercase.
    zmax = models.FloatField(null=True, db_column='zMax', blank=True) # Field name made lowercase.
    factionid = models.IntegerField(null=True, db_column='factionID', blank=True) # Field name made lowercase.
    radius = models.FloatField(null=True, blank=True)
    class Meta:
        db_table = u'mapRegions'

class Mapsolarsystemjumps(models.Model):
    fromregionid = models.IntegerField(null=True, db_column='fromRegionID', blank=True) # Field name made lowercase.
    fromconstellationid = models.IntegerField(null=True, db_column='fromConstellationID', blank=True) # Field name made lowercase.
    fromsolarsystemid = models.IntegerField(primary_key=True, db_column='fromSolarSystemID') # Field name made lowercase.
    tosolarsystemid = models.IntegerField(primary_key=True, db_column='toSolarSystemID') # Field name made lowercase.
    toconstellationid = models.IntegerField(null=True, db_column='toConstellationID', blank=True) # Field name made lowercase.
    toregionid = models.IntegerField(null=True, db_column='toRegionID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'mapSolarSystemJumps'

class Mapsolarsystems(models.Model):
    regionid = models.IntegerField(null=True, db_column='regionID', blank=True) # Field name made lowercase.
    constellationid = models.IntegerField(null=True, db_column='constellationID', blank=True) # Field name made lowercase.
    solarsystemid = models.IntegerField(primary_key=True, db_column='solarSystemID') # Field name made lowercase.
    solarsystemname = models.CharField(max_length=300, db_column='solarSystemName', blank=True) # Field name made lowercase.
    x = models.FloatField(null=True, blank=True)
    y = models.FloatField(null=True, blank=True)
    z = models.FloatField(null=True, blank=True)
    xmin = models.FloatField(null=True, db_column='xMin', blank=True) # Field name made lowercase.
    xmax = models.FloatField(null=True, db_column='xMax', blank=True) # Field name made lowercase.
    ymin = models.FloatField(null=True, db_column='yMin', blank=True) # Field name made lowercase.
    ymax = models.FloatField(null=True, db_column='yMax', blank=True) # Field name made lowercase.
    zmin = models.FloatField(null=True, db_column='zMin', blank=True) # Field name made lowercase.
    zmax = models.FloatField(null=True, db_column='zMax', blank=True) # Field name made lowercase.
    luminosity = models.FloatField(null=True, blank=True)
    border = models.IntegerField(null=True, blank=True)
    fringe = models.IntegerField(null=True, blank=True)
    corridor = models.IntegerField(null=True, blank=True)
    hub = models.IntegerField(null=True, blank=True)
    international = models.IntegerField(null=True, blank=True)
    regional = models.IntegerField(null=True, blank=True)
    constellation = models.IntegerField(null=True, blank=True)
    security = models.FloatField(null=True, blank=True)
    factionid = models.IntegerField(null=True, db_column='factionID', blank=True) # Field name made lowercase.
    radius = models.FloatField(null=True, blank=True)
    suntypeid = models.IntegerField(null=True, db_column='sunTypeID', blank=True) # Field name made lowercase.
    securityclass = models.CharField(max_length=6, db_column='securityClass', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'mapSolarSystems'

class Mapuniverse(models.Model):
    universeid = models.IntegerField(primary_key=True, db_column='universeID') # Field name made lowercase.
    universename = models.CharField(max_length=300, db_column='universeName', blank=True) # Field name made lowercase.
    x = models.FloatField(null=True, blank=True)
    y = models.FloatField(null=True, blank=True)
    z = models.FloatField(null=True, blank=True)
    xmin = models.FloatField(null=True, db_column='xMin', blank=True) # Field name made lowercase.
    xmax = models.FloatField(null=True, db_column='xMax', blank=True) # Field name made lowercase.
    ymin = models.FloatField(null=True, db_column='yMin', blank=True) # Field name made lowercase.
    ymax = models.FloatField(null=True, db_column='yMax', blank=True) # Field name made lowercase.
    zmin = models.FloatField(null=True, db_column='zMin', blank=True) # Field name made lowercase.
    zmax = models.FloatField(null=True, db_column='zMax', blank=True) # Field name made lowercase.
    radius = models.FloatField(null=True, blank=True)
    class Meta:
        db_table = u'mapUniverse'