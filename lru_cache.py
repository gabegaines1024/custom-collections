"""
LRU (Least Recently Used) Cache Implementation

An LRU cache removes the least recently used item when it reaches capacity.
Use cases: caching API responses, database queries, expensive computations.

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
        # If key already exists, update it and move to end (most recent)
        if key in self.cache:
            self.cache.move_to_end(key)
            self.cache[key] = value
            return
        
        # If at capacity, remove least recently used item
        if len(self.cache) >= self.capacity:
            # Remove first item (least recently used)
            least_used = next(iter(self.cache))
            print(f"Cache full! Evicting: {least_used} = {self.cache[least_used]}")
            del self.cache[least_used]
        
        # Add new item (will be at end = most recently used)
        self.cache[key] = value

    def items(self):
        """Return list of (key, value) tuples."""
        return list(self.cache.items())

    def __str__(self):
        """Return user-friendly string."""
        if not self.cache:
            return "LRUCache (empty)"
        items = ', '.join(f"{k}: {v}" for k, v in self.cache.items())
        return f"LRUCache({len(self)}/{self.capacity}): [{items}]"
    
    def __len__(self):
        """Return current cache size."""
        return len(self.cache)
    
    def __repr__(self):
        """Return string for developer debugging"""
        return f"LRUCache({self.cache}, {self.capacity})"
    
# Test implementation
if __name__ == "__main__":
    print("=== Testing LRU Cache ===\n")
    
    cache = LRUCache(3)
    
    # Test 1: Basic operations
    cache.put("a", 1)
    cache.put("b", 2)
    cache.put("c", 3)
    print(f"After adding a, b, c:")
    print(f"  Items: {cache.items()}")
    print(f"  Size: {len(cache)}")
    print(f"  String: {cache}")
    print(f"  Repr: {repr(cache)}\n")
      
    # Test 2: Get operation
    result = cache.get("a")
    print(f"Getting 'a': {result}\n")

    
    
    # Test 3: Eviction
    cache.put("d", 4)  # Should evict 'b' (least recently used)
    print(f"After adding 'd': {cache}\n")
    print(f"  Items: {cache.items()}")
    print(f"  Size: {len(cache)}")
    print(f"  String: {cache}")
    print(f"  Repr: {repr(cache)}\n")
    
    
    # Test 4: Update existing
    cache.put("a", 100)
    print(f"After updating 'a' to 100:\n")
    print(f"  Items: {cache.items()}")
    print(f"  Size: {len(cache)}")
    print(f"  String: {cache}")
    print(f"  Repr: {repr(cache)}\n")
    print(f"Get 'a': {cache.get('a')}")
