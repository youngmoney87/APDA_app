# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ConversionSheet(models.Model):
    def __str__(self):
        return self.degree_grp

    id = models.FloatField(db_column='ID', primary_key=True)  # Field name made lowercase.
    degree_grp = models.CharField(db_column='Degree_grp', max_length=255)  # Field name made lowercase.
    awlgrp = models.CharField(max_length=255)
    awl = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'Conversion_Sheet'


class SchoolList(models.Model):
    def __str__(self):
        return self.school

    unitid = models.FloatField(db_column='UNITID', primary_key=True)  # Field name made lowercase.
    school = models.CharField(db_column='SCHOOL', max_length=255)  # Field name made lowercase.
    client = models.FloatField(db_column='Client')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'School_list'