from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import (
    Profile,
    TenantContract,
    Event,
    MaintenanceRequest
)


class ProfileAdmin(UserAdmin):
    model = Profile
    fieldsets = UserAdmin.fieldsets + (
        ("Custom Fields", {"fields": ("room",
                                      "id_number",
                                      "initial_contract_date",
                                      "final_contract_date"
                                      )}),
    )


admin.site.register(Profile, ProfileAdmin)

admin.site.register(Event)

admin.site.register(TenantContract)

admin.site.register(MaintenanceRequest)
