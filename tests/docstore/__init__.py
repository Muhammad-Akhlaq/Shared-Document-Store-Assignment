import pytest
from django.urls import reverse
from rest_framework import status

from users.models import User


@pytest.mark.django_db
def test_register_user(api_client):
    url = reverse("register")
    data = {
        "username": "testuser",
        "password": "testpassword",
        "email": "test@example.com",
    }

    response = api_client.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED
    assert User.objects.filter(username="testuser").exists()
