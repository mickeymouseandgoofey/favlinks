import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from links.models import Link

@pytest.mark.django_db
def test_add_link_missing_title(client):
    # Create and log in user
    user = User.objects.create_user(username="student", password="pass")
    client.login(username="student", password="pass")

    # Submit form with missing title
    response = client.post(reverse("add_link"), {
        "title": "",  # Missing required field
        "url": "https://example.com",
        "description": "Missing title test",
        "tags": "test"
    })

    # Form should not redirect
    assert response.status_code == 200
    content = response.content.decode()
    assert "This field is required" in content or "title" in content.lower()

    # Confirm no link was saved
    assert not Link.objects.filter(url="https://example.com").exists()
