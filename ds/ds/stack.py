class Stack:

    def __init_(self):
        self._storage = []

    def __len__(self):
        return len(self._storage)

    def push(self, item):
        self._storage.append(item)

    def pop(self):
        try: 
            item = self._storage.po()
        except indexError:
            item = None
        return item
