from django.contrib import admin
from .models import SmartCity, SmartCountry, SmartDistrict


# Register your models here.
class SmartCitiesAdmin(admin.ModelAdmin):
    raw_id_fields = ["alt_names"]


class SmartCountryAdmin(SmartCitiesAdmin):
    list_display = [
        "name",
        "code",
        "code3",
        "tld",
        "phone",
        "continent",
        "area",
        "population",
    ]
    search_fields = ["name", "code", "code3", "tld", "phone"]
    filter_horizontal = ["neighbours"]


class SmartCityAdmin(SmartCitiesAdmin):
    ordering = ["name_std"]
    list_display = ["name_std", "subregion", "region", "country", "population"]
    search_fields = ["name", "name_std"]
    raw_id_fields = ["alt_names", "region", "subregion"]


class SmartDistrictAdmin(SmartCitiesAdmin):
    raw_id_fields = ["alt_names", "city"]
    list_display = ["name_std", "city"]
    search_fields = ["name", "name_std"]


admin.site.register(SmartCountry, SmartCountryAdmin)
admin.site.register(SmartCity, SmartCityAdmin)
admin.site.register(SmartDistrict, SmartDistrictAdmin)
