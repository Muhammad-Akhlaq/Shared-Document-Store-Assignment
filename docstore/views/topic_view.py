from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from docstore.mixins import (
    CreateUpdateMixin,
    DestroyMixin,
    IsActiveFilterMixin,
    OwnershipPermissionMixin,
)
from docstore.models import Topic
from docstore.serializers import TopicSerializer


class TopicListCreateView(
    CreateUpdateMixin, IsActiveFilterMixin, generics.ListCreateAPIView
):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = [IsAuthenticated]


class TopicRetrieveUpdateDestroyView(
    DestroyMixin,
    OwnershipPermissionMixin,
    IsActiveFilterMixin,
    generics.RetrieveUpdateDestroyAPIView,
):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = [IsAuthenticated]
