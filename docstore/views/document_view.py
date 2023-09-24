from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from docstore.mixins import (
    CreateUpdateMixin,
    DestroyMixin,
    IsActiveFilterMixin,
    OwnershipPermissionMixin,
)
from docstore.models import Document
from docstore.serializers import DocumentSerializer


class DocumentListCreateView(
    CreateUpdateMixin, IsActiveFilterMixin, generics.ListCreateAPIView
):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated]


class DocumentRetrieveUpdateDestroyView(
    DestroyMixin,
    OwnershipPermissionMixin,
    IsActiveFilterMixin,
    generics.RetrieveUpdateDestroyAPIView,
):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated]
