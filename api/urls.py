from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [
    path('apply/job/', views.SendFormEmail.as_view(), name="apply"),
]
