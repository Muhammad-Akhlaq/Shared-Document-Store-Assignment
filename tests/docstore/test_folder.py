import pytest
from django.urls import reverse
from rest_framework import status

from docstore.models import Folder


@pytest.mark.django_db
class TestsFolderListCreateView:
    def test_folder_list(self, api_client, authenticated_client, folder):
        url = reverse("folder-list-create")

        # Test GET request
        response = authenticated_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
        assert response.data[0]["name"] == folder.name

    def test_folder_create(self, api_client, authenticated_client):
        url = reverse("folder-list-create")

        # Test POST request
        data = {"name": "New Folder"}
        response = authenticated_client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED
        assert Folder.objects.filter(name="New Folder").exists()

    def test_folder_list_with_name_filter(
        self, api_client, authenticated_client, folder
    ):
        url = reverse("folder-list-create")

        # Test GET request with name filter
        response = authenticated_client.get(url, {"name": folder.name})
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
        assert response.data[0]["name"] == folder.name

    def test_folder_list_with_topic_filter(
        self, api_client, authenticated_client, folder, document
    ):
        url = reverse("folder-list-create")

        # Test GET request with topic filter
        response = authenticated_client.get(url, {"topic": document.topic.name})
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
        assert response.data[0]["name"] == folder.name

    def test_folder_list_with_document_filter(
        self, api_client, authenticated_client, folder, document
    ):
        url = reverse("folder-list-create")

        # Test GET request with document filter
        response = authenticated_client.get(url, {"document": document.name})
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
        assert response.data[0]["name"] == folder.name

    def test_folder_list_with_combined_filters(
        self, api_client, authenticated_client, folder, document
    ):
        url = reverse("folder-list-create")

        # Test GET request with combined filters
        response = authenticated_client.get(
            url, {"name": document.folder.name, "topic": document.topic.name}
        )
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
        assert response.data[0]["name"] == folder.name


@pytest.mark.django_db
class TestsFolderRetrieveUpdateDestroyView:
    def test_folder_retrieve(self, api_client, authenticated_client, folder):
        url = reverse("folder-retrieve-update-destroy", kwargs={"pk": folder.pk})

        # Test GET request
        response = authenticated_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data["name"] == folder.name

    def test_folder_update(self, api_client, authenticated_client, folder):
        url = reverse("folder-retrieve-update-destroy", kwargs={"pk": folder.pk})

        # Test PUT request
        data = {"name": "Updated Folder"}
        response = authenticated_client.put(url, data)
        assert response.status_code == status.HTTP_200_OK
        assert Folder.objects.get(pk=folder.pk).name == "Updated Folder"

    def test_folder_destroy(self, api_client, authenticated_client, folder):
        url = reverse("folder-retrieve-update-destroy", kwargs={"pk": folder.pk})

        # Test DELETE request
        response = authenticated_client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert not Folder.objects.filter(pk=folder.pk, is_active=True).exists()
