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