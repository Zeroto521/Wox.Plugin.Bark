# -*- coding: utf-8 -*-

import requests

from .constant import *


def bark(message: str) -> int:
    url = api_url.format(key=key, message=message)
    r = requests.post(url)

    return r.status_code
