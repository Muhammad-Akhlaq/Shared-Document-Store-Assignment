import pytest
from django.urls import reverse
from rest_framework import status

from docstore.models import Topic


@pytest.mark.django_db
class TestsTopicListCreateView:
    def test_topic_list(self, api_client, authenticated_client, topic):
        url = reverse("topic-list-create")

        # Test GET request
        response = authenticated_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
        assert response.data[0]["name"] == topic.name

    def test_topic_create(self, api_client, authenticated_client):
        url = reverse("topic-list-create")

        # Test POST request
        data = {"name": "New Topic"}
        response = authenticated_client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED
        assert Topic.objects.filter(name="New Topic").exists()


@pytest.mark.django_db
class TestsTopicRetrieveUpdateDestroyView:
    def test_topic_retrieve(self, api_client, authenticated_client, topic):
        url = reverse("topic-retrieve-update-destroy", kwargs={"pk": topic.pk})

        # Test GET request
        response = authenticated_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data["name"] == topic.name

    def test_topic_update(self, api_client, authenticated_client, topic):
        url = reverse("topic-retrieve-update-destroy", kwargs={"pk": topic.pk})

        # Test PUT request
        data = {"name": "Updated Topic"}
        response = authenticated_client.put(url, data)
        assert response.status_code == status.HTTP_200_OK
        assert Topic.objects.get(pk=topic.pk).name == "Updated Topic"

    def test_topic_destroy(self, api_client, authenticated_client, topic):
        url = reverse("topic-retrieve-update-destroy", kwargs={"pk": topic.pk})

        # Test DELETE request
        response = authenticated_client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert not Topic.objects.filter(pk=topic.pk, is_active=True).exists()
