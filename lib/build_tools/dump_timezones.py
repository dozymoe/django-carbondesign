""" Dump timezone names to js.
"""
import json
import os
from pybuildtool import BaseTask
import pytz

tool_name = __name__

class Task(BaseTask):

    name = tool_name

    def perform(self):
        if len(self.file_in):
            self.bld.fatal('%s does not need input' % tool_name.capitalize())

        items = [x for x in sorted(pytz.common_timezones)]
        items_json = json.dumps(items)

        for fname in self.file_out:
            if os.path.exists(fname) and\
                    os.path.getsize(fname) == len(items_json):
                continue
            with open(fname, 'w', encoding='utf-8') as f:
                f.write(items_json)
