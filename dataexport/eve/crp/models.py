from django.db import models

class Activity(models.Model):
    id                  = models.IntegerField(primary_key=True, db_column='activityID') # Field name made lowercase.
    name                = models.CharField(max_length=300, db_column='activityName', blank=True) # Field name made lowercase.
    description         = models.CharField(max_length=3000, blank=True)
    class Meta:
        db_table        = u'crpActivities'

class NPCCorporationDivision(models.Model):
    corporation         = models.ForeignKey("crp.NPCCorporation", primary_key=True, db_column='corporationID') # Field name made lowercase.
    division            = models.ForeignKey("crp.NPCDivision", primary_key=True, db_column='divisionID') # Field name made lowercase.
    size                = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'crpNPCCorporationDivisions'

class NPCCorporationResearchField(models.Model):
    skill               = models.ForeignKey("inv.Type", primary_key=True, db_column='skillID') # Field name made lowercase.
    corporation         = models.ForeignKey("crp.NPCCorporation", primary_key=True, db_column='corporationID') # Field name made lowercase.
    class Meta:
        db_table = u'crpNPCCorporationResearchFields'

class NPCCorporationTrade(models.Model):
    corporation         = models.ForeignKey("crp.NPCCorporation", primary_key=True, db_column='corporationID') # Field name made lowercase.
    type                = models.ForeignKey("inv.Type", primary_key=True, db_column='typeID') # Field name made lowercase.
    class Meta:
        db_table        = u'crpNPCCorporationTrades'

class NPCCorporation(models.Model):
    id                  = models.IntegerField(primary_key=True, db_column='corporationID') # Field name made lowercase.
    size                = models.CharField(max_length=3, blank=True)
    extent              = models.CharField(max_length=3, blank=True)
    solarsystem         = models.ForeignKey("map.SolarSystem", null=True, db_column='solarSystemID', blank=True) # Field name made lowercase.
    investor1           = models.ForeignKey("crp.NPCCorporation", null=True, db_column='investorID1', blank=True, related_name='+') # Field name made lowercase.
    investorshares1     = models.IntegerField(null=True, db_column='investorShares1', blank=True) # Field name made lowercase.
    investor2           = models.ForeignKey("crp.NPCCorporation", null=True, db_column='investorID2', blank=True, related_name='+') # Field name made lowercase.
    investorshares2     = models.IntegerField(null=True, db_column='investorShares2', blank=True) # Field name made lowercase.
    investor3           = models.ForeignKey("crp.NPCCorporation", null=True, db_column='investorID3', blank=True, related_name='+') # Field name made lowercase.
    investorshares3     = models.IntegerField(null=True, db_column='investorShares3', blank=True) # Field name made lowercase.
    investor4           = models.ForeignKey("crp.NPCCorporation", null=True, db_column='investorID4', blank=True, related_name='+') # Field name made lowercase.
    investorshares4     = models.IntegerField(null=True, db_column='investorShares4', blank=True) # Field name made lowercase.
    friend              = models.ForeignKey("crp.NPCCorporation", null=True, db_column='friendID', blank=True, related_name='friends_of') # Field name made lowercase.
    enemy               = models.ForeignKey("crp.NPCCorporation", null=True, db_column='enemyID', blank=True, related_name='enemies_of') # Field name made lowercase.
    publicshares        = models.BigIntegerField(null=True, db_column='publicShares', blank=True) # Field name made lowercase.
    initialprice        = models.IntegerField(null=True, db_column='initialPrice', blank=True) # Field name made lowercase.
    minsecurity         = models.FloatField(null=True, db_column='minSecurity', blank=True) # Field name made lowercase.
    scattered           = models.NullBooleanField(null=True, blank=True)
    fringe              = models.IntegerField(null=True, blank=True)
    corridor            = models.IntegerField(null=True, blank=True)
    hub                 = models.IntegerField(null=True, blank=True)
    border              = models.IntegerField(null=True, blank=True)
    faction             = models.ForeignKey("chr.Faction", null=True, db_column='factionID', blank=True) # Field name made lowercase.
    sizefactor          = models.FloatField(null=True, db_column='sizeFactor', blank=True) # Field name made lowercase.
    stationcount        = models.IntegerField(null=True, db_column='stationCount', blank=True) # Field name made lowercase.
    stationsystemcount  = models.IntegerField(null=True, db_column='stationSystemCount', blank=True) # Field name made lowercase.
    description         = models.CharField(max_length=12000, blank=True)
    icon                = models.ForeignKey("eve.Icon", null=True, db_column='iconID', blank=True)
    class Meta:
        db_table        = u'crpNPCCorporations'

class NPCDivision(models.Model):
    id                  = models.IntegerField(primary_key=True, db_column='divisionID') # Field name made lowercase.
    name                = models.CharField(max_length=300, db_column='divisionName', blank=True) # Field name made lowercase.
    description         = models.CharField(max_length=3000, blank=True)
    leadertype          = models.CharField(max_length=300, db_column='leaderType', blank=True) # Field name made lowercase.
    class Meta:
        db_table        = u'crpNPCDivisions'