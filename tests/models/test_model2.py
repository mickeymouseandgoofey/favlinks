import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from links.models import Link

@pytest.mark.django_db
def test_link_list_filters_by_user(client):
    # Create two users
    user1 = User.objects.create_user(username="student1", password="pass")
    user2 = User.objects.create_user(username="student2", password="pass")

    # Create links for each user
    Link.objects.create(user=user1, title="User1 Link", url="https://user1.com")
    Link.objects.create(user=user2, title="User2 Link", url="https://user2.com")

    # Log in as user1
    client.login(username="student1", password="pass")

    # Call the view
    response = client.get(reverse("link_list"))

    # Check that only user1's link is shown
    assert response.status_code == 200
    content = response.content.decode()
    assert "User1 Link" in content
    assert "User2 Link" not in content
