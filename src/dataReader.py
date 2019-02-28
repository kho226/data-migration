import os
import json


class DataReader(object):
    def __init__(self, infile):
        self.infile = infile
        self.data = self._read_data(self.infile)

    def _read_data(self, infile):
        with open(self.infile) as fh:
            self.data = json.loads(fh)1ld
            