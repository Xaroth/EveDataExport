from django.db import models

class Activity(models.Model):
    id                  = models.IntegerField(primary_key=True, db_column='activityID') # Field name made lowercase.
    name                = models.CharField(max_length=300, db_column='activityName', blank=True) # Field name made lowercase.
    iconno              = models.CharField(max_length=15, db_column='iconNo', blank=True) # Field name made lowercase.
    description         = models.CharField(max_length=3000, blank=True)
    published           = models.NullBooleanField(null=True, blank=True)
    class Meta:
        db_table        = u'ramActivities'

class AssemblyLineStation(models.Model):
    station             = models.ForeignKey("sta.Station", primary_key=True, db_column='stationID') # Field name made lowercase.
    assemblylinetype    = models.ForeignKey("ram.AssemblyLineType", primary_key=True, db_column='assemblyLineTypeID') # Field name made lowercase.
    quantity            = models.IntegerField(null=True, blank=True)
    stationtype         = models.ForeignKey("sta.StationType", null=True, db_column='stationTypeID', blank=True) # Field name made lowercase.
    owner               = models.ForeignKey("crp.NPCCorporation", null=True, db_column='ownerID', blank=True) # Field name made lowercase.
    solarsystem         = models.ForeignKey("map.SolarSystem", null=True, db_column='solarSystemID', blank=True) # Field name made lowercase.
    region              = models.ForeignKey("map.Region", null=True, db_column='regionID', blank=True) # Field name made lowercase.
    class Meta:
        db_table        = u'ramAssemblyLineStations'

class AssemblyLineTypeDetailPerCategory(models.Model):
    assemblylinetype    = models.ForeignKey("ram.AssemblyLineType", primary_key=True, db_column='assemblyLineTypeID') # Field name made lowercase.
    category            = models.ForeignKey("inv.Category", primary_key=True, db_column='categoryID') # Field name made lowercase.
    timemultiplier      = models.FloatField(null=True, db_column='timeMultiplier', blank=True) # Field name made lowercase.
    materialmultiplier  = models.FloatField(null=True, db_column='materialMultiplier', blank=True) # Field name made lowercase.
    class Meta:
        db_table        = u'ramAssemblyLineTypeDetailPerCategory'

class AssemblyLineTypeDetailPerGroup(models.Model):
    assemblylinetype    = models.ForeignKey("ram.AssemblyLineType", primary_key=True, db_column='assemblyLineTypeID') # Field name made lowercase.
    group               = models.ForeignKey("inv.Group", primary_key=True, db_column='groupID') # Field name made lowercase.
    timemultiplier      = models.FloatField(null=True, db_column='timeMultiplier', blank=True) # Field name made lowercase.
    materialmultiplier  = models.FloatField(null=True, db_column='materialMultiplier', blank=True) # Field name made lowercase.
    class Meta:
        db_table        = u'ramAssemblyLineTypeDetailPerGroup'

class AssemblyLineType(models.Model):
    id                  = models.IntegerField(primary_key=True, db_column='assemblyLineTypeID') # Field name made lowercase.
    name                = models.CharField(max_length=300, db_column='assemblyLineTypeName', blank=True) # Field name made lowercase.
    description         = models.CharField(max_length=3000, blank=True)
    basetimemultiplier  = models.FloatField(null=True, db_column='baseTimeMultiplier', blank=True) # Field name made lowercase.
    basematerialmultiplier = models.FloatField(null=True, db_column='baseMaterialMultiplier', blank=True) # Field name made lowercase.
    volume              = models.FloatField(null=True, blank=True)
    activity            = models.ForeignKey("ram.Activity", null=True, db_column='activityID', blank=True) # Field name made lowercase.
    mincostperhour      = models.FloatField(null=True, db_column='minCostPerHour', blank=True) # Field name made lowercase.
    class Meta:
        db_table        = u'ramAssemblyLineTypes'

class AssemblyLine(models.Model):
    id                  = models.IntegerField(primary_key=True, db_column='assemblyLineID') # Field name made lowercase.
    type                = models.ForeignKey("ram.AssemblyLineType", null=True, db_column='assemblyLineTypeID', blank=True) # Field name made lowercase.
    container           = models.ForeignKey("sta.Station", null=True, db_column='containerID', blank=True) # Field name made lowercase.
    nextfreetime        = models.DateTimeField(null=True, db_column='nextFreeTime', blank=True) # Field name made lowercase.
    uigroupingid        = models.IntegerField(null=True, db_column='UIGroupingID', blank=True) # Field name made lowercase.
    costinstall         = models.FloatField(null=True, db_column='costInstall', blank=True) # Field name made lowercase.
    costperhour         = models.FloatField(null=True, db_column='costPerHour', blank=True) # Field name made lowercase.
    restrictionmask     = models.IntegerField(null=True, db_column='restrictionMask', blank=True) # Field name made lowercase.
    discountpergoodstandingpoint = models.FloatField(null=True, db_column='discountPerGoodStandingPoint', blank=True) # Field name made lowercase.
    surchargeperbadstandingpoint = models.FloatField(null=True, db_column='surchargePerBadStandingPoint', blank=True) # Field name made lowercase.
    minimumstanding     = models.FloatField(null=True, db_column='minimumStanding', blank=True) # Field name made lowercase.
    minimumcharsecurity = models.FloatField(null=True, db_column='minimumCharSecurity', blank=True) # Field name made lowercase.
    minimumcorpsecurity = models.FloatField(null=True, db_column='minimumCorpSecurity', blank=True) # Field name made lowercase.
    maximumcharsecurity = models.FloatField(null=True, db_column='maximumCharSecurity', blank=True) # Field name made lowercase.
    maximumcorpsecurity = models.FloatField(null=True, db_column='maximumCorpSecurity', blank=True) # Field name made lowercase.
    owner               = models.ForeignKey("crp.NPCCorporation", null=True, db_column='ownerID', blank=True) # Field name made lowercase.
    activity            = models.ForeignKey("ram.Activity", null=True, db_column='activityID', blank=True) # Field name made lowercase.
    class Meta:
        db_table        = u'ramAssemblyLines'

class InstallationTypeContent(models.Model):
    installationtype    = models.ForeignKey("inv.Type", primary_key=True, db_column='installationTypeID') # Field name made lowercase.
    assemblylinetype    = models.ForeignKey("inv.Type", primary_key=True, db_column='assemblyLineTypeID', related_name='+') # Field name made lowercase.
    quantity            = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table        = u'ramInstallationTypeContents'

class TypeRequirement(models.Model):
    type                = models.ForeignKey("inv.Type", primary_key=True, db_column='typeID') # Field name made lowercase.
    activity            = models.ForeignKey("ram.Activity", primary_key=True, db_column='activityID') # Field name made lowercase.
    requiredtype        = models.ForeignKey("inv.Type", primary_key=True, db_column='requiredTypeID', related_name='+') # Field name made lowercase.
    quantity            = models.IntegerField(null=True, blank=True)
    damageperjob        = models.FloatField(null=True, db_column='damagePerJob', blank=True) # Field name made lowercase.
    recycle             = models.NullBooleanField(null=True, blank=True)
    class Meta:
        db_table        = u'ramTypeRequirements'