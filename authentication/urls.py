from django.urls import path
from rest_framework_simplejwt import ToknObtainPairView


urlpatterns = [
    path('authentication/token/', ToknObtainPairView.as_view(), name='token_obtain_pair'),
]