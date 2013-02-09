from django.db import models

class BlueprintType(models.Model):
    blueprint           = models.OneToOneField("inv.Type", primary_key=True, db_column='blueprintTypeID', parent_link = True)
    parent              = models.OneToOneField("inv.Type", null=True, db_column='parentBlueprintTypeID', blank=True, related_name='+')
    product             = models.OneToOneField("inv.Type", null=True, db_column='productTypeID', blank=True, related_name='productblueprint')
    productiontime      = models.IntegerField(null=True, db_column='productionTime', blank=True)
    techlevel           = models.IntegerField(null=True, db_column='techLevel', blank=True)
    researchproductivitytime = models.IntegerField(null=True, db_column='researchProductivityTime', blank=True)
    researchmaterialtime = models.IntegerField(null=True, db_column='researchMaterialTime', blank=True)
    researchcopytime    = models.IntegerField(null=True, db_column='researchCopyTime', blank=True)
    researchtechtime    = models.IntegerField(null=True, db_column='researchTechTime', blank=True)
    productivitymodifier = models.IntegerField(null=True, db_column='productivityModifier', blank=True)
    materialmodifier    = models.IntegerField(null=True, db_column='materialModifier', blank=True)
    wastefactor         = models.IntegerField(null=True, db_column='wasteFactor', blank=True)
    maxproductionlimit  = models.IntegerField(null=True, db_column='maxProductionLimit', blank=True)

    class Meta:
        db_table        = u'invBlueprintTypes'

class Category(models.Model):
    id                  = models.IntegerField(primary_key=True, db_column='categoryID') # Field name made lowercase.
    name                = models.CharField(max_length=300, db_column='categoryName', blank=True) # Field name made lowercase.
    description         = models.CharField(max_length=9000, blank=True)
    icon                = models.ForeignKey("eve.Icon", null=True, db_column='iconID', blank=True)
    published           = models.NullBooleanField(null=True, blank=True)

    class Meta:
        db_table        = u'invCategories'

class ContrabandType(models.Model):
    faction             = models.ForeignKey("chr.Faction", primary_key=True, db_column='factionID') # Field name made lowercase.
    type                = models.ForeignKey("inv.Type", db_column='typeID') # Field name made lowercase.
    standingloss        = models.FloatField(null=True, db_column='standingLoss', blank=True) # Field name made lowercase.
    confiscateminsec    = models.FloatField(null=True, db_column='confiscateMinSec', blank=True) # Field name made lowercase.
    finebyvalue         = models.FloatField(null=True, db_column='fineByValue', blank=True) # Field name made lowercase.
    attackminsec        = models.FloatField(null=True, db_column='attackMinSec', blank=True) # Field name made lowercase.
    class Meta:
        db_table        = u'invContrabandTypes'

class ControlTowerResourcePurpose(models.Model):
    purpose             = models.IntegerField(primary_key=True)
    text                = models.CharField(max_length=300, db_column='purposeText', blank=True) # Field name made lowercase.
    class Meta:
        db_table        = u'invControlTowerResourcePurposes'

class ControltowerResource(models.Model):
    controltower        = models.ForeignKey("inv.Type", primary_key=True, db_column='controlTowerTypeID') # Field name made lowercase.
    resource            = models.ForeignKey("inv.Type", primary_key=True, db_column='resourceTypeID', related_name='+') # Field name made lowercase.
    purpose             = models.ForeignKey("inv.ControlTowerResourcePurpose", null=True, blank=True)
    quantity            = models.IntegerField(null=True, blank=True)
    minsecuritylevel    = models.FloatField(null=True, db_column='minSecurityLevel', blank=True) # Field name made lowercase.
    factionid           = models.ForeignKey("chr.Faction", null=True, db_column='factionID', blank=True) # Field name made lowercase.
    class Meta:
        db_table        = u'invControlTowerResources'

class Flag(models.Model):
    id                  = models.IntegerField(primary_key=True, db_column='flagID') # Field name made lowercase.
    name                = models.CharField(max_length=600, db_column='flagName', blank=True) # Field name made lowercase.
    text                = models.CharField(max_length=300, db_column='flagText', blank=True) # Field name made lowercase.
    orderid             = models.IntegerField(null=True, db_column='orderID', blank=True) # Field name made lowercase.
    class Meta:
        db_table        = u'invFlags'

class Group(models.Model):
    id                  = models.IntegerField(primary_key=True, db_column='groupID') # Field name made lowercase.
    category            = models.ForeignKey("inv.Category", null=True, db_column='categoryID', blank=True) # Field name made lowercase.
    name                = models.CharField(max_length=300, db_column='groupName', blank=True) # Field name made lowercase.
    description         = models.CharField(max_length=9000, blank=True)
    icon                = models.ForeignKey("eve.Icon", null=True, db_column='iconID', blank=True)
    usebaseprice        = models.IntegerField(null=True, db_column='useBasePrice', blank=True) # Field name made lowercase.
    allowmanufacture    = models.IntegerField(null=True, db_column='allowManufacture', blank=True) # Field name made lowercase.
    allowrecycler       = models.IntegerField(null=True, db_column='allowRecycler', blank=True) # Field name made lowercase.
    anchored            = models.IntegerField(null=True, blank=True)
    anchorable          = models.IntegerField(null=True, blank=True)
    fittablenonsingleton = models.IntegerField(null=True, db_column='fittableNonSingleton', blank=True) # Field name made lowercase.
    published           = models.NullBooleanField(null=True, blank=True)
    class Meta:
        db_table        = u'invGroups'

class Item(models.Model):
    id                  = models.BigIntegerField(primary_key=True, db_column='itemID') # Field name made lowercase.
    type                = models.ForeignKey("Type", db_column='typeID') # Field name made lowercase.
    ownerid             = models.IntegerField(db_column='ownerID') # Field name made lowercase.
    location            = models.ForeignKey("self", db_column='locationID') # Field name made lowercase.
    flag                = models.ForeignKey("Flag", db_column='flagID') # Field name made lowercase.
    quantity            = models.IntegerField()
    class Meta:
        db_table        = u'invItems'

class MarketGroup(models.Model):
    id                  = models.IntegerField(primary_key=True, db_column='marketGroupID') # Field name made lowercase.
    parent              = models.ForeignKey("self", null=True, db_column='parentGroupID', blank=True) # Field name made lowercase.
    name                = models.CharField(max_length=300, db_column='marketGroupName', blank=True) # Field name made lowercase.
    description         = models.CharField(max_length=9000, blank=True)
    icon                = models.ForeignKey("eve.Icon", null=True, db_column='iconID', blank=True)
    hastypes            = models.IntegerField(null=True, db_column='hasTypes', blank=True) # Field name made lowercase.
    class Meta:
        db_table        = u'invMarketGroups'

class MetaGroup(models.Model):
    id                  = models.IntegerField(primary_key=True, db_column='metaGroupID') # Field name made lowercase.
    name                = models.CharField(max_length=300, db_column='metaGroupName', blank=True) # Field name made lowercase.
    description         = models.CharField(max_length=3000, blank=True)
    icon                = models.ForeignKey("eve.Icon", null=True, db_column='iconID', blank=True)
    class Meta:
        db_table        = u'invMetaGroups'

class MetaType(models.Model):
    type                = models.ForeignKey("inv.Type", primary_key=True, db_column='typeID', related_name='meta_types') # Field name made lowercase.
    parent              = models.ForeignKey("inv.Type", null=True, db_column='parentTypeID', blank=True, related_name='+') # Field name made lowercase.
    group               = models.ForeignKey("inv.MetaGroup", null=True, db_column='metaGroupID', blank=True) # Field name made lowercase.
    class Meta:
        db_table        = u'invMetaTypes'

class Name(models.Model):
    item                = models.ForeignKey("inv.Item", primary_key=True, db_column='itemID') # Field name made lowercase.
    name                = models.CharField(max_length=600, db_column='itemName') # Field name made lowercase.
    class Meta:
        db_table        = u'invNames'

class Position(models.Model):
    item                = models.ForeignKey("inv.Item", primary_key=True, db_column='itemID') # Field name made lowercase.
    x                   = models.FloatField()
    y                   = models.FloatField()
    z                   = models.FloatField()
    yaw                 = models.FloatField(null=True, blank=True)
    pitch               = models.FloatField(null=True, blank=True)
    roll                = models.FloatField(null=True, blank=True)
    class Meta:
        db_table        = u'invPositions'

class TypeMaterial(models.Model):
    type                = models.ForeignKey("inv.Type", primary_key=True, db_column='typeID', related_name='+') # Field name made lowercase.
    material            = models.ForeignKey("inv.Type", primary_key=True, db_column='materialTypeID', related_name='type_material_materials') # Field name made lowercase.
    quantity            = models.IntegerField()
    class Meta:
        db_table        = u'invTypeMaterials'

class TypeReaction(models.Model):
    reaction            = models.ForeignKey("inv.Type", primary_key=True, db_column='reactionTypeID', related_name='+') # Field name made lowercase.
    input               = models.IntegerField(primary_key=True)
    type                = models.ForeignKey("inv.Type", primary_key=True, db_column='typeID', related_name='+') # Field name made lowercase.
    quantity            = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table        = u'invTypeReactions'

class Type(models.Model):
    id                  = models.AutoField(primary_key=True, db_column='typeID') # Field name made lowercase.
    group               = models.ForeignKey("inv.Group", null=True, db_column='groupID', blank=True) # Field name made lowercase.
    typename            = models.CharField(max_length=300, db_column='typeName', blank=True) # Field name made lowercase.
    description         = models.CharField(max_length=9000, blank=True)
    mass                = models.FloatField(null=True, blank=True)
    volume              = models.FloatField(null=True, blank=True)
    capacity            = models.FloatField(null=True, blank=True)
    portionsize         = models.IntegerField(null=True, db_column='portionSize', blank=True) # Field name made lowercase.
    raceid              = models.IntegerField(null=True, db_column='raceID', blank=True) # Field name made lowercase.
    baseprice           = models.DecimalField(decimal_places=4, null=True, max_digits=21, db_column='basePrice', blank=True) # Field name made lowercase.
    published           = models.IntegerField(null=True, blank=True)
    marketgroup         = models.ForeignKey("inv.MarketGroup", null=True, db_column='marketGroupID', blank=True) # Field name made lowercase.
    chanceofduplicating = models.FloatField(null=True, db_column='chanceOfDuplicating', blank=True) # Field name made lowercase.
    class Meta:
        db_table        = u'invTypes'

class UniqueName(models.Model):
    itemid              = models.IntegerField(primary_key=True, db_column='itemID') # Field name made lowercase.
    itemname            = models.CharField(max_length=600, db_column='itemName') # Field name made lowercase.
    groupid             = models.IntegerField(null=True, db_column='groupID', blank=True) # Field name made lowercase.
    class Meta:
        db_table        = u'invUniqueNames'