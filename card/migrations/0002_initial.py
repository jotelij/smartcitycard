# Generated by Django 4.1.7 on 2023-03-17 16:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.CITIES_COUNTRY_MODEL),
        ("magala", "0001_initial"),
        ("card", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="personhouse",
            name="house",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="person_houses",
                to="magala.house",
                verbose_name="Living house",
            ),
        ),
        migrations.AddField(
            model_name="personhouse",
            name="person",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="person_houses",
                to="card.person",
                verbose_name="The person",
            ),
        ),
        migrations.AddField(
            model_name="personhouse",
            name="updated_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="%(app_label)s_%(class)s_updated_by",
                related_query_name="updated_by_%(app_label)s_%(class)ss",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Updated by",
            ),
        ),
        migrations.AddField(
            model_name="person",
            name="birth_place",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="persons",
                to="magala.kebele",
                verbose_name="Place of birth",
            ),
        ),
        migrations.AddField(
            model_name="person",
            name="created_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="%(app_label)s_%(class)s_created_by",
                related_query_name="created_by_%(app_label)s_%(class)ss",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Created by",
            ),
        ),
        migrations.AddField(
            model_name="person",
            name="ethinicity",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="card.ethinicity",
                verbose_name="Ethinicity",
            ),
        ),
        migrations.AddField(
            model_name="person",
            name="nationality",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="persons",
                to=settings.CITIES_COUNTRY_MODEL,
                verbose_name="Nationality",
            ),
        ),
        migrations.AddField(
            model_name="person",
            name="updated_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="%(app_label)s_%(class)s_updated_by",
                related_query_name="updated_by_%(app_label)s_%(class)ss",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Updated by",
            ),
        ),
        migrations.AddField(
            model_name="person",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Person Account",
            ),
        ),
        migrations.AddField(
            model_name="occupation",
            name="created_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="%(app_label)s_%(class)s_created_by",
                related_query_name="created_by_%(app_label)s_%(class)ss",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Created by",
            ),
        ),
        migrations.AddField(
            model_name="occupation",
            name="updated_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="%(app_label)s_%(class)s_updated_by",
                related_query_name="updated_by_%(app_label)s_%(class)ss",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Updated by",
            ),
        ),
    ]