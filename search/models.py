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
        #set to false since the table already exsisted
        managed = False
        db_table = 'passengers'