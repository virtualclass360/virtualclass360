from rest_framework import serializers
from django.db import models
from .models import *
class Userserilazers(serializers.ModelSerializer):
    class Meta:
        model=Users
        fields= "__all__"

class Planserilazers(serializers.ModelSerializer):
    class Meta:
        model=Plans
        fields= "__all__"


class Intrest_Categoryserilazers(serializers.ModelSerializer):
    class Meta:
        model=Intrest_Category
        fields= "__all__"
class Intrest_Sub_Categoryserilazers(serializers.ModelSerializer):
    class Meta:
        model=Intrest_Sub_Category
        fields= "__all__"
