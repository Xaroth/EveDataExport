from django.db import models

class Category(models.Model):
    id                  = models.IntegerField(primary_key=True, db_column='categoryID') # Field name made lowercase.
    description         = models.CharField(max_length=1500, blank=True)
    name                = models.CharField(max_length=768, db_column='categoryName', blank=True) # Field name made lowercase.
    class Meta:
        db_table        = u'crtCategories'

class Certificate(models.Model):
    id                  = models.IntegerField(primary_key=True, db_column='certificateID') # Field name made lowercase.
    category            = models.ForeignKey("crt.Category", null=True, db_column='categoryID', blank=True) # Field name made lowercase.
    classid             = models.ForeignKey("crt.Class", null=True, db_column='classID', blank=True) # Field name made lowercase.
    grade               = models.IntegerField(null=True, blank=True)
    corpid              = models.ForeignKey("crp.NPCCorporation", null=True, db_column='corpID', blank=True) # Field name made lowercase.
    icon                = models.ForeignKey("eve.Icon", null=True, db_column='iconID', blank=True)
    description         = models.CharField(max_length=1500, blank=True)
    class Meta:
        db_table        = u'crtCertificates'

class Class(models.Model):
    id                  = models.IntegerField(primary_key=True, db_column='classID') # Field name made lowercase.
    description         = models.CharField(max_length=1500, blank=True)
    name                = models.CharField(max_length=768, db_column='className', blank=True) # Field name made lowercase.
    class Meta:
        db_table        = u'crtClasses'

class Recommendation(models.Model):
    id                  = models.IntegerField(primary_key=True, db_column='recommendationID') # Field name made lowercase.
    shiptype            = models.ForeignKey("inv.Type", null=True, db_column='shipTypeID', blank=True) # Field name made lowercase.
    certificate         = models.ForeignKey("crt.Certificate", null=True, db_column='certificateID', blank=True) # Field name made lowercase.
    recommendationlevel = models.IntegerField(db_column='recommendationLevel') # Field name made lowercase.
    class Meta:
        db_table = u'crtRecommendations'

class Relationship(models.Model):
    id                  = models.IntegerField(primary_key=True, db_column='relationshipID') # Field name made lowercase.
    parent              = models.ForeignKey("crt.Certificate", null=True, db_column='parentID', blank=True, related_name='relationships') # Field name made lowercase.
    parenttype          = models.ForeignKey("inv.Type", null=True, db_column='parentTypeID', blank=True) # Field name made lowercase.
    parentlevel         = models.IntegerField(null=True, db_column='parentLevel', blank=True) # Field name made lowercase.
    child               = models.ForeignKey("crt.Certificate", null=True, db_column='childID', blank=True, related_name='+') # Field name made lowercase.
    class Meta:
        db_table        = u'crtRelationships'