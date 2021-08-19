from django import urls
import pytest
from rest_framework.test import APIClient

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
    # header = {'HTTP_Authorization': "Bearer "+jwt_access_token}
    url = urls.reverse('participated-treasures')
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION = 'Bearer ' + jwt_access_token)
    resp = client.get(url)
    assert resp.status_code == 200
    # Should be authenticated into the route

def test_addhunters(new_user,new_treasure):
    new_treasure.hunters.add(new_user)
    assert new_treasure.hunters.count() == 1

