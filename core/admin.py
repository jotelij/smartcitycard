from django.contrib import admin
from safedelete.admin import SafeDeleteAdmin, SafeDeleteAdminFilter, highlight_deleted


# Register your models here.
class BaseSafeAdmin(SafeDeleteAdmin):
    list_display = (
        highlight_deleted,
        "highlight_deleted_field",
    ) + SafeDeleteAdmin.list_display
    list_filter = (SafeDeleteAdminFilter,) + SafeDeleteAdmin.list_filter
    field_to_highlight = "id"


# ContactAdmin.highlight_deleted_field.short_description = ContactAdmin.field_to_highlight
