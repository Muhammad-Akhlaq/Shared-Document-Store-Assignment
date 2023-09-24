import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
class TestsUserDetailView:
    def test_get_user_detail(self, api_client, user):
        url = reverse("user-detail")
        api_client.force_authenticate(user=user)

        response = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data["username"] == user.username

    def test_get_user_detail_unauthenticated(self, api_client):
        url = reverse("user-detail")

        response = api_client.get(url)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
