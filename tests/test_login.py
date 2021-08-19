from django import urls
import pytest

@pytest.mark.django_db
def test_unsuccessful_login(new_user, client):
    '''
    Verify that the login will give you unauthorised status
    if no username or password given
    '''
    url = urls.reverse('user-login')
    resp = client.post(url)
    assert resp.status_code == 401

def test_successful_login(new_user,client):
    url = urls.reverse('user-login')
    resp = client.post(url,{
        "username":"Test_user",
        "password":"password"
    })
    assert resp.status_code == 200

def test_jwt_tokens_received(new_user,client):
    url = urls.reverse('user-login')
    resp = client.post(url,{
        "username":"Test_user",
        "password":"password"
    })
    assert resp.json()['token'] != None
    assert resp.json()['refresh'] != None
    
    
