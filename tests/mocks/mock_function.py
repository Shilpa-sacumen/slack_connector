import json
from typing import Any, Dict, List

from requests import Response


def mock_userinfo(*args:List[Any],**kwargs:Dict[str,Any])->Response:
    """mock for converstion list api success

    Returns:
        Response: _description_
    """
    result={
        "ok": "true",
        "channels": [
        {
            "id": "C086YFZ9DDL",
            "name": "all-shilpa",
            "is_channel": "true",
            "is_group": "false",
            "is_im": "false",
            "updated": 1735880230018,          
        },
        ]
    }
    url='https://slack.com/api/users.info'
    response=Response()
    response.url=url
    response.status_code=200
    response._content=bytes(json.dumps(result),encoding="utf-8")
    return response

def mock_userinfo_fail(*args:List[Any],**kwargs:Dict[str,Any])->Response:
    """_summary_

    Returns:
        Response: _description_
    """
    result={
        'error':"Invalid authorization"
    }
    url='https://slack.com/api/users.info'
    response=Response()
    response.url=url
    response.status_code=404
    response._content=bytes(json.dumps(result),encoding="utf-8")
    return response