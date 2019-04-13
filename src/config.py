import os
import json


class Config:

    DIRECTORY = "directory"
    SUCCEEDED = "succeeded"

    def __init__(self, name):
        dir_ = os.path.dirname(os.path.realpath(__file__))
        self._name = os.path.join(dir_, name)
        self._data = dict()

        # Properties that reside in _data
        self.directory = "./"
        self.succeeded = 0b0  # List of downloaded comics stored as binary

        if not os.path.isfile(self._name):
            with open(self._name, "w") as _file:
                json.dump(self.data, _file, indent=4)

        self.data = json.loads(open(self._name).read())  # Load old config file

    def commit(self):
        with open(self._name, "w") as _file:
            json.dump(self._data, _file, indent=4)

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    @property
    def directory(self):
        return self._data[self.DIRECTORY]

    @directory.setter
    def directory(self, directory):
        self._data[self.DIRECTORY] = directory

    @property
    def succeeded(self):
        return self._data[self.SUCCEEDED]

    @succeeded.setter
    def succeeded(self, succeeded):
        self._data[self.SUCCEEDED] = succeeded

    def get_succeeded_list(self, end):
        return [img for img in range(end) if self.succeeded & (0b1 << img)]

    def set_succeeded(self, succeeded):
        self.succeeded = self.succeeded | (0b1 << succeeded)
