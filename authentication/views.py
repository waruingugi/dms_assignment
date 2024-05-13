from rest_framework.generics import CreateAPIView

from authentication.models import User
from authentication.serializers import UserSerializer


class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_context(self) -> dict:
        return {"request": self.request}
