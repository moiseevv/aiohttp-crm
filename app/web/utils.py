from typing import Any
from aiohttp.web_response import Response
from aiohttp.web import json_response as aiohttp_json_response


def json_response(data: Any = None, status: str = 'ok'):
    if data is None:
        data = {}
    return aiohttp_json_response(data={
        "status": status,
        "data": data,
    })

def json_error(http_status: int, status: str = 'error', message = None, data = None):
    if data is None:
        data = {}
    return aiohttp_json_response(
        status= http_status,
        data={
            "status":status,
            "message":str(message),
            "data":data,
        }
    )

