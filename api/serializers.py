from django.contrib.auth.models import User, Group
from rest_framework import serializers
from magala.models import SmartCountry
from card.models import Person


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = SmartCountry


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
