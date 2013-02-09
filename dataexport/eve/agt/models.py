from django.db import models

class Agtagenttypes(models.Model):
    agenttypeid = models.IntegerField(primary_key=True, db_column='agentTypeID') # Field name made lowercase.
    agenttype = models.CharField(max_length=150, db_column='agentType', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'agtAgentTypes'

class Agtagents(models.Model):
    agentid = models.IntegerField(primary_key=True, db_column='agentID') # Field name made lowercase.
    divisionid = models.IntegerField(null=True, db_column='divisionID', blank=True) # Field name made lowercase.
    corporationid = models.IntegerField(null=True, db_column='corporationID', blank=True) # Field name made lowercase.
    locationid = models.IntegerField(null=True, db_column='locationID', blank=True) # Field name made lowercase.
    level = models.IntegerField(null=True, blank=True)
    quality = models.IntegerField(null=True, blank=True)
    agenttypeid = models.IntegerField(null=True, db_column='agentTypeID', blank=True) # Field name made lowercase.
    islocator = models.IntegerField(null=True, db_column='isLocator', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'agtAgents'

class Agtresearchagents(models.Model):
    agentid = models.IntegerField(primary_key=True, db_column='agentID') # Field name made lowercase.
    typeid = models.IntegerField(db_column='typeID') # Field name made lowercase.
    class Meta:
        db_table = u'agtResearchAgents'