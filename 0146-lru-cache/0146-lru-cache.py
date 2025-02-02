class LRUCache:
    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}
    def get(self, key: int) -> int:
        if key in self.cache:
            val=self.cache[key]
            del self.cache[key]
            self.cache[key]=val
            return val
        else:
            return -1
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            del self.cache[key]
            self.cache[key]=value
        else:
            if len(self.cache)<self.capacity:
                self.cache[key]=value
            else:
                k=list(self.cache.keys())[0]
                del self.cache[k]
                self.cache[key]=value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)