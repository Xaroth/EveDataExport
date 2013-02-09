from django.db import models

class Dgmattributecategories(models.Model):
    categoryid = models.IntegerField(primary_key=True, db_column='categoryID') # Field name made lowercase.
    categoryname = models.CharField(max_length=150, db_column='categoryName', blank=True) # Field name made lowercase.
    categorydescription = models.CharField(max_length=600, db_column='categoryDescription', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'dgmAttributeCategories'

class Dgmattributetypes(models.Model):
    attributeid = models.IntegerField(primary_key=True, db_column='attributeID') # Field name made lowercase.
    attributename = models.CharField(max_length=300, db_column='attributeName', blank=True) # Field name made lowercase.
    description = models.CharField(max_length=3000, blank=True)
    icon = models.ForeignKey("eve.Icon", null=True, db_column='iconID', blank=True)
    defaultvalue = models.FloatField(null=True, db_column='defaultValue', blank=True) # Field name made lowercase.
    published = models.IntegerField(null=True, blank=True)
    displayname = models.CharField(max_length=300, db_column='displayName', blank=True) # Field name made lowercase.
    unitid = models.IntegerField(null=True, db_column='unitID', blank=True) # Field name made lowercase.
    stackable = models.IntegerField(null=True, blank=True)
    highisgood = models.IntegerField(null=True, db_column='highIsGood', blank=True) # Field name made lowercase.
    categoryid = models.IntegerField(null=True, db_column='categoryID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'dgmAttributeTypes'

class Dgmeffects(models.Model):
    effectid = models.IntegerField(primary_key=True, db_column='effectID') # Field name made lowercase.
    effectname = models.CharField(max_length=1200, db_column='effectName', blank=True) # Field name made lowercase.
    effectcategory = models.IntegerField(null=True, db_column='effectCategory', blank=True) # Field name made lowercase.
    preexpression = models.IntegerField(null=True, db_column='preExpression', blank=True) # Field name made lowercase.
    postexpression = models.IntegerField(null=True, db_column='postExpression', blank=True) # Field name made lowercase.
    description = models.CharField(max_length=3000, blank=True)
    guid = models.CharField(max_length=180, blank=True)
    icon = models.ForeignKey("eve.Icon", null=True, db_column='iconID', blank=True)
    isoffensive = models.IntegerField(null=True, db_column='isOffensive', blank=True) # Field name made lowercase.
    isassistance = models.IntegerField(null=True, db_column='isAssistance', blank=True) # Field name made lowercase.
    durationattributeid = models.IntegerField(null=True, db_column='durationAttributeID', blank=True) # Field name made lowercase.
    trackingspeedattributeid = models.IntegerField(null=True, db_column='trackingSpeedAttributeID', blank=True) # Field name made lowercase.
    dischargeattributeid = models.IntegerField(null=True, db_column='dischargeAttributeID', blank=True) # Field name made lowercase.
    rangeattributeid = models.IntegerField(null=True, db_column='rangeAttributeID', blank=True) # Field name made lowercase.
    falloffattributeid = models.IntegerField(null=True, db_column='falloffAttributeID', blank=True) # Field name made lowercase.
    disallowautorepeat = models.IntegerField(null=True, db_column='disallowAutoRepeat', blank=True) # Field name made lowercase.
    published = models.IntegerField(null=True, blank=True)
    displayname = models.CharField(max_length=300, db_column='displayName', blank=True) # Field name made lowercase.
    iswarpsafe = models.IntegerField(null=True, db_column='isWarpSafe', blank=True) # Field name made lowercase.
    rangechance = models.IntegerField(null=True, db_column='rangeChance', blank=True) # Field name made lowercase.
    electronicchance = models.IntegerField(null=True, db_column='electronicChance', blank=True) # Field name made lowercase.
    propulsionchance = models.IntegerField(null=True, db_column='propulsionChance', blank=True) # Field name made lowercase.
    distribution = models.IntegerField(null=True, blank=True)
    sfxname = models.CharField(max_length=60, db_column='sfxName', blank=True) # Field name made lowercase.
    npcusagechanceattributeid = models.IntegerField(null=True, db_column='npcUsageChanceAttributeID', blank=True) # Field name made lowercase.
    npcactivationchanceattributeid = models.IntegerField(null=True, db_column='npcActivationChanceAttributeID', blank=True) # Field name made lowercase.
    fittingusagechanceattributeid = models.IntegerField(null=True, db_column='fittingUsageChanceAttributeID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'dgmEffects'

class Dgmtypeattributes(models.Model):
    typeid = models.IntegerField(primary_key=True, db_column='typeID') # Field name made lowercase.
    attributeid = models.IntegerField(primary_key=True, db_column='attributeID') # Field name made lowercase.
    valueint = models.IntegerField(null=True, db_column='valueInt', blank=True) # Field name made lowercase.
    valuefloat = models.FloatField(null=True, db_column='valueFloat', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'dgmTypeAttributes'

class Dgmtypeeffects(models.Model):
    typeid = models.IntegerField(primary_key=True, db_column='typeID') # Field name made lowercase.
    effectid = models.IntegerField(primary_key=True, db_column='effectID') # Field name made lowercase.
    isdefault = models.IntegerField(null=True, db_column='isDefault', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'dgmTypeEffects'
