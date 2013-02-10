from xml.dom import minidom
import httplib

from django.db import models
from django.core.cache import cache

from eve.tools import LoggableObject

class BlueprintType(models.Model, LoggableObject):
    type                = models.OneToOneField("inv.Type", primary_key=True, db_column='blueprintTypeID', related_name='blueprint', parent_link = True)
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

    def __str__(self):
        return self.type.name

    def getBaseInventionChance(self):
        """
        Returns the base invention chance for this blueprint.

        Requires blueprint to be for a T2 product.
        check for base chance might be somewhat outdated, there might be a better way of checking.
        """
        chance = getattr(self, '_getBaseInventionChance', None)
        if chance:
            return chance
        chance = 0.40
        p = self.product
        if not p.attributes.techLevel == 1:
            return 0.00
        if p.group.category.name == "Ship":
            group = p.group.name
            if group in ['Frigate', 'Freighter', 'Destroyer'] or p.name == 'Skiff':
                chance = 0.30
            elif group in ['Cruiser', 'Industrial'] or p.name == 'Mackinaw':
                chance = 0.25
            elif group in ['Battlecruiser', 'Battleship'] or p.name == 'Hulk':
                chance = 0.2
            else:
                chance = 0
        self._getBaseInventionChance = chance
        return chance

    def calculateInventionChance(self, encryption_skill = 5, primary_dc_skill = 5, secondary_dc_skill = 5, meta_item = None, decryptor_mod = 1.0):
        meta_level = 0
        if not meta_item == None:
            meta_level = meta_item.attributedict.get('metaLevel', 0)
        base = self.getBaseInventionChance()
        return min(1, 
                     base * (1 + (encryption_skill * 0.01)) 
                          * (1 + (0.02* (primary_dc_skill + secondary_dc_skill)) 
                               * (5 / (5 - meta_level))) 
                          * decryptor_mod )

    def getInventionBlueprints(self):
        return [x.type.productblueprint for x in MetaType.objects.filter(parent = self.product, group__id = 2)]

    def applyAdjustedResearchTime(self, base, skill = 0, slot = 1.0, implant = 1.0):
        return base * ( 1 - ( 0.05 * float(skill))) * float(slot) * float(implant)

    def getAdjustedCopyTime(self, skill = 0, slot = 1.0, implant = 1.0):
        return self.applyAdjustedResearchTime(self.researchcopytime, skill, slot, implant)

    def getAdjustedMaterialTime(self, skill = 0, slot = 1.0, implant = 1.0):
        return self.applyAdjustedResearchTime(self.researchmaterialtime, skill, slot, implant)

    def getAdjustedProductivityTime(self, skill = 0, slot = 1.0, implant = 1.0):
        return self.applyAdjustedResearchTime(self.researchproductivitytime, skill, slot, implant)

    def getAdjustedProductionTime(self, industry = 5, slot = 1.0, implant = 1.0, pe_level = 0):
        ptm = ( 1 - (0.04 * float(industry))) * float(implant) * float(slot)
        pemod = 1
        if pe_level >= 0:
            pemod = (float(pe_level) / (1+float(pe_level)))
        else:
            pemod = (float(pe_level) - 1)
        return float(self.productiontime) * (1 - (float(self.productivitymodifier) / float(self.productiontime) ) * (pemod)) * ptm

    def getBaseMaterials(self):
        bom = getattr(self, '_getBaseMaterials', None)
        if not bom:
            bom = self._getBaseMaterials = dict(self.product.type_materials.exclude(material__group__category__name = "Skill").values_list('material', 'quantity'))
        return bom

    def getRamMaterials(self, activity="Manufacturing"):
        bom = getattr(self, '_getRamMaterials_%s' % activity, None)
        if not bom:            
            bom = dict([(x.requiredtype_id, x) for x in self.type.typerequirement_set.filter(activity__name=activity).exclude(requiredtype__group__category__name = "Skill")])
            setattr(self, '_getRamMaterials_%s' % activity, bom)
        return bom

    def applyWasteQuantity(self, bom_item, me_level):
        bom_item['waste'] = self.getWasteAmount(bom_item['base'], me_level)
        bom_item['total'] = bom_item['base'] + bom_item['ram'] + bom_item['waste']
        return bom_item

    def applyCost(self, item, bom_item):
        price = item.getPrice()
        bom_item['buy'] = price['buy']
        bom_item['sell'] = price['sell']
        bom_item['total_buy'] = bom_item['total'] * price['buy']
        bom_item['total_sell'] = bom_item['total'] * price['sell']
        return bom_item

    def getWasteAmount(self, quantity, me_level):
        waste = round(self.wastefactor, 2)
        me = round(me_level, 2)
        if quantity == 0:
            return 0
        q = round(float(quantity), 2)
        if me_level >= 0:
            return int(round(q * (waste / 100) * ( 1 / (me + 1)), 0))
        else:
            return int(round(q * (waste / 100) * (1 - me), 0))

    def getBillOfMaterials(self, me_level = 0, include_cost = False):
        self.log.debug("Getting Bill of Materials for %s" % str(self))
        ram = self.getRamMaterials()
        base = self.getBaseMaterials()
        exclude = []
        itemlist = list(set(ram.keys() + base.keys()))
        bom = dict([(x, {'damage': 1.0, 'waste': 0, 'recycle': True, 'base': 0, 'ram': 0, 'waste': 0, 'total': 0}) for x in itemlist])
        for item, quantity in base.items():
            self.log.debug("ItemID: %s :: %s" % (item, quantity))
            bom[item]['base'] = quantity

        for item, data in ram.items():
            self.log.debug("ItemID: %s :: %s @ %s%s" % (item, data.quantity, data.damageperjob, ", recycles" if data.recycle else ""))
            bom[item]['ram'] = data.quantity
            bom[item]['damage'] = data.damageperjob
            bom[item]['recycle'] = data.recycle == True
            if data.recycle:
                exclude.append(item)
        exclude = BlueprintType.objects.filter(product__in = exclude)
        for item in exclude:
            self.log.debug("Excluding: %s" % item)
            exclude_bom = item.getBaseMaterials()
            for item, quantity in exclude_bom.items():
                try:
                    self.log.debug("Exluding ItemID: %s :: %s"  % (item, quantity))
                    bom[item]['base'] -= quantity
                except KeyError:
                    pass
        items = dict( [(x.pk, x) for x in Type.objects.filter(id__in = bom.keys()) ] )
        calc = lambda x,y: self.applyWasteQuantity(y, me_level)
        if include_cost:
            calc = lambda x,y: self.applyCost(x, self.applyWasteQuantity(y, me_level))
        bom = dict( [ (items.get(x, None), calc(items.get(x, None),y)) for x,y in bom.items() if y['ram'] + y['base'] > 0 ] )

        return bom




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
    type                = models.ForeignKey("inv.Type", primary_key=True, db_column='typeID', related_name='type_materials') # Field name made lowercase.
    material            = models.ForeignKey("inv.Type", primary_key=True, db_column='materialTypeID', related_name='type_material_materials') # Field name made lowercase.
    quantity            = models.IntegerField()

    def __str__(self):
        return "%s * %s"  % (self.material.name, self.quantity)
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
    name                = models.CharField(max_length=300, db_column='typeName', blank=True) # Field name made lowercase.
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

    def __str__(self):
        return self.name

    _attributes      = None
    _attributedict   = None
    @property
    def attributes(self):
        if self._attributes == None:
            self._attributes = type('attributes', (object,), self.attributedict) 
        return self._attributes

    @property
    def attributedict(self):
        if self._attributedict == None:
            attribs = self.attribute_set.select_related('attribute').all()
            self._attributedict = dict([(x.attribute.name, x.value) for x in attribs])
        return self._attributedict


    class Meta:
        db_table        = u'invTypes'

    def getPrice(self):
        res = cache.get("invTypes.price." + str(self.id))
        if res != None: return res

        conn = httplib.HTTPConnection("api.eve-central.com")
        conn.request("GET", "/api/marketstat?usesystem=30000142&typeid=" + str(self.id))
        res = conn.getresponse()
        reply = res.read()
        conn.close()

        dom = minidom.parseString(reply)
        item = dom.getElementsByTagName("buy")
        buy = float(item[0].getElementsByTagName("percentile")[0].childNodes[0].nodeValue)
        item = dom.getElementsByTagName("sell")
        sell = float(item[0].getElementsByTagName("percentile")[0].childNodes[0].nodeValue)

        ret = { "buy": buy, "sell": sell }

        cache.set("invTypes.price." + str(self.id), ret, 3600)
        return ret


class UniqueName(models.Model):
    itemid              = models.IntegerField(primary_key=True, db_column='itemID') # Field name made lowercase.
    itemname            = models.CharField(max_length=600, db_column='itemName') # Field name made lowercase.
    groupid             = models.IntegerField(null=True, db_column='groupID', blank=True) # Field name made lowercase.
    class Meta:
        db_table        = u'invUniqueNames'
