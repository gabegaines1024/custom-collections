"""
LRU (Least Recently Used) Cache Implementation

An LRU cache removes the least recently used item when it reaches capacity.
Use cases: caching API responses, database queries, expensive computations.

Time Complexity:
- get(): O(1)
- put(): O(1)
"""

from collections import OrderedDict
from typing import Any

class LRUCache:

    def __init__(self, capacity: int):

        if capacity <= 0:
            raise ValueError("Capacity must be greater than 0")
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: str) -> Any:
        if key not in self.cache:
            return None
        
        self.cache.move_to_end(key)
        return self.cache[key]
    
    def put(self, key, value):
        """
        Add or update key-value pair. Evict LRU item if at capacity.
        
        Args:
            key: Key to store
            value: Value to store
            
        Hint: 
        - If key exists, update and mark as recently used
        - If at capacity, remove least recently used item first
        - Then add new item
        """

        #wrap this in try catch blocks
        if self.cache[key]:
            if len(self.cache) >= self.capacity:
                print("================Capacity Full================\n")
                print("1. Delete Least Used Item\n")
                print("2. Continue With Keeping Old items\n")
                userInput = input()
                if (int(userInput) == 1):
                    #logic to delete the least used item
                    pass
                elif (int(userInput) == 2):
                    #logic to continue
                    pass
                else:
                    #logic for edge cases
                    pass
                
        
        # TODO: Implement put logic
        pass
    
    def __len__(self):
        """Return current cache size."""
        # TODO: Return number of items
        return len(self.cache)
    
    def __repr__(self):
        return ""