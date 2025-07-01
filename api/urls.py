from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [
    path('apply/job/', views.SendFormEmail.as_view(), name="apply"),
    path('airmax/apply/job/', views.SendFormEmailAirMax.as_view(), name="Airmax_apply"),
    path('airjordan/apply/job/', views.SendFormEmailAirJordan.as_view(), name="Airjordan_apply"),
]
