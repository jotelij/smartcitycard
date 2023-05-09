from django.contrib import admin
from core.admin import BaseSafeAdmin
from .models import Person, PersonHouse, Ethinicity


# Register your models here.
@admin.register(Person)
class PersonAdmin(BaseSafeAdmin):
    pass


@admin.register(PersonHouse)
class PersonHouseAdmin(BaseSafeAdmin):
    pass


admin.site.register(Ethinicity)
# admin.site.register(Person, PersonAdmin)

# ContactAdmin.highlight_deleted_field.short_description = ContactAdmin.field_to_highlight
