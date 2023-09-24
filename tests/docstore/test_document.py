import pytest
from django.urls import reverse
from rest_framework import status

from docstore.models import Document


@pytest.mark.django_db
class TestsDocumentListCreateView:
    def test_document_list(self, api_client, authenticated_client, document):
        url = reverse("document-list-create")

        # Test GET request
        response = authenticated_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
        assert response.data[0]["name"] == document.name

    def test_document_create(self, api_client, authenticated_client, folder, topic):
        url = reverse("document-list-create")
        file = open("tests/utils/dummy.txt", "rb")
        # Test POST request
        data = {
            "name": "New Document",
            "file": file,
            "folder": folder.pk,
            "topic": topic.pk,
        }
        response = authenticated_client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED
        assert Document.objects.filter(name="New Document", folder=folder).exists()

    def test_unauthenticated_user_document_list(self, api_client, document):
        url = reverse("document-list-create")

        # Test GET request without authentication
        response = api_client.get(url)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_unauthenticated_user_document_create(self, api_client, folder):
        url = reverse("document-list-create")

        # Test POST request without authentication
        data = {"name": "New Document", "folder": folder.pk}
        response = api_client.post(url, data)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
class TestsDocumentRetrieveUpdateDestroyView:
    def test_document_retrieve(self, api_client, authenticated_client, document):
        url = reverse("document-retrieve-update-destroy", kwargs={"pk": document.pk})

        # Test GET request
        response = authenticated_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data["name"] == document.name

    def test_document_update(
        self, api_client, authenticated_client, document, folder, topic
    ):
        url = reverse("document-retrieve-update-destroy", kwargs={"pk": document.pk})

        file = open("tests/utils/dummy.txt", "rb")
        # Test PUT request
        data = {
            "name": "Updated Document",
            "file": file,
            "folder": folder.pk,
            "topic": topic.pk,
        }
        response = authenticated_client.put(url, data)
        assert response.status_code == status.HTTP_200_OK
        assert Document.objects.get(pk=document.pk).name == "Updated Document"
        assert Document.objects.get(pk=document.pk).folder == folder

    def test_document_destroy(self, api_client, authenticated_client, document):
        url = reverse("document-retrieve-update-destroy", kwargs={"pk": document.pk})

        # Test DELETE request
        response = authenticated_client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert not Document.objects.filter(pk=document.pk, is_active=True).exists()

    def test_unauthenticated_user_document_retrieve(self, api_client, document):
        url = reverse("document-retrieve-update-destroy", kwargs={"pk": document.pk})

        # Test GET request without authentication
        api_client.credentials(HTTP_AUTHORIZATION="Bearer invalid_token")
        response = api_client.get(url)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_unauthenticated_user_document_update(self, api_client, document, folder):
        url = reverse("document-retrieve-update-destroy", kwargs={"pk": document.pk})

        # Test PUT request without authentication
        api_client.credentials(HTTP_AUTHORIZATION="Bearer invalid_token")
        data = {"name": "Updated Document", "folder": folder.pk}
        response = api_client.put(url, data)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_unauthenticated_user_document_destroy(self, api_client, document):
        url = reverse("document-retrieve-update-destroy", kwargs={"pk": document.pk})

        # Test DELETE request without authentication
        api_client.credentials(HTTP_AUTHORIZATION="Bearer invalid_token")
        response = api_client.delete(url)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
