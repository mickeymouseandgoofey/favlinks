import pytest
from django.contrib.auth.models import User
from links.models import Link  # ✅ matches your actual model name

@pytest.mark.django_db
def test_link_str():
    user = User.objects.create_user(username="student")
    link = Link.objects.create(
        user=user,
        title="My Portfolio",
        url="https://myportfolio.example.com"
    )
    assert str(link) == "My Portfolio"
