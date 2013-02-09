from django.db import models

class OperationService(models.Model):
    operationid         = models.ForeignKey("sta.Operation", primary_key=True, db_column='operationID') # Field name made lowercase.
    serviceid           = models.ForeignKey("sta.Service", primary_key=True, db_column='serviceID') # Field name made lowercase.
    class Meta:
        db_table = u'staOperationServices'

class Operation(models.Model):
    activity            = models.ForeignKey("crp.Activity", null=True, db_column='activityID', blank=True) # Field name made lowercase.
    id                  = models.IntegerField(primary_key=True, db_column='operationID') # Field name made lowercase.
    name                = models.CharField(max_length=300, db_column='operationName', blank=True) # Field name made lowercase.
    description         = models.CharField(max_length=3000, blank=True)
    fringe              = models.IntegerField(null=True, blank=True)
    corridor            = models.IntegerField(null=True, blank=True)
    hub                 = models.IntegerField(null=True, blank=True)
    border              = models.IntegerField(null=True, blank=True)
    ratio               = models.IntegerField(null=True, blank=True)
    caldaristationtypeid = models.ForeignKey("sta.StationType", null=True, db_column='caldariStationTypeID', blank=True, related_name='+') # Field name made lowercase.
    minmatarstationtypeid = models.ForeignKey("sta.StationType", null=True, db_column='minmatarStationTypeID', blank=True, related_name='+') # Field name made lowercase.
    amarrstationtypeid  = models.ForeignKey("sta.StationType", null=True, db_column='amarrStationTypeID', blank=True, related_name='+') # Field name made lowercase.
    gallentestationtypeid = models.ForeignKey("sta.StationType", null=True, db_column='gallenteStationTypeID', blank=True, related_name='+') # Field name made lowercase.
    jovestationtypeid   = models.ForeignKey("sta.StationType", null=True, db_column='joveStationTypeID', blank=True, related_name='+') # Field name made lowercase.
    class Meta:
        db_table        = u'staOperations'

class Service(models.Model):
    id                  = models.IntegerField(primary_key=True, db_column='serviceID') # Field name made lowercase.
    name                = models.CharField(max_length=300, db_column='serviceName', blank=True) # Field name made lowercase.
    description         = models.CharField(max_length=3000, blank=True)
    class Meta:
        db_table        = u'staServices'

class StationType(models.Model):
    stationtype         = models.ForeignKey("inv.Type", primary_key=True, db_column='stationTypeID') # Field name made lowercase.
    dockentryx          = models.FloatField(null=True, db_column='dockEntryX', blank=True) # Field name made lowercase.
    dockentryy          = models.FloatField(null=True, db_column='dockEntryY', blank=True) # Field name made lowercase.
    dockentryz          = models.FloatField(null=True, db_column='dockEntryZ', blank=True) # Field name made lowercase.
    dockorientationx    = models.FloatField(null=True, db_column='dockOrientationX', blank=True) # Field name made lowercase.
    dockorientationy    = models.FloatField(null=True, db_column='dockOrientationY', blank=True) # Field name made lowercase.
    dockorientationz    = models.FloatField(null=True, db_column='dockOrientationZ', blank=True) # Field name made lowercase.
    operation           = models.ForeignKey("sta.Operation", null=True, db_column='operationID', blank=True) # Field name made lowercase.
    officeslots         = models.IntegerField(null=True, db_column='officeSlots', blank=True) # Field name made lowercase.
    reprocessingefficiency = models.FloatField(null=True, db_column='reprocessingEfficiency', blank=True) # Field name made lowercase.
    conquerable         = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table        = u'staStationTypes'

class Station(models.Model):
    id                  = models.IntegerField(primary_key=True, db_column='stationID') # Field name made lowercase.
    security            = models.IntegerField(null=True, blank=True)
    dockingcostpervolume = models.FloatField(null=True, db_column='dockingCostPerVolume', blank=True) # Field name made lowercase.
    maxshipvolumedockable = models.FloatField(null=True, db_column='maxShipVolumeDockable', blank=True) # Field name made lowercase.
    officerentalcost    = models.IntegerField(null=True, db_column='officeRentalCost', blank=True) # Field name made lowercase.
    operation           = models.ForeignKey("sta.Operation", null=True, db_column='operationID', blank=True) # Field name made lowercase.
    stationtype         = models.ForeignKey("sta.StationType", null=True, db_column='stationTypeID', blank=True) # Field name made lowercase.
    corporation         = models.ForeignKey("crp.NPCCorporation", null=True, db_column='corporationID', blank=True) # Field name made lowercase.
    solarsystem         = models.ForeignKey("map.SolarSystem", null=True, db_column='solarSystemID', blank=True) # Field name made lowercase.
    constellation       = models.ForeignKey("map.Constellation", null=True, db_column='constellationID', blank=True) # Field name made lowercase.
    region              = models.ForeignKey("map.Region", null=True, db_column='regionID', blank=True) # Field name made lowercase.
    name                = models.CharField(max_length=300, db_column='stationName', blank=True) # Field name made lowercase.
    x                   = models.FloatField(null=True, blank=True)
    y                   = models.FloatField(null=True, blank=True)
    z                   = models.FloatField(null=True, blank=True)
    reprocessingefficiency = models.FloatField(null=True, db_column='reprocessingEfficiency', blank=True) # Field name made lowercase.
    reprocessingstationstake = models.FloatField(null=True, db_column='reprocessingStationsTake', blank=True) # Field name made lowercase.
    reprocessinghangarflag = models.IntegerField(null=True, db_column='reprocessingHangarFlag', blank=True) # Field name made lowercase.
    class Meta:
        db_table        = u'staStations'