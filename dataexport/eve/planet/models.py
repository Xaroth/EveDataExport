from django.db import models

class Planetschematics(models.Model):
    schematicid = models.IntegerField(primary_key=True, db_column='schematicID') # Field name made lowercase.
    schematicname = models.CharField(max_length=765, db_column='schematicName', blank=True) # Field name made lowercase.
    cycletime = models.IntegerField(null=True, db_column='cycleTime', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'planetSchematics'

class Planetschematicspinmap(models.Model):
    schematicid = models.IntegerField(primary_key=True, db_column='schematicID') # Field name made lowercase.
    pintypeid = models.IntegerField(primary_key=True, db_column='pinTypeID') # Field name made lowercase.
    class Meta:
        db_table = u'planetSchematicsPinMap'

class Planetschematicstypemap(models.Model):
    schematicid = models.IntegerField(primary_key=True, db_column='schematicID') # Field name made lowercase.
    typeid = models.IntegerField(primary_key=True, db_column='typeID') # Field name made lowercase.
    quantity = models.IntegerField(null=True, blank=True)
    isinput = models.IntegerField(null=True, db_column='isInput', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'planetSchematicsTypeMap'