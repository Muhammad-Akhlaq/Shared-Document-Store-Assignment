from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response


class OwnershipPermissionMixin:
    def check_object_permissions(self, request, obj):
        super().check_object_permissions(request, obj)
        if not obj.is_owned_by(request.user):
            raise PermissionDenied("You do not have permission to perform this action.")


class IsActiveFilterMixin:
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_active=True)


class CreateUpdateMixin:
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)


class DestroyMixin:
    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.check_object_permissions(request, instance)
        self.perform_destroy(instance)
        return self.send_response()

    def send_response(self):
        return self.http_response(status_=status.HTTP_204_NO_CONTENT)

    @staticmethod
    def http_response(status_=status.HTTP_200_OK, data=None):
        return Response(data, status=status_)
