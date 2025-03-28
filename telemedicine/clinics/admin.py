from django.contrib import admin

from clinics.models import Clinic


class ClinicAdmin(admin.ModelAdmin):
    ...


admin.site.register(Clinic, ClinicAdmin)
