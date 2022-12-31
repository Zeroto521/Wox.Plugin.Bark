# -*- coding: utf-8 -*-

import copy
from typing import List

from flowlauncher import FlowLauncher

from .bark import bark
from .template import *


class MessageManager:
    def __init__(self):
        self.queue = []

    def sendNormalMess(self, title: str, subtitle: str):
        message = copy.deepcopy(RESULT_TEMPLATE)
        message["Title"] = title
        message["SubTitle"] = subtitle

        self.queue.append(message)


class Main(MessageManager, FlowLauncher):
    def query(self, param: str) -> List[dict]:
        param = param.strip()

        title = "Bark"
        if param:
            status_code = bark(param)
            if status_code == 200:
                self.sendNormalMess(title, "Succeed.")
            else:
                self.sendNormalMess(title, "Fail.")
        else:
            self.sendNormalMess(
                title, "Input the message which you want to send your device.",
            )

        return self.queue
