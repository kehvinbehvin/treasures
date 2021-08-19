import pytest
from django.contrib.auth.models import User
from django import urls
from treasure.models import Treasure

@pytest.fixture
def new_user_factory(db):
    def create_app_user(
        username:str,
        password: str = None,
        first_name: str ='firstname',
        last_name: str = 'lastname',
        email: str = 'test@test.com',
        is_staff:str = False,
        is_superuser: str = False,
        is_active: str = True,
    ):
        user = User.objects.create_user(
            username= username,
            password = password,
            first_name = first_name,
            last_name = last_name,
            email = email,
            is_staff = is_staff,
            is_superuser = is_superuser ,
            is_active = is_active,
        )
        return user
    return create_app_user

@pytest.fixture
def new_user(db,new_user_factory):
    return new_user_factory("Test_user","password","Kevin")

@pytest.fixture
def jwt_access_token(db,new_user,client):
    url = urls.reverse('user-login')
    resp = client.post(url,{
        "username":"Test_user",
        "password":"password"
    })
    return resp.json()['token']

@pytest.fixture
def new_treasure_factory(db):
    def create_treasure(
        author,
            name = "default-name",
            description = "default-description",
            lng = 123,
            lat = 321,
            quiz = "default-quiz",
            mcq1 = "default-quiz",
            mcq2 = "default-mcq1",
            mcq3 = "default-mcq2",
            hint = "default-mcq3",
            answer = "default-answer",
    ):
        treasure = Treasure.objects.create(
            author = author,
            name = name,
            description = description,
            lng = lng,
            lat = lat,
            quiz = quiz,
            mcq1 = mcq1,
            mcq2 = mcq2,
            mcq3 = mcq3,
            hint = hint,
            answer = answer,
        )
        return treasure
    return create_treasure

@pytest.fixture
def new_treasure(db,new_treasure_factory,new_user):
    return new_treasure_factory(new_user)