from rest_framework import serializers

from docstore.models import Topic


class TopicSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source="created_by.username")
    updated_by = serializers.ReadOnlyField(source="updated_by.username")
    is_active = serializers.BooleanField(read_only=True)

    class Meta:
        model = Topic
        fields = [
            "id",
            "name",
            "is_active",
            "created_at",
            "created_by",
            "updated_at",
            "updated_by",
        ]
