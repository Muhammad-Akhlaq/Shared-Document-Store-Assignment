from django_filters import rest_framework as filters

from docstore.models import Folder


class CustomCharFilter(filters.CharFilter):
    def filter(self, qs, value):
        if value == 'null':
            return qs.filter(parent_folder=None)
        return super().filter(qs, value)


class FolderFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr="icontains")
    topic = filters.CharFilter(
        field_name="documents__topic__name", lookup_expr="icontains"
    )
    document = filters.CharFilter(field_name="documents__name", lookup_expr="icontains")
    parent_folder = CustomCharFilter(field_name="parent_folder")

    class Meta:
        model = Folder
        fields = ["name", "document", "topic", "parent_folder"]
