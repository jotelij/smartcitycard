from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response

from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope

from .serializers import (
    UserSerializer,
    GroupSerializer,
    CountrySerializer,
    PersonSerializer,
)
from magala.models import SmartCountry
from card.models import Person

DEV_PERMISSIONS = [permissions.IsAuthenticated]
COMMON_PERMISSIONS = [permissions.AllowAny]


class UserList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetails(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    # required_scopes = ["groups"]
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class CountryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = SmartCountry.objects.all()
    serializer_class = CountrySerializer
    permission_classes = COMMON_PERMISSIONS


class PersonViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = COMMON_PERMISSIONS
