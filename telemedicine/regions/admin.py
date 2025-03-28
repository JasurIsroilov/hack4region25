from django.contrib import admin

from regions.models import Region


class RegionAdmin(admin.ModelAdmin):
    ...


admin.site.register(Region, RegionAdmin)
