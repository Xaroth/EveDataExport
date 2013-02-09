from django.db import models

class AttributeCategory(models.Model):
    id                  = models.IntegerField(primary_key=True, db_column='categoryID') # Field name made lowercase.
    name                = models.CharField(max_length=150, db_column='categoryName', blank=True) # Field name made lowercase.
    description         = models.CharField(max_length=600, db_column='categoryDescription', blank=True) # Field name made lowercase.
    class Meta:
        db_table        = u'dgmAttributeCategories'

class AttributeType(models.Model):
    id                  = models.IntegerField(primary_key=True, db_column='attributeID') # Field name made lowercase.
    name                = models.CharField(max_length=300, db_column='attributeName', blank=True) # Field name made lowercase.
    description         = models.CharField(max_length=3000, blank=True)
    icon                = models.ForeignKey("eve.Icon", null=True, db_column='iconID', blank=True)
    defaultvalue        = models.FloatField(null=True, db_column='defaultValue', blank=True) # Field name made lowercase.
    published           = models.NullBooleanField(null=True, blank=True)
    displayname         = models.CharField(max_length=300, db_column='displayName', blank=True) # Field name made lowercase.
    unitid              = models.ForeignKey("eve.Unit", null=True, db_column='unitID', blank=True) # Field name made lowercase.
    stackable           = models.NullBooleanField(null=True, blank=True)
    highisgood          = models.NullBooleanField(null=True, db_column='highIsGood', blank=True) # Field name made lowercase.
    categoryid          = models.ForeignKey("dgm.AttributeCategory", null=True, db_column='categoryID', blank=True) # Field name made lowercase.
    class Meta:
        db_table        = u'dgmAttributeTypes'

class Effect(models.Model):
    id                  = models.IntegerField(primary_key=True, db_column='effectID') # Field name made lowercase.
    name                = models.CharField(max_length=1200, db_column='effectName', blank=True) # Field name made lowercase.
    category            = models.IntegerField(null=True, db_column='effectCategory', blank=True) # Field name made lowercase.
    preexpression       = models.IntegerField(null=True, db_column='preExpression', blank=True) # Field name made lowercase.
    postexpression      = models.IntegerField(null=True, db_column='postExpression', blank=True) # Field name made lowercase.
    description         = models.CharField(max_length=3000, blank=True)
    guid                = models.CharField(max_length=180, blank=True)
    icon                = models.ForeignKey("eve.Icon", null=True, db_column='iconID', blank=True)
    isoffensive         = models.NullBooleanField(null=True, db_column='isOffensive', blank=True) # Field name made lowercase.
    isassistance        = models.NullBooleanField(null=True, db_column='isAssistance', blank=True) # Field name made lowercase.
    durationattribute   = models.ForeignKey("dgm.AttributeType", null=True, db_column='durationAttributeID', blank=True, related_name='+') # Field name made lowercase.
    trackingspeedattribute = models.ForeignKey("dgm.AttributeType", null=True, db_column='trackingSpeedAttributeID', blank=True, related_name='+') # Field name made lowercase.
    dischargeattribute  = models.ForeignKey("dgm.AttributeType", null=True, db_column='dischargeAttributeID', blank=True, related_name='+') # Field name made lowercase.
    rangeattribute      = models.ForeignKey("dgm.AttributeType", null=True, db_column='rangeAttributeID', blank=True, related_name='+') # Field name made lowercase.
    falloffattribute    = models.ForeignKey("dgm.AttributeType", null=True, db_column='falloffAttributeID', blank=True, related_name='+') # Field name made lowercase.
    disallowautorepeat  = models.NullBooleanField(null=True, db_column='disallowAutoRepeat', blank=True) # Field name made lowercase.
    published           = models.NullBooleanField(null=True, blank=True)
    displayname         = models.CharField(max_length=300, db_column='displayName', blank=True) # Field name made lowercase.
    iswarpsafe          = models.NullBooleanField(null=True, db_column='isWarpSafe', blank=True) # Field name made lowercase.
    rangechance         = models.IntegerField(null=True, db_column='rangeChance', blank=True) # Field name made lowercase.
    electronicchance    = models.IntegerField(null=True, db_column='electronicChance', blank=True) # Field name made lowercase.
    propulsionchance    = models.IntegerField(null=True, db_column='propulsionChance', blank=True) # Field name made lowercase.
    distribution        = models.IntegerField(null=True, blank=True)
    sfxname             = models.CharField(max_length=60, db_column='sfxName', blank=True) # Field name made lowercase.
    npcusagechanceattribute = models.ForeignKey("dgm.AttributeType", null=True, db_column='npcUsageChanceAttributeID', blank=True, related_name='+') # Field name made lowercase.
    npcactivationchanceattribute = models.ForeignKey("dgm.AttributeType", null=True, db_column='npcActivationChanceAttributeID', blank=True, related_name='+') # Field name made lowercase.
    fittingusagechanceattribute = models.ForeignKey("dgm.AttributeType", null=True, db_column='fittingUsageChanceAttributeID', blank=True, related_name='+') # Field name made lowercase.
    class Meta:
        db_table        = u'dgmEffects'

class TypeAttribute(models.Model):
    type                = models.ForeignKey("inv.Type", primary_key=True, db_column='typeID') # Field name made lowercase.
    attribute           = models.ForeignKey("dgm.AttributeType", primary_key=True, db_column='attributeID') # Field name made lowercase.
    valueint            = models.IntegerField(null=True, db_column='valueInt', blank=True) # Field name made lowercase.
    valuefloat          = models.FloatField(null=True, db_column='valueFloat', blank=True) # Field name made lowercase.

    @property
    def value(self):
        return self.valuefloat or self.valueint

    class Meta:
        db_table        = u'dgmTypeAttributes'

class TypeEffect(models.Model):
    type                = models.ForeignKey("inv.Type", primary_key=True, db_column='typeID') # Field name made lowercase.
    effect              = models.ForeignKey("dgm.Effect", primary_key=True, db_column='effectID') # Field name made lowercase.
    isdefault           = models.NullBooleanField(null=True, db_column='isDefault', blank=True) # Field name made lowercase.
    class Meta:
        db_table        = u'dgmTypeEffects'
