class MyHashSet:

    def __init__(self):
        self.hash_set = []

    def _hasKey(self, key):
        if key in self.hash_set:
            return True
        
        return False

    def add(self, key: int) -> None:
        if not self._hasKey(key):
            self.hash_set.append(key)

    def remove(self, key: int) -> None:
        if self._hasKey(key):
            for idx, value in enumerate(self.hash_set):
                if key == value:
                    self.hash_set.pop(idx)
                    break

    def contains(self, key: int) -> bool:
        return self._hasKey(key)


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)