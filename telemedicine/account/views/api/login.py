from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from ...serializers.token_obtain import CustomTokenObtainPairSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    permission_classes = [AllowAny]
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.user
        access_token = serializer.validated_data["access"]
        refresh_token = serializer.validated_data["refresh"]

        response = Response(
            {
                "user": {
                    "id": user.id,
                    "phone_number": user.phone_number,
                    "email": user.email,
                },
                "access_token": access_token,
                "refresh_token": refresh_token
            },
            status=status.HTTP_200_OK
        )

        response.set_cookie(
            key="access_token",
            value=access_token,
            httponly=False,
            secure=True,
            samesite="Lax",
            max_age=7 * 24 * 60 * 60
        )
        return response
