from django.contrib import admin

from cities.models import City


class CityAdmin(admin.ModelAdmin):
    ...


admin.site.register(City, CityAdmin)
