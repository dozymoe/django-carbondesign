""" Dump timezone names to js.
"""
from django.contrib.messages import constants
import json
import os
from pybuildtool import BaseTask

tool_name = __name__

class Task(BaseTask):

    name = tool_name

    def perform(self):
        if len(self.file_in):
            self.bld.fatal('%s does not need input' % tool_name.capitalize())

        obj = {
            'DEBUG': constants.DEBUG,
            'INFO': constants.INFO,
            'SUCCESS': constants.SUCCESS,
            'WARNING': constants.WARNING,
            'ERROR': constants.ERROR,
        }
        obj_json = json.dumps(obj)

        for fname in self.file_out:
            if os.path.exists(fname) and\
                    os.path.getsize(fname) == len(obj_json):
                continue
            with open(fname, 'w', encoding='utf-8') as f:
                f.write(obj_json)
