import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from docstore.models import Document, Folder, Topic

User = get_user_model()


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user():
    return User.objects.create_user(
        username="testuser", password="testpassword", email="test@example.com"
    )


@pytest.fixture
def authenticated_client(user):
    client = APIClient()
    refresh = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
    return client


@pytest.fixture
def folder(user):
    return Folder.objects.create(name="Test Folder", created_by=user, updated_by=user)


@pytest.fixture
def topic(user):
    return Topic.objects.create(name="Test Topic", created_by=user, updated_by=user)


@pytest.fixture
def document(folder, topic, user):
    return Document.objects.create(
        name="Test Document",
        folder=folder,
        topic=topic,
        created_by=user,
        updated_by=user,
    )
