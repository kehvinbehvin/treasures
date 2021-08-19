from django import urls
import pytest
from rest_framework.test import APIClient
from invites.models import Invites

# @pytest.mark.parametrize('view_params',['user-signup','user-login'])
# def test_unauthorized_entry(client):
#     '''
#     Verify that this view is not for unauthenticated users
#     '''
#     # url = urls.reverse('inviters')
#     # resp = client.get('/inviters/1')
#     assert resp.status_code == 401
    # Returns status 401 unauthorised