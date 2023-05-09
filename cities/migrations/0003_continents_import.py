# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-29 19:49
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion

import swapper

from ..util import add_continents as util_add_continents


def get_model(apps, name):
    model_tuple = swapper.split(swapper.get_model_name("cities", name))
    return apps.get_model(*model_tuple)


def add_continents(apps, schema_editor):
    util_add_continents(get_model(apps, "Continent"))


def rm_continents(apps, schema_editor):
    # The table is going to be nuked anyway, we just don't want RunPython()
    # to throw an exception on backwards migrations
    pass


def add_continent_fks(apps, schema_editor):
    Country = get_model(apps, "Country")
    Continent = get_model(apps, "Continent")

    for continent in Continent.objects.all():
        Country.objects.filter(continent_code=continent.code).update(
            continent=continent
        )


def rm_continent_fks(apps, schema_editor):
    Country = get_model(apps, "Country")
    Continent = get_model(apps, "Continent")

    for continent in Continent.objects.all():
        Country.objects.filter(continent=continent).update(
            continent_code=continent.code
        )


class Migration(migrations.Migration):
    dependencies = [
        ("cities", "0002_initial"),
        swapper.dependency("cities", "Country"),
    ]

    operations = [
        migrations.RunPython(add_continents, rm_continents),
        # migrations.RunPython(add_continent_fks, rm_continent_fks),
    ]