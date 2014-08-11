class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.table = {}
        self.size = 0
        self.queue = []
        

    # @return an integer
    def get(self, key):
        if key in self.table:
            self.queue.remove(key)
            self.queue.append(key)         
            return self.table[key]
        else:
            return -1
        

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.table:
            self.queue.remove(key)
            self.table[key] = value
            self.queue.append(key)
        else:
            if self.size < self.capacity:
                self.table[key] = value 
                self.queue.append(key)
                self.size += 1
            else:
                del self.table[self.queue[0]]
                del self.queue[0]
                self.size -= 1
                self.set(key,value)  