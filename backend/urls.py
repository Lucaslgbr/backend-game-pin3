"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from backend.game import views as viewss
from backend.game.api.router import APIRouter
from backend.game.views import CustomObtainAuthToken

api_router = APIRouter()

urlpatterns = [
    path("", viewss.index, name="index"),
    path('admin/', admin.site.urls),
    path('api/', include(api_router.urls)),
    path('api/v1/auth/', CustomObtainAuthToken.as_view()),
    path("chat/<str:room_name>/<str:user_id>", viewss.room, name="room")

]
