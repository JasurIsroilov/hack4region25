from django.shortcuts import render
from clinics.models import Clinic
from cities.models import City
from regions.models import Region


def clinic_list(request):
    clinics = Clinic.objects.all()
    regions = Region.objects.all()
    cities = City.objects.all()

    region_city_mapping = {
        region.id: [(city.id, city.name) for city in region.cities.all()]
        for region in regions
    }

    return render(
        request,
        "clinics/clinics_list.html",
        {
            "clinics": clinics,
            "regions": regions,
            "cities": cities,
            "region_city_mapping": region_city_mapping,
        },
    )

