class Entry:
    def __init__(self, item, priority):
        self.priority = priority
        self.item = item
    def __lt__(self, other):
        return self.priority < other.priority
    def __eq__(self, other):
        return self.item == other.item and self.priority == other.priority


class PQ_UL:
    def __init__(self):
        self._entries = []
    def insert(self, item, priority):
        self._entries.append(Entry(item, priority))
    def __len__(self):
        return len(self._entries)
    def find_min(self):
        return min(self._entries)
    def remove_min(self):
        entry = min(self._entries)
        self._entries.remove
        return entry


class PQ_OL:
    def __init__(self):
        self._entries = []
    def insert(self, item, priority):
        self._entries.append(Entry(item, priority))
        self._entries.sort(reverse = True)
    def __len__(self):
        return len(self._entries)
    def find_min(self):
        return self._entries[-1]
    def remove_min(self):
        return self._entries.pop()