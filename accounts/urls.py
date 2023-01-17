from django.urls import path
from accounts.views import CustomTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('login/', CustomTokenObtainPairView.as_view(), name='login_token_obtain'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]