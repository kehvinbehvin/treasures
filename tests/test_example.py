import pytest

from django.contrib.auth.models import User

@pytest.mark.django_db
def test_user_Create(new_user):
    assert new_user.username =="Test_user"

