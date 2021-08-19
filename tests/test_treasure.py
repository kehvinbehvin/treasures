from django import urls
import pytest
from rest_framework.test import APIClient
from treasure.models import Treasure

@pytest.mark.django_db
def test_authorized_entry(client):
    '''
    Verify that this view is authorised for unauthenticated users
    '''
    url = urls.reverse('all-treasures')
    resp = client.get(url)
    assert resp.status_code == 200
    # Returns status 200 OK

def test_unauthorized_entry(client):
    '''
    Verify that this view is not for unauthenticated users
    '''
    url = urls.reverse('participated-treasures')
    resp = client.get(url)
    assert resp.status_code == 401
    # Returns status 401 unauthorised

def test_authorized_entry(jwt_access_token):
    '''
    Verify that the Jwt authentication works
    '''
    url = urls.reverse('participated-treasures')
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION = 'Bearer ' + jwt_access_token)
    resp = client.get(url)
    assert resp.status_code == 200
    # Should be authenticated into the route

def test_addhunters(new_user,new_treasure):
    new_treasure.hunters.add(new_user)
    assert new_treasure.hunters.count() == 1

@pytest.mark.django_db
def test_treasure_detailed(new_treasure,jwt_access_token):
    treasure_name = new_treasure.name
    treasure = Treasure.objects.all()
    url = urls.reverse('detailed-treasures',kwargs={'name':treasure_name})
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION = 'Bearer ' + jwt_access_token)
    resp = client.get(url)
    assert resp.json()[0]['name'] == 'default-name'
    # Should return the treasure object given the treasure name

@pytest.mark.django_db
def test_treasure_detailed_update_hunter(new_treasure,jwt_access_token,new_user):
    treasure_name = new_treasure.name
    new_user_name = new_user.username
    treasure = Treasure.objects.all()
    url = urls.reverse('detailed-treasures',kwargs={'name':treasure_name})
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION = 'Bearer ' + jwt_access_token)
    resp = client.put(url)
    assert resp.json()[0]['hunters'][0]['username'] == new_user_name
    # Should return the treasure object with the new user's name

def test_treasure_detailed_update_hunter_nonexistent(new_treasure,jwt_access_token,new_user):
    treasure_name = 'fewaf'
    new_user_name = new_user.username
    treasure = Treasure.objects.all()
    url = urls.reverse('detailed-treasures',kwargs={'name':treasure_name})
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION = 'Bearer ' + jwt_access_token)
    resp = client.put(url)
    assert resp.status_code == 400
    # Should return the status 400 bad request.


def test_treasure_detailed_nonexistent(new_treasure,jwt_access_token,new_user):
    treasure_name = 'fewaf'
    treasure = Treasure.objects.all()
    url = urls.reverse('detailed-treasures',kwargs={'name':treasure_name})
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION = 'Bearer ' + jwt_access_token)
    resp = client.get(url)
    assert resp.json() == []
    # Should return empty array if the treasure does not exist