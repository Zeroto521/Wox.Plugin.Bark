# -*- coding: utf-8 -*-

import copy
import os
import sys
from typing import List
sys.path.append('../bark')

from bark import bark
from wox import Wox

from .template import *


class Main(Wox):

    messages_queue = []

    def sendNormalMess(self, title: str, subtitle: str):
        message = copy.deepcopy(RESULT_TEMPLATE)
        message['Title'] = title
        message['SubTitle'] = subtitle

        self.messages_queue.append(message)

    def query(self, param: str) -> List[dict]:
        param = param.strip()

        if param:
            status_code = bark(param)
            self.sendNormalMess('Bark', 'Done.')

            if status_code == 200:
                self.sendNormalMess('Bark', 'Succeed.')
            else:
                self.sendNormalMess('Bark', 'Fail.')
        else:
            self.sendNormalMess(
                'Bark', 'Input the message which you want to send your device.')

        return self.messages_queue
