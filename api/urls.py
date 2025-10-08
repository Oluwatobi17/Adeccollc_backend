from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [
    # path('airjordan/apply/job/', views.SendFormEmailAirJordan.as_view(), name="Airjordan_apply"),
]
