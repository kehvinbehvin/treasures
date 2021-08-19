from django import urls
import pytest

def test_unsuccessful_registration(client):
    '''
    Verify that the login will give you 500 Internal server error if
    you do not send any info
    '''
    url = urls.reverse('user-signup')
    resp = client.post(url)
    assert resp.status_code == 400
    # Returns status 400 Bad Request, 

@pytest.mark.django_db
def test_successful_registration(client):
    url = urls.reverse('user-signup')
    resp = client.post(url,{
        "username":"Test_user",
        "password":"password",
        "email":"Test_user@gmail.com"
    })
    assert resp.status_code == 201
    # Returns status 201 created