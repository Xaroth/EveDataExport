from django.db import models

class Translationtables(models.Model):
    sourcetable = models.CharField(max_length=600, primary_key=True, db_column='sourceTable') # Field name made lowercase.
    destinationtable = models.CharField(max_length=600, db_column='destinationTable', blank=True) # Field name made lowercase.
    translatedkey = models.CharField(max_length=600, primary_key=True, db_column='translatedKey') # Field name made lowercase.
    tcgroupid = models.IntegerField(null=True, db_column='tcGroupID', blank=True) # Field name made lowercase.
    tcid = models.IntegerField(null=True, db_column='tcID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'translationTables'

class Trntranslationcolumns(models.Model):
    tcgroupid = models.IntegerField(null=True, db_column='tcGroupID', blank=True) # Field name made lowercase.
    tcid = models.IntegerField(primary_key=True, db_column='tcID') # Field name made lowercase.
    tablename = models.CharField(max_length=768, db_column='tableName') # Field name made lowercase.
    columnname = models.CharField(max_length=384, db_column='columnName') # Field name made lowercase.
    masterid = models.CharField(max_length=384, db_column='masterID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'trnTranslationColumns'

class Trntranslationlanguages(models.Model):
    numericlanguageid = models.IntegerField(primary_key=True, db_column='numericLanguageID') # Field name made lowercase.
    languageid = models.CharField(max_length=150, db_column='languageID', blank=True) # Field name made lowercase.
    languagename = models.CharField(max_length=600, db_column='languageName', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'trnTranslationLanguages'

class Trntranslations(models.Model):
    tcid = models.IntegerField(primary_key=True, db_column='tcID') # Field name made lowercase.
    keyid = models.IntegerField(primary_key=True, db_column='keyID') # Field name made lowercase.
    languageid = models.CharField(max_length=150, primary_key=True, db_column='languageID') # Field name made lowercase.
    text = models.TextField(blank=True)
    class Meta:
        db_table = u'trnTranslations'