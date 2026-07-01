class MyHashMap:

    def __init__(self):
        self.legth = 10000
        self.ht = [None] * self.legth
    
    def _generation_hash(self, key: int) -> int:
        return key % self.legth

    def put(self, key: int, value: int) -> None:
        _key = self._generation_hash(key)
        self.ht[_key] = value

    def get(self, key: int) -> int:
        _key = self._generation_hash(key)
        print(self.ht[_key])
        return self.ht[_key] if self.ht[_key] != None else -1

    def remove(self, key: int) -> None:
        _key = self._generation_hash(key)
        self.ht[_key] = None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)