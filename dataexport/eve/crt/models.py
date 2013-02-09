from django.db import models

class Crtcategories(models.Model):
    categoryid = models.IntegerField(primary_key=True, db_column='categoryID') # Field name made lowercase.
    description = models.CharField(max_length=1500, blank=True)
    categoryname = models.CharField(max_length=768, db_column='categoryName', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'crtCategories'

class Crtcertificates(models.Model):
    certificateid = models.IntegerField(primary_key=True, db_column='certificateID') # Field name made lowercase.
    categoryid = models.IntegerField(null=True, db_column='categoryID', blank=True) # Field name made lowercase.
    classid = models.IntegerField(null=True, db_column='classID', blank=True) # Field name made lowercase.
    grade = models.IntegerField(null=True, blank=True)
    corpid = models.IntegerField(null=True, db_column='corpID', blank=True) # Field name made lowercase.
    icon = models.ForeignKey("eve.Icon", null=True, db_column='iconID', blank=True)
    description = models.CharField(max_length=1500, blank=True)
    class Meta:
        db_table = u'crtCertificates'

class Crtclasses(models.Model):
    classid = models.IntegerField(primary_key=True, db_column='classID') # Field name made lowercase.
    description = models.CharField(max_length=1500, blank=True)
    classname = models.CharField(max_length=768, db_column='className', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'crtClasses'

class Crtrecommendations(models.Model):
    recommendationid = models.IntegerField(primary_key=True, db_column='recommendationID') # Field name made lowercase.
    shiptypeid = models.IntegerField(null=True, db_column='shipTypeID', blank=True) # Field name made lowercase.
    certificateid = models.IntegerField(null=True, db_column='certificateID', blank=True) # Field name made lowercase.
    recommendationlevel = models.IntegerField(db_column='recommendationLevel') # Field name made lowercase.
    class Meta:
        db_table = u'crtRecommendations'

class Crtrelationships(models.Model):
    relationshipid = models.IntegerField(primary_key=True, db_column='relationshipID') # Field name made lowercase.
    parentid = models.IntegerField(null=True, db_column='parentID', blank=True) # Field name made lowercase.
    parenttypeid = models.IntegerField(null=True, db_column='parentTypeID', blank=True) # Field name made lowercase.
    parentlevel = models.IntegerField(null=True, db_column='parentLevel', blank=True) # Field name made lowercase.
    childid = models.IntegerField(null=True, db_column='childID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'crtRelationships'