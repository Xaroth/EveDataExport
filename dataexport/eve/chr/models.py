from django.db import models

class Ancestry(models.Model):
    id                  = models.IntegerField(primary_key=True, db_column='ancestryID') # Field name made lowercase.
    ancestryname        = models.CharField(max_length=300, db_column='ancestryName', blank=True) # Field name made lowercase.
    bloodline           = models.ForeignKey("chr.Bloodline", null=True, db_column='bloodlineID', blank=True) # Field name made lowercase.
    description         = models.CharField(max_length=3000, blank=True)
    perception          = models.IntegerField(null=True, blank=True)
    willpower           = models.IntegerField(null=True, blank=True)
    charisma            = models.IntegerField(null=True, blank=True)
    memory              = models.IntegerField(null=True, blank=True)
    intelligence        = models.IntegerField(null=True, blank=True)
    icon                = models.ForeignKey("eve.Icon", null=True, db_column='iconID', blank=True)
    shortdescription    = models.CharField(max_length=1500, db_column='shortDescription', blank=True) # Field name made lowercase.
    class Meta:
        db_table        = u'chrAncestries'

class Attribute(models.Model):
    id                  = models.IntegerField(primary_key=True, db_column='attributeID') # Field name made lowercase.
    attributename       = models.CharField(max_length=300, db_column='attributeName', blank=True) # Field name made lowercase.
    description         = models.CharField(max_length=3000, blank=True)
    icon                = models.ForeignKey("eve.Icon", null=True, db_column='iconID', blank=True)
    shortdescription    = models.CharField(max_length=1500, db_column='shortDescription', blank=True) # Field name made lowercase.
    notes               = models.CharField(max_length=1500, blank=True)
    class Meta:
        db_table        = u'chrAttributes'

class Bloodline(models.Model):
    id                  = models.IntegerField(primary_key=True, db_column='bloodlineID') # Field name made lowercase.
    name                = models.CharField(max_length=300, db_column='bloodlineName', blank=True) # Field name made lowercase.
    raceid              = models.IntegerField(null=True, db_column='raceID', blank=True) # Field name made lowercase.
    description         = models.CharField(max_length=3000, blank=True)
    maledescription     = models.CharField(max_length=3000, db_column='maleDescription', blank=True) # Field name made lowercase.
    femaledescription   = models.CharField(max_length=3000, db_column='femaleDescription', blank=True) # Field name made lowercase.
    shiptypeid          = models.ForeignKey("inv.Type", null=True, db_column='shipTypeID', blank=True) # Field name made lowercase.
    corporationid       = models.ForeignKey("crp.NPCCorporation", null=True, db_column='corporationID', blank=True) # Field name made lowercase.
    perception          = models.IntegerField(null=True, blank=True)
    willpower           = models.IntegerField(null=True, blank=True)
    charisma            = models.IntegerField(null=True, blank=True)
    memory              = models.IntegerField(null=True, blank=True)
    intelligence        = models.IntegerField(null=True, blank=True)
    icon                = models.ForeignKey("eve.Icon", null=True, db_column='iconID', blank=True)
    shortdescription    = models.CharField(max_length=1500, db_column='shortDescription', blank=True) # Field name made lowercase.
    shortmaledescription = models.CharField(max_length=1500, db_column='shortMaleDescription', blank=True) # Field name made lowercase.
    shortfemaledescription = models.CharField(max_length=1500, db_column='shortFemaleDescription', blank=True) # Field name made lowercase.
    class Meta:
        db_table        = u'chrBloodlines'

class Faction(models.Model):
    id                  = models.IntegerField(primary_key=True, db_column='factionID') # Field name made lowercase.
    name                = models.CharField(max_length=300, db_column='factionName', blank=True) # Field name made lowercase.
    description         = models.CharField(max_length=3000, blank=True)
    raceids             = models.IntegerField(null=True, db_column='raceIDs', blank=True) # Field name made lowercase.
    solarsystem         = models.ForeignKey("map.SolarSystem", null=True, db_column='solarSystemID', blank=True, related_name='faction_homes') # Field name made lowercase.
    corporation         = models.ForeignKey("crp.NPCCorporation", null=True, db_column='corporationID', blank=True, related_name='+') # Field name made lowercase.
    sizefactor          = models.FloatField(null=True, db_column='sizeFactor', blank=True) # Field name made lowercase.
    stationcount        = models.IntegerField(null=True, db_column='stationCount', blank=True) # Field name made lowercase.
    stationsystemcount  = models.IntegerField(null=True, db_column='stationSystemCount', blank=True) # Field name made lowercase.
    militiacorporation  = models.ForeignKey("crp.NPCCorporation", null=True, db_column='militiaCorporationID', blank=True, related_name='+') # Field name made lowercase.
    icon                = models.ForeignKey("eve.Icon", null=True, db_column='iconID', blank=True)
    class Meta:
        db_table        = u'chrFactions'

class Race(models.Model):
    id                  = models.IntegerField(primary_key=True, db_column='raceID') # Field name made lowercase.
    name                = models.CharField(max_length=300, db_column='raceName', blank=True) # Field name made lowercase.
    description         = models.CharField(max_length=3000, blank=True)
    icon                = models.ForeignKey("eve.Icon", null=True, db_column='iconID', blank=True)
    shortdescription    = models.CharField(max_length=1500, db_column='shortDescription', blank=True) # Field name made lowercase.
    class Meta:
        db_table        = u'chrRaces'