from django.urls import path

from authentication.views import (
    UserCreateAPIView,
    UserDeleteAPIView,
    UserListAPIView,
    UserRetrieveUpdateAPIView,
)

app_name = "user"

urlpatterns = [
    path("user/create/", UserCreateAPIView.as_view(), name="user-create"),
    path("user/list/", UserListAPIView.as_view(), name="user-list"),
    path("users/<str:id>/", UserRetrieveUpdateAPIView.as_view(), name="user-detail"),
    path("users/<str:id>/delete/", UserDeleteAPIView.as_view(), name="user-delete"),
]
