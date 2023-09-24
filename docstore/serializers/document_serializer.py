from rest_framework import serializers

from docstore.models import Document


class DocumentSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source="created_by.username")
    updated_by = serializers.ReadOnlyField(source="updated_by.username")
    file = serializers.FileField(required=True)
    topic_detail = serializers.SerializerMethodField()
    folder_detail = serializers.SerializerMethodField()
    is_active = serializers.BooleanField(read_only=True)

    class Meta:
        model = Document
        fields = [
            "id",
            "name",
            "file",
            "folder",
            "topic",
            "is_active",
            "created_at",
            "created_by",
            "updated_at",
            "updated_by",
            "topic_detail",
            "folder_detail"
        ]

    def get_topic_detail(self, instance):
        from docstore.serializers import TopicSerializer
        serializer = TopicSerializer(instance.topic)
        return serializer.data

    def get_folder_detail(self, instance):
        from docstore.serializers import ReadOnlyFolderSerializer
        serializer = ReadOnlyFolderSerializer(instance.folder)
        return serializer.data
