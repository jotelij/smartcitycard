from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.gis.db.models import PointField
from cities.models import (
    BaseCountry,
    BaseCity,
    Place,
    SlugModel,
    unicode_func,
    SET_NULL_OR_CASCADE,
    BaseDistrict,
)
import swapper


class SmartCountry(BaseCountry, models.Model):
    more_data = models.TextField()

    class Meta(BaseCountry.Meta):
        verbose_name = _("Country")
        verbose_name_plural = _("Countries")
        # swappable = swapper.swappable_setting("cities", "Country")


class SmartCity(BaseCity, models.Model):
    more_data = models.TextField()

    class Meta(BaseCity.Meta):
        verbose_name = _("City")
        verbose_name_plural = _("Cities")
        # swappable = swapper.swappable_setting("cities", "City")


class SmartDistrict(BaseDistrict, models.Model):
    more_data = models.TextField()

    class Meta(BaseDistrict.Meta):
        verbose_name_plural = _("Subcities")
        verbose_name = _("Subcity")
        # swappable = swapper.swappable_setting("cities", "District")


class Woreda(Place, SlugModel):
    slug_contains_id = True

    name_std = models.CharField(
        max_length=200, db_index=True, verbose_name="standard name"
    )
    location = PointField()
    population = models.IntegerField()
    city = models.ForeignKey(
        swapper.get_model_name("cities", "City"),
        related_name="woredas",
        on_delete=SET_NULL_OR_CASCADE,
    )
    district = models.ForeignKey(
        swapper.get_model_name("cities", "District"),
        related_name="woredas",
        on_delete=SET_NULL_OR_CASCADE,
    )

    class Meta:
        unique_together = (("city", "district", "name"),)

    @property
    def parent(self):
        return self.district

    def slugify(self):
        if self.id:
            return "{}-{}".format(self.id, unicode_func(self.name))
        return None


class Kebele(Place, SlugModel):
    slug_contains_id = True

    name_std = models.CharField(
        max_length=200, db_index=True, verbose_name="standard name"
    )
    location = PointField()
    population = models.IntegerField()
    city = models.ForeignKey(
        swapper.get_model_name("cities", "City"),
        related_name="kebeles",
        on_delete=SET_NULL_OR_CASCADE,
    )
    district = models.ForeignKey(
        swapper.get_model_name("cities", "District"),
        related_name="kebeles",
        on_delete=SET_NULL_OR_CASCADE,
    )
    woreda = models.ForeignKey(
        Woreda,
        related_name="kebeles",
        on_delete=SET_NULL_OR_CASCADE,
    )

    class Meta:
        unique_together = (("city", "district", "woreda", "name"),)

    @property
    def parent(self):
        return self.woreda

    def slugify(self):
        if self.id:
            return "{}-{}".format(self.id, unicode_func(self.name))
        return None


class House(Place):
    location = PointField()
    city = models.ForeignKey(
        swapper.get_model_name("cities", "City"),
        related_name="houses",
        on_delete=SET_NULL_OR_CASCADE,
    )
    district = models.ForeignKey(
        swapper.get_model_name("cities", "District"),
        related_name="houses",
        on_delete=SET_NULL_OR_CASCADE,
    )
    woreda = models.ForeignKey(
        Woreda,
        related_name="houses",
        on_delete=SET_NULL_OR_CASCADE,
    )
    kebele = models.ForeignKey(
        Kebele,
        related_name="houses",
        on_delete=SET_NULL_OR_CASCADE,
    )

    class Meta:
        unique_together = (("district", "woreda", "kebele", "name"),)
