from django.db import models

class AgentType(models.Model):
    id                  = models.IntegerField(primary_key=True, db_column='agentTypeID') # Field name made lowercase.
    type                = models.CharField(max_length=150, db_column='agentType', blank=True) # Field name made lowercase.
    class Meta:
        db_table        = u'agtAgentTypes'

class Agent(models.Model):
    id                  = models.IntegerField(primary_key=True, db_column='agentID') # Field name made lowercase.
    division            = models.ForeignKey("crp.NPCDivision", null=True, db_column='divisionID', blank=True) # Field name made lowercase.
    corporation         = models.ForeignKey("crp.NPCCorporation", null=True, db_column='corporationID', blank=True) # Field name made lowercase.
    location            = models.ForeignKey("map.Denormalize", null=True, db_column='locationID', blank=True) # Field name made lowercase.
    level               = models.IntegerField(null=True, blank=True)
    quality             = models.IntegerField(null=True, blank=True)
    type                = models.ForeignKey("agt.AgentType", null=True, db_column='agentTypeID', blank=True) # Field name made lowercase.
    islocator           = models.NullBooleanField(null=True, db_column='isLocator', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'agtAgents'

class ResearchAgent(models.Model):
    agent               = models.ForeignKey("agt.Agent", primary_key=True, db_column='agentID') # Field name made lowercase.
    type                = models.ForeignKey("inv.Type", db_column='typeID') # Field name made lowercase.
    class Meta:
        db_table        = u'agtResearchAgents'