class MyHashSet:

    def __init__(self):
        self.hash_set = []

    def _hasKey(self, key):
        for idx, _ in enumerate(self.hash_set):
            if key == self.hash_set[idx]:
                return idx
        return -1

    def add(self, key: int) -> None:
        idx = self._hasKey(key)
        if idx == -1:
            self.hash_set.append(key)

    def remove(self, key: int) -> None:
        idx = self._hasKey(key)
        if idx != -1:
            self.hash_set.pop(idx)

    def contains(self, key: int) -> bool:
        if self._hasKey(key) != -1:
            return True
        
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)