import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken


@pytest.mark.django_db
class TestsUserAuthenticationView:
    def test_login_user(self, api_client, user):
        url = reverse("user-login")
        data = {
            "username": user.username,
            "password": "testpassword",
        }

        response = api_client.post(url, data)
        assert response.status_code == status.HTTP_200_OK
        assert "access" in response.data
        assert "refresh" in response.data

    def test_login_user_invalid_credentials(self, api_client, user):
        url = reverse("user-login")
        data = {
            "username": user.username,
            "password": "invalidpassword",
        }

        response = api_client.post(url, data)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_refresh_token(self, api_client, user):
        url = reverse("user-token-refresh")
        refresh = RefreshToken.for_user(user)
        response = api_client.post(url, data={"refresh": str(refresh)})
        assert response.status_code == status.HTTP_200_OK
        assert "access" in response.data
        assert "refresh" in response.data

    def test_refresh_token_invalid_token(self, api_client):
        url = reverse("user-token-refresh")
        response = api_client.post(url, data={"refresh": "invalidtoken"})
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
