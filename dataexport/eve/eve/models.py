from django.db import models

class Graphic(models.Model):
    id                  = models.AutoField(primary_key=True, db_column='graphicID')
    filename            = models.CharField(max_length=1500, db_column='graphicFile')
    description         = models.TextField()
    obsolete            = models.IntegerField()
    graphictype         = models.CharField(max_length=300, db_column='graphicType', blank=True)
    collidable          = models.IntegerField(null=True, blank=True)
    explosionid         = models.IntegerField(null=True, db_column='explosionID', blank=True)
    directoryid         = models.IntegerField(null=True, db_column='directoryID', blank=True)
    graphicname         = models.CharField(max_length=192, db_column='graphicName')

    class Meta:
        db_table        = u'eveGraphics'
        ordering        = ('id',)

class Icon(models.Model):
    id                  = models.AutoField(primary_key=True, db_column='iconID')
    filename            = models.CharField(max_length=1500, db_column='iconFile')
    description         = models.TextField()

    class Meta:
        db_table        = u'eveIcons'
        ordering        = ('id',)

class Unit(models.Model):
    id                  = models.AutoField(primary_key=True, db_column='unitID')
    name                = models.CharField(max_length=300, db_column='unitName', blank=True)
    displayname         = models.CharField(max_length=150, db_column='displayName', blank=True)
    description         = models.CharField(max_length=3000, blank=True)

    class Meta:
        db_table        = u'eveUnits'
        ordering        = ('id',)