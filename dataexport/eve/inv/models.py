from django.db import models

class Invblueprinttypes(models.Model):
    blueprinttypeid = models.IntegerField(primary_key=True, db_column='blueprintTypeID') # Field name made lowercase.
    parentblueprinttypeid = models.IntegerField(null=True, db_column='parentBlueprintTypeID', blank=True) # Field name made lowercase.
    producttypeid = models.IntegerField(null=True, db_column='productTypeID', blank=True) # Field name made lowercase.
    productiontime = models.IntegerField(null=True, db_column='productionTime', blank=True) # Field name made lowercase.
    techlevel = models.IntegerField(null=True, db_column='techLevel', blank=True) # Field name made lowercase.
    researchproductivitytime = models.IntegerField(null=True, db_column='researchProductivityTime', blank=True) # Field name made lowercase.
    researchmaterialtime = models.IntegerField(null=True, db_column='researchMaterialTime', blank=True) # Field name made lowercase.
    researchcopytime = models.IntegerField(null=True, db_column='researchCopyTime', blank=True) # Field name made lowercase.
    researchtechtime = models.IntegerField(null=True, db_column='researchTechTime', blank=True) # Field name made lowercase.
    productivitymodifier = models.IntegerField(null=True, db_column='productivityModifier', blank=True) # Field name made lowercase.
    materialmodifier = models.IntegerField(null=True, db_column='materialModifier', blank=True) # Field name made lowercase.
    wastefactor = models.IntegerField(null=True, db_column='wasteFactor', blank=True) # Field name made lowercase.
    maxproductionlimit = models.IntegerField(null=True, db_column='maxProductionLimit', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'invBlueprintTypes'

class Invcategories(models.Model):
    categoryid = models.IntegerField(primary_key=True, db_column='categoryID') # Field name made lowercase.
    categoryname = models.CharField(max_length=300, db_column='categoryName', blank=True) # Field name made lowercase.
    description = models.CharField(max_length=9000, blank=True)
    iconid = models.IntegerField(null=True, db_column='iconID', blank=True) # Field name made lowercase.
    published = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'invCategories'

class Invcontrabandtypes(models.Model):
    factionid = models.IntegerField(primary_key=True, db_column='factionID') # Field name made lowercase.
    typeid = models.IntegerField(db_column='typeID') # Field name made lowercase.
    standingloss = models.FloatField(null=True, db_column='standingLoss', blank=True) # Field name made lowercase.
    confiscateminsec = models.FloatField(null=True, db_column='confiscateMinSec', blank=True) # Field name made lowercase.
    finebyvalue = models.FloatField(null=True, db_column='fineByValue', blank=True) # Field name made lowercase.
    attackminsec = models.FloatField(null=True, db_column='attackMinSec', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'invContrabandTypes'

class Invcontroltowerresourcepurposes(models.Model):
    purpose = models.IntegerField(primary_key=True)
    purposetext = models.CharField(max_length=300, db_column='purposeText', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'invControlTowerResourcePurposes'

class Invcontroltowerresources(models.Model):
    controltowertypeid = models.IntegerField(primary_key=True, db_column='controlTowerTypeID') # Field name made lowercase.
    resourcetypeid = models.IntegerField(primary_key=True, db_column='resourceTypeID') # Field name made lowercase.
    purpose = models.IntegerField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    minsecuritylevel = models.FloatField(null=True, db_column='minSecurityLevel', blank=True) # Field name made lowercase.
    factionid = models.IntegerField(null=True, db_column='factionID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'invControlTowerResources'

class Invflags(models.Model):
    flagid = models.IntegerField(primary_key=True, db_column='flagID') # Field name made lowercase.
    flagname = models.CharField(max_length=600, db_column='flagName', blank=True) # Field name made lowercase.
    flagtext = models.CharField(max_length=300, db_column='flagText', blank=True) # Field name made lowercase.
    orderid = models.IntegerField(null=True, db_column='orderID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'invFlags'

class Invgroups(models.Model):
    groupid = models.IntegerField(primary_key=True, db_column='groupID') # Field name made lowercase.
    categoryid = models.IntegerField(null=True, db_column='categoryID', blank=True) # Field name made lowercase.
    groupname = models.CharField(max_length=300, db_column='groupName', blank=True) # Field name made lowercase.
    description = models.CharField(max_length=9000, blank=True)
    iconid = models.IntegerField(null=True, db_column='iconID', blank=True) # Field name made lowercase.
    usebaseprice = models.IntegerField(null=True, db_column='useBasePrice', blank=True) # Field name made lowercase.
    allowmanufacture = models.IntegerField(null=True, db_column='allowManufacture', blank=True) # Field name made lowercase.
    allowrecycler = models.IntegerField(null=True, db_column='allowRecycler', blank=True) # Field name made lowercase.
    anchored = models.IntegerField(null=True, blank=True)
    anchorable = models.IntegerField(null=True, blank=True)
    fittablenonsingleton = models.IntegerField(null=True, db_column='fittableNonSingleton', blank=True) # Field name made lowercase.
    published = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'invGroups'

class Invitems(models.Model):
    itemid = models.BigIntegerField(primary_key=True, db_column='itemID') # Field name made lowercase.
    typeid = models.IntegerField(db_column='typeID') # Field name made lowercase.
    ownerid = models.IntegerField(db_column='ownerID') # Field name made lowercase.
    locationid = models.BigIntegerField(db_column='locationID') # Field name made lowercase.
    flagid = models.IntegerField(db_column='flagID') # Field name made lowercase.
    quantity = models.IntegerField()
    class Meta:
        db_table = u'invItems'

class Invmarketgroups(models.Model):
    marketgroupid = models.IntegerField(primary_key=True, db_column='marketGroupID') # Field name made lowercase.
    parentgroupid = models.IntegerField(null=True, db_column='parentGroupID', blank=True) # Field name made lowercase.
    marketgroupname = models.CharField(max_length=300, db_column='marketGroupName', blank=True) # Field name made lowercase.
    description = models.CharField(max_length=9000, blank=True)
    iconid = models.IntegerField(null=True, db_column='iconID', blank=True) # Field name made lowercase.
    hastypes = models.IntegerField(null=True, db_column='hasTypes', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'invMarketGroups'

class Invmetagroups(models.Model):
    metagroupid = models.IntegerField(primary_key=True, db_column='metaGroupID') # Field name made lowercase.
    metagroupname = models.CharField(max_length=300, db_column='metaGroupName', blank=True) # Field name made lowercase.
    description = models.CharField(max_length=3000, blank=True)
    iconid = models.IntegerField(null=True, db_column='iconID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'invMetaGroups'

class Invmetatypes(models.Model):
    typeid = models.IntegerField(primary_key=True, db_column='typeID') # Field name made lowercase.
    parenttypeid = models.IntegerField(null=True, db_column='parentTypeID', blank=True) # Field name made lowercase.
    metagroupid = models.IntegerField(null=True, db_column='metaGroupID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'invMetaTypes'

class Invnames(models.Model):
    itemid = models.BigIntegerField(primary_key=True, db_column='itemID') # Field name made lowercase.
    itemname = models.CharField(max_length=600, db_column='itemName') # Field name made lowercase.
    class Meta:
        db_table = u'invNames'

class Invpositions(models.Model):
    itemid = models.BigIntegerField(primary_key=True, db_column='itemID') # Field name made lowercase.
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()
    yaw = models.FloatField(null=True, blank=True)
    pitch = models.FloatField(null=True, blank=True)
    roll = models.FloatField(null=True, blank=True)
    class Meta:
        db_table = u'invPositions'

class Invtypematerials(models.Model):
    typeid = models.IntegerField(primary_key=True, db_column='typeID') # Field name made lowercase.
    materialtypeid = models.IntegerField(primary_key=True, db_column='materialTypeID') # Field name made lowercase.
    quantity = models.IntegerField()
    class Meta:
        db_table = u'invTypeMaterials'

class Invtypereactions(models.Model):
    reactiontypeid = models.IntegerField(primary_key=True, db_column='reactionTypeID') # Field name made lowercase.
    input = models.IntegerField(primary_key=True)
    typeid = models.IntegerField(primary_key=True, db_column='typeID') # Field name made lowercase.
    quantity = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'invTypeReactions'

class Invtypes(models.Model):
    typeid = models.IntegerField(primary_key=True, db_column='typeID') # Field name made lowercase.
    groupid = models.IntegerField(null=True, db_column='groupID', blank=True) # Field name made lowercase.
    typename = models.CharField(max_length=300, db_column='typeName', blank=True) # Field name made lowercase.
    description = models.CharField(max_length=9000, blank=True)
    mass = models.FloatField(null=True, blank=True)
    volume = models.FloatField(null=True, blank=True)
    capacity = models.FloatField(null=True, blank=True)
    portionsize = models.IntegerField(null=True, db_column='portionSize', blank=True) # Field name made lowercase.
    raceid = models.IntegerField(null=True, db_column='raceID', blank=True) # Field name made lowercase.
    baseprice = models.DecimalField(decimal_places=4, null=True, max_digits=21, db_column='basePrice', blank=True) # Field name made lowercase.
    published = models.IntegerField(null=True, blank=True)
    marketgroupid = models.IntegerField(null=True, db_column='marketGroupID', blank=True) # Field name made lowercase.
    chanceofduplicating = models.FloatField(null=True, db_column='chanceOfDuplicating', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'invTypes'

class Invuniquenames(models.Model):
    itemid = models.IntegerField(primary_key=True, db_column='itemID') # Field name made lowercase.
    itemname = models.CharField(max_length=600, db_column='itemName') # Field name made lowercase.
    groupid = models.IntegerField(null=True, db_column='groupID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'invUniqueNames'