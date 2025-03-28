from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from clinics.models import Clinic
from clinics.serializers.read import ClinicReadSerializer


class NearestClinicsView(APIView):
    def post(self, request):
        try:
            user_latitude = float(request.data.get("latitude"))
            user_longitude = float(request.data.get("longitude"))

            clinics = Clinic.objects.all()

            clinics = sorted(
                clinics,
                key=lambda clinic: (
                        (float(clinic.latitude) - user_latitude) ** 2 +
                        (float(clinic.longitude) - user_longitude) ** 2
                )
            )

            nearest_clinics = clinics[:10]

            serializer = ClinicReadSerializer(nearest_clinics, many=True)
            return Response({"clinics": serializer.data}, status=status.HTTP_200_OK)

        except (TypeError, ValueError) as e:
            return Response({"error": "Invalid data"}, status=status.HTTP_400_BAD_REQUEST)
