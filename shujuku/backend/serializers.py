from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import Service,User,Health,Water,Notice



class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model   =  Service
        fields  =  ('dlou_id','dno_id','dwx','dsun')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model   =  User
        fields  =  ('uno','xiaoqu','username','usex','password','ulou','uln','uphone','flag')

class HealthSerializer(serializers.ModelSerializer):
    class Meta:
        model   =  Health
        fields  =  ('xiaoqu','dlou_id','dno_id','dws')

class WaterSerializer(serializers.ModelSerializer):
    class Meta:
        model   =  Water
        fields  =  ('dlou_id','xiaoqu','dno_id','wwt','wdt')

class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model   =  Notice
        fields  =  ('n_tag','n_time','n_content')

class ChangePasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model   =  User
        fields  =  ('uno','password','password1')




