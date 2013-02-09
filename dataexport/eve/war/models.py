from django.db import models

class Warcombatzonesystems(models.Model):
    solarsystemid = models.IntegerField(primary_key=True, db_column='solarSystemID') # Field name made lowercase.
    combatzoneid = models.IntegerField(null=True, db_column='combatZoneID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'warCombatZoneSystems'

class Warcombatzones(models.Model):
    combatzoneid = models.IntegerField(primary_key=True, db_column='combatZoneID') # Field name made lowercase.
    combatzonename = models.CharField(max_length=300, db_column='combatZoneName', blank=True) # Field name made lowercase.
    factionid = models.IntegerField(null=True, db_column='factionID', blank=True) # Field name made lowercase.
    centersystemid = models.IntegerField(null=True, db_column='centerSystemID', blank=True) # Field name made lowercase.
    description = models.CharField(max_length=1500, blank=True)
    class Meta:
        db_table = u'warCombatZones'
