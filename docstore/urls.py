from django.urls import path

from docstore.views import (
    DocumentListCreateView,
    DocumentRetrieveUpdateDestroyView,
    FolderListCreateView,
    FolderRetrieveUpdateDestroyView,
    TopicListCreateView,
    TopicRetrieveUpdateDestroyView,
)

urlpatterns = [
    path("documents/", DocumentListCreateView.as_view(), name="document-list-create"),
    path(
        "documents/<int:pk>/",
        DocumentRetrieveUpdateDestroyView.as_view(),
        name="document-retrieve-update-destroy",
    ),
    path("folders/", FolderListCreateView.as_view(), name="folder-list-create"),
    path(
        "folders/<int:pk>/",
        FolderRetrieveUpdateDestroyView.as_view(),
        name="folder-retrieve-update-destroy",
    ),
    path("topics/", TopicListCreateView.as_view(), name="topic-list-create"),
    path(
        "topics/<int:pk>/",
        TopicRetrieveUpdateDestroyView.as_view(),
        name="topic-retrieve-update-destroy",
    ),
]
