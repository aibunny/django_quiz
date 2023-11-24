# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Passengers(models.Model):
    passengerid = models.BigIntegerField(db_column='PassengerId', primary_key=True)  # Field name made lowercase.
    survived = models.TextField(db_column='Survived', blank=True, null=True)  # Field name made lowercase.
    pclass = models.BigIntegerField(db_column='Pclass', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    sex = models.TextField(db_column='Sex', blank=True, null=True)  # Field name made lowercase.
    age = models.FloatField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    sibsp = models.BigIntegerField(db_column='SibSp', blank=True, null=True)  # Field name made lowercase.
    parch = models.TextField(db_column='Parch', blank=True, null=True)  # Field name made lowercase.
    ticket = models.TextField(db_column='Ticket', blank=True, null=True)  # Field name made lowercase.
    fare = models.FloatField(db_column='Fare', blank=True, null=True)  # Field name made lowercase.
    cabin = models.TextField(db_column='Cabin', blank=True, null=True)  # Field name made lowercase.
    embarked = models.TextField(db_column='Embarked', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'passengers'
