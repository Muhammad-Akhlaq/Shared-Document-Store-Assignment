from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from docstore.filters import FolderFilter
from docstore.mixins import (
    CreateUpdateMixin,
    DestroyMixin,
    IsActiveFilterMixin,
    OwnershipPermissionMixin,
)
from docstore.models import Folder
from docstore.serializers import FolderSerializer


class FolderListCreateView(
    CreateUpdateMixin, IsActiveFilterMixin, generics.ListCreateAPIView
):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer
    permission_classes = [IsAuthenticated]
    filterset_class = FolderFilter


class FolderRetrieveUpdateDestroyView(
    DestroyMixin,
    OwnershipPermissionMixin,
    IsActiveFilterMixin,
    generics.RetrieveUpdateDestroyAPIView,
):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer
    permission_classes = [IsAuthenticated]
    filterset_class = FolderFilter
