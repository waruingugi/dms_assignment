from django.urls import path

from authentication.views import UserCreateAPIView

app_name = "user"

urlpatterns = [
    path("user/create/", UserCreateAPIView.as_view(), name="user-create"),
]
