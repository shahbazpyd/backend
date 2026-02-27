from django.urls import path

from backend.accademy.accademy import urls
from .views import RegisterView
from rest_framework_simpleJWT.views import TokenOptainPairView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("register/", RegisterView.as_view()),
    path("login/", TokenOptainPairView.as_view()),
    path("refresh/", TokenRefreshView.as_view()),
]