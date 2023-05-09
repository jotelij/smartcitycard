from django.db import models
from core.models import BaseSafeModel
from django.utils.translation import gettext_lazy as _
from django.conf import settings
import swapper
from magala.models import House, Kebele


class Occupation(BaseSafeModel):
    name = models.CharField(
        _("Name"),
        max_length=150,
        null=False,
        blank=False,
        help_text=_("Occupation name"),
    )


class Ethinicity(models.Model):
    name = models.TextField(_("Name"))


class Person(BaseSafeModel):
    class Gender(models.TextChoices):
        MALE = "M", "Male"
        FEMALE = "F", "Female"
        UNKNOWN = "U", "Unknow"

    class BloodGroup(models.TextChoices):
        A = "A", "A"
        A_PLUS = "AP", "A+"
        B = "B", "B"
        B_PLUS = "BP", "B+"
        O = "O", "O"
        O_PLUS = "OP", "O+"
        AB = "AB", "AB"
        AB_PLUS = "ABP", "AB+"
        NO_RH = "NRH", "No RH"
        UNK = "UNK", "Unknown"

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        verbose_name=_("Person Account"),
        on_delete=models.CASCADE,
    )
    id_code = models.CharField(_("ID code"), max_length=150)
    name_om = models.CharField(
        _("Afan Oromo Name"),
        max_length=150,
        null=False,
        blank=False,
        help_text=_("Person name in Afan Oromo"),
    )
    father_name_om = models.CharField(
        _("Afan Oromo Father Name"),
        max_length=150,
        null=False,
        blank=False,
        help_text=_("Person father name in Afan Oromo"),
    )
    gfather_name_om = models.CharField(
        _("Afan Oromo Grandfather Name"),
        max_length=150,
        null=False,
        blank=False,
        help_text=_("Person grandfather name in Afan Oromo"),
    )
    name_en = models.CharField(
        _("English First Name"),
        max_length=150,
        null=False,
        blank=False,
        help_text=_("Person first name in English"),
    )
    name_am = models.CharField(
        _("Amharic Name"),
        max_length=150,
        null=False,
        blank=False,
        help_text=_("Person name in Amharic"),
    )
    father_name_am = models.CharField(
        _("Amharic Father Name"),
        max_length=150,
        null=False,
        blank=False,
        help_text=_("Person father name in Amharic"),
    )
    gfather_name_am = models.CharField(
        _("Amharic Grandfather Name"),
        max_length=150,
        null=False,
        blank=False,
        help_text=_("Person grandfather name in Amharic"),
    )
    name_en = models.CharField(
        _("English First Name"),
        max_length=150,
        null=False,
        blank=False,
        help_text=_("Person first name in English"),
    )
    father_name_en = models.CharField(
        _("English Father Name"),
        max_length=150,
        null=False,
        blank=False,
        help_text=_("Person father name in English"),
    )
    gfather_name_en = models.CharField(
        _("English Grandfather Name"),
        max_length=150,
        null=False,
        blank=False,
        help_text=_("Person grandfather name in English"),
    )
    gender = models.CharField(
        _("Gender"),
        choices=Gender.choices,
        max_length=1,
        blank=False,
        null=False,
    )
    birthdate = models.DateField(
        _("Date of Birth"),
        auto_now=False,
        auto_now_add=False,
        blank=False,
        null=False,
    )
    birth_place = models.ForeignKey(
        Kebele,
        related_name="persons",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("Place of birth"),
    )
    blood_group = models.CharField(
        _("Blood Group"),
        choices=BloodGroup.choices,
        default=BloodGroup.UNK,
        max_length=3,
        blank=True,
        null=True,
    )
    nationality = models.ForeignKey(
        swapper.get_model_name("cities", "Country"),
        verbose_name=_("Nationality"),
        related_name="persons",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    ethinicity = models.ForeignKey(
        Ethinicity,
        verbose_name=_("Ethinicity"),
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )


# class PersonCity(BaseSafeModel):
#     person = models.ForeignKey(
#         Person,
#         related_name="kebeles",
#         on_delete=models.CASCADE,
#     )
#     city = models.ForeignKey(
#         swapper.get_model_name("cities", "City"),
#         related_name="person_houses",
#         on_delete=models.CASCADE,
#     )
#     is_current = models.BooleanField(_("Current city?"))


class PersonHouse(BaseSafeModel):
    person = models.ForeignKey(
        Person,
        related_name="person_houses",
        on_delete=models.CASCADE,
        verbose_name=_("The person"),
    )
    house = models.ForeignKey(
        House,
        related_name="person_houses",
        on_delete=models.CASCADE,
        verbose_name=_("Living house"),
    )
    start = models.DateField(
        _("Starting from"),
        auto_now=False,
        auto_now_add=False,
        null=False,
        blank=False,
    )
    end = models.DateField(
        _("Until"),
        auto_now=False,
        auto_now_add=False,
        null=True,
        blank=True,
    )
    is_current = models.BooleanField(
        _("Current house?"), default=True, blank=True, null=False
    )
    is_rent = models.BooleanField(
        _("Is rented?"), default=False, blank=False, null=False
    )
