from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import CustomTokenObtainPairView, getUsers, registerUser

urlpatterns = [
    path('register', registerUser),
    path('login', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),  
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'), 
]
