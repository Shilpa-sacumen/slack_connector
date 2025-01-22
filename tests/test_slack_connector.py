from typing import Any

import pytest
import responses
from requests.exceptions import HTTPError

from src.slack_connector_call import (base_url, obj, usergroup_endpoint,
                                      userinfo_endpoint)
from tests.mocks.mock_function import mock_userinfo, mock_userinfo_fail


def test_userinfo_fail():
    """ to test userinfo api """
    
    response=obj.user_info(base_url+userinfo_endpoint)
    assert response.status_code==200

def test_userinfo_error():
    """to test httperror 
    """

    url='https://slack.com/apl/conversations.list'
    # url=base_url+userinfo_endpoint
    with pytest.raises(HTTPError):
        obj.user_info(url)

def test_usergroup_error():
    """to test usergroup httperror 
    """

    url1='https://sliack.com/apl/users.list'
    # url1=base_url+usergroup_endpoint
    with pytest.raises(HTTPError):
        obj.user_group_list(url1)

def test_usergroup_fail():
    """ to test usergroup api """
    
    response=obj.user_group_list(base_url+usergroup_endpoint)
    assert response.status_code==200


def test_userinfo_mocker(mocker:Any):
    """_summary_

    Args:
        mocker (Any): _description_
    """
    
    mocker.patch("requests.get",mock_userinfo)
    response=obj.user_info("test_url")
    data=response.json()
    assert response.status_code==200
    assert data['ok']=='true'


def test_userinfo_fail_mocker(mocker:Any):
    """_summary_

    Args:
        mocker (Any): _description_
    """
    
    mocker.patch("requests.get",mock_userinfo_fail)
    response=obj.user_info("test_url")
    data=response.json()
    assert response.status_code==404
    assert data['error']=="Invalid authorization"

@pytest.mark.vcr()
def test_userinfo_vcr():
    """_summary_
    """

    response=obj.user_info(base_url+userinfo_endpoint)
    assert response.status_code==200

@pytest.mark.vcr()
def test_usergroup_vcr():
    """_summary_
    """

    response=obj.user_group_list(base_url+usergroup_endpoint)
    assert response.status_code==200

@responses.activate
def test_userinfo():
    """_summary_
    """
    data={
        'ok':True,
        'channels':[
            {
                'id':'123',
                'name':'shilpa',
            }
        ]
    }
    responses.add(
        responses.GET,
        "https://example.com/api/book/123",
        json=data,
        status=200
    )
    url="https://example.com/api/book/123"
    response=obj.user_info(url)
    assert response.status_code==200