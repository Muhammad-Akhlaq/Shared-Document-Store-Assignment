import pytest
from django.urls import reverse
from rest_framework import status

from users.models import User


@pytest.mark.django_db
class TestsUserRegistrationView:
    def test_register_user(self, api_client):
        url = reverse("user-register")
        data = {
            "username": "testuser",
            "password": "testpassword",
            "email": "test@example.com",
        }

        response = api_client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED
        assert User.objects.filter(username="testuser").exists()

    def test_register_user_missing_username(self, api_client):
        url = reverse("user-register")
        data = {"password": "testpassword", "email": "test@example.com"}

        response = api_client.post(url, data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert not User.objects.filter(email="test@example.com").exists()

    def test_register_user_missing_password(self, api_client):
        url = reverse("user-register")
        data = {"username": "testuser", "email": "test@example.com"}

        response = api_client.post(url, data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert not User.objects.filter(username="testuser").exists()

    def test_register_user_missing_email(self, api_client):
        url = reverse("user-register")
        data = {"username": "testuser", "password": "testpassword"}

        response = api_client.post(url, data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert not User.objects.filter(username="testuser").exists()

    def test_register_user_existing_username(self, api_client, user):
        url = reverse("user-register")
        data = {
            "username": user.username,
            "password": "testpassword",
            "email": "test@example.com",
        }

        response = api_client.post(url, data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.json() == ["Username already exists."]

    def test_register_user_existing_email(self, api_client, user):
        url = reverse("user-register")
        data = {"username": "newuser", "password": "testpassword", "email": user.email}

        response = api_client.post(url, data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.json() == ["Email already exists."]
