from collections.abc import MutableSequence
class PingEventList(MutableSequence):
    def __init__(self, ping_list):
        self._ping_list = []
    def __delitem__(self, i):
        del self._ping_list[i]
    def __getitem__(self, i):
        return self._ping_list[i]
    def __len__(self):
        return len(self._ping_list)
    def __setitem__(self, i, val):
        self._ping_list[i]=val
    def insert(self, val):
        self._ping_list.append(val)
