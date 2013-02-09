from django.db import models

class Evegraphics(models.Model):
    graphicid = models.IntegerField(primary_key=True, db_column='graphicID') # Field name made lowercase.
    graphicfile = models.CharField(max_length=1500, db_column='graphicFile') # Field name made lowercase.
    description = models.TextField()
    obsolete = models.IntegerField()
    graphictype = models.CharField(max_length=300, db_column='graphicType', blank=True) # Field name made lowercase.
    collidable = models.IntegerField(null=True, blank=True)
    explosionid = models.IntegerField(null=True, db_column='explosionID', blank=True) # Field name made lowercase.
    directoryid = models.IntegerField(null=True, db_column='directoryID', blank=True) # Field name made lowercase.
    graphicname = models.CharField(max_length=192, db_column='graphicName') # Field name made lowercase.
    class Meta:
        db_table = u'eveGraphics'

class Eveicons(models.Model):
    iconid = models.IntegerField(primary_key=True, db_column='iconID') # Field name made lowercase.
    iconfile = models.CharField(max_length=1500, db_column='iconFile') # Field name made lowercase.
    description = models.TextField()
    class Meta:
        db_table = u'eveIcons'

class Eveunits(models.Model):
    unitid = models.IntegerField(primary_key=True, db_column='unitID') # Field name made lowercase.
    unitname = models.CharField(max_length=300, db_column='unitName', blank=True) # Field name made lowercase.
    displayname = models.CharField(max_length=150, db_column='displayName', blank=True) # Field name made lowercase.
    description = models.CharField(max_length=3000, blank=True)
    class Meta:
        db_table = u'eveUnits'