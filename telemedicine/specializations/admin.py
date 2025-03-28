from django.contrib import admin

from specializations.models import Specialization


class SpecializationAdmin(admin.ModelAdmin):
    ...


admin.site.register(Specialization, SpecializationAdmin)
