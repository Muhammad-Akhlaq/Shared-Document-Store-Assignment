from rest_framework import serializers

from docstore.models import Folder


class FolderSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source="created_by.username")
    updated_by = serializers.ReadOnlyField(source="updated_by.username")
    parent_folder_detail = serializers.SerializerMethodField()
    documents = serializers.SerializerMethodField()
    is_active = serializers.BooleanField(read_only=True)

    class Meta:
        model = Folder
        fields = [
            "id",
            "name",
            "parent_folder",
            "is_active",
            "created_at",
            "created_by",
            "updated_at",
            "updated_by",
            "documents",
            "parent_folder_detail",
        ]

    def get_documents(self, instance):
        from docstore.serializers import DocumentSerializer

        serializer = DocumentSerializer(
            instance.documents.filter(is_active=True).all(), many=True
        )
        return serializer.data

    def get_parent_folder_detail(self, obj):
        if obj.parent_folder:
            # Serialize the parent folder using the same serializer
            serializer = self.__class__(obj.parent_folder)
            return serializer.data
        return None


class ReadOnlyFolderSerializer(FolderSerializer):
    documents = None
