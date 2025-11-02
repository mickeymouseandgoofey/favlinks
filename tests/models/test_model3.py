import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from links.models import Link

@pytest.mark.django_db
def test_add_link_saves_user_link(client):
    # Create and log in user
    user = User.objects.create_user(username="student", password="pass")
    client.login(username="student", password="pass")

    # Submit form data
    response = client.post(reverse("add_link"), {
        "title": "My Blog",
        "url": "https://myblog.example.com",
        "description": "Personal blog",
        "tags": "blog,personal"
    })

    # Check redirect
    assert response.status_code == 302
    assert response.url == reverse("link_list")

    # Confirm link was saved and tied to user
    link = Link.objects.get(title="My Blog")
    assert link.user == user
    assert link.url == "https://myblog.example.com"
