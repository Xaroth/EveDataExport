from django.db import models

class Schematic(models.Model):
    id                  = models.IntegerField(primary_key=True, db_column='schematicID') # Field name made lowercase.
    name                = models.CharField(max_length=765, db_column='schematicName', blank=True) # Field name made lowercase.
    cycletime           = models.IntegerField(null=True, db_column='cycleTime', blank=True) # Field name made lowercase.
    class Meta:
        db_table        = u'planetSchematics'

class SchematicPinMap(models.Model):
    schematic           = models.ForeignKey("planet.Schematic", primary_key=True, db_column='schematicID') # Field name made lowercase.
    pintypeid           = models.ForeignKey("inv.Type", primary_key=True, db_column='pinTypeID') # Field name made lowercase.
    class Meta:
        db_table        = u'planetSchematicsPinMap'

class SchematicTypeMap(models.Model):
    schematic           = models.ForeignKey("planet.Schematic", primary_key=True, db_column='schematicID') # Field name made lowercase.
    type                = models.ForeignKey("inv.Type", primary_key=True, db_column='typeID') # Field name made lowercase.
    quantity            = models.IntegerField(null=True, blank=True)
    isinput             = models.NullBooleanField(null=True, db_column='isInput', blank=True) # Field name made lowercase.
    class Meta:
        db_table        = u'planetSchematicsTypeMap'