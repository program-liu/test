# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

import random

class Health(models.Model):
    xiaoqu = models.CharField(max_length=255, blank=True, null=True)
    dlou_id = models.CharField(db_column='Dlou_id', max_length=10)  # Field name made lowercase.
    dno_id = models.CharField(db_column='Dno_id', unique=True, max_length=10)  # Field name made lowercase.
    dws = models.CharField(db_column='Dws', max_length=10)  # Field name made lowercase.

    class Meta:
     
        db_table = 'health'


class Notice(models.Model):
    n_tag = models.CharField(db_column='N_tag', primary_key=True, max_length=255)  # Field name made lowercase.
    n_time = models.DateTimeField(db_column='N_time', blank=True, null=True)  # Field name made lowercase.
    n_content = models.CharField(db_column='N_content', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
     
        db_table = 'notice'


class Service(models.Model):
    dlou_id = models.CharField(db_column='Dlou_id', max_length=10)  # Field name made lowercase.
    dno_id = models.CharField(db_column='Dno_id', max_length=10)  # Field name made lowercase.
    dwx = models.CharField(db_column='Dwx', max_length=100)  # Field name made lowercase.
    dsun = models.CharField(db_column='Dsun', max_length=255)  # Field name made lowercase.

    class Meta:
     
        db_table = 'service'


class User(models.Model):
    uno = models.CharField(primary_key=True, max_length=255)
    xiaoqu = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=225)
    usex = models.CharField(max_length=4, blank=True, null=True)
    password = models.CharField(max_length=225, blank=True, null=True)
    password1 = models.CharField(max_length=225, blank=True, null=True)
    ulou = models.CharField(max_length=225, blank=True, null=True)
    uln = models.CharField(max_length=225, blank=True, null=True)
    uphone = models.CharField(max_length=255, blank=True, null=True)
    flag = models.IntegerField()

    class Meta:
    
        db_table = 'user'


class Water(models.Model):
    dlou_id = models.CharField(db_column='Dlou_id', max_length=10)  # Field name made lowercase.
    xiaoqu = models.CharField(max_length=225, blank=True, null=True)
    dno_id = models.CharField(db_column='Dno_id', max_length=10)  # Field name made lowercase.
    wwt = models.CharField(db_column='Wwt', max_length=10, blank=True, null=True)  # Field name made lowercase.
    wdt = models.CharField(db_column='Wdt', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'water'

    
