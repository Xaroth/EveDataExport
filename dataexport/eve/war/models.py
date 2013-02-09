from django.db import models

class CombatZoneSystem(models.Model):
    solarsystem         = models.ForeignKey("map.SolarSystem", primary_key=True, db_column='solarSystemID') # Field name made lowercase.
    combatzone          = models.ForeignKey("war.CombatZone", null=True, db_column='combatZoneID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'warCombatZoneSystems'

class CombatZone(models.Model):
    id                  = models.IntegerField(primary_key=True, db_column='combatZoneID') # Field name made lowercase.
    name                = models.CharField(max_length=300, db_column='combatZoneName', blank=True) # Field name made lowercase.
    faction             = models.ForeignKey("chr.Faction", null=True, db_column='factionID', blank=True) # Field name made lowercase.
    centersystem        = models.ForeignKey("map.SolarSystem", null=True, db_column='centerSystemID', blank=True) # Field name made lowercase.
    description         = models.CharField(max_length=1500, blank=True)
    class Meta:
        db_table        = u'warCombatZones'
