"""
Priority Task Queue Implementation - Skeleton

Your task: Implement a priority queue where lower priority numbers = higher priority
- add_task() should be O(log n)
- get_next_task() should be O(log n)
- peek() should be O(1)

Hint: Use Python's heapq module (min-heap)
"""

import heapq
from dataclasses import dataclass, field
from typing import Any
from datetime import datetime

"""When order=True, dataclasses automatically generates the rich comparison methods (__lt__, __le__, __gt__, __ge__)."""
"""Automatically creates __init__(), __repr__(), and __eq__()"""
@dataclass(order=True)
class Task:
    """Task with priority and metadata."""
    name: str = field(compare=False) 
    priority: int = field(compare=True)
    timestamp: datetime = field(compare=True, default_factory=datetime.now)
    data: Any = field(compare=False, default=None)

    def __repr__(self):
        return f"Task('{self.name}', priority={self.priority})"


class PriorityTaskQueue:
    """Priority queue for task scheduling."""
    """Tasks are compared by priority first, then timestamp if priorities are equal"""
    
    def __init__(self):
        """
        Initialize the priority queue.
        """
        self.heap = []
        self.counter = 0
    
    def add_task(self, name: str, priority: int, data: Any = None):
        """
        Add a task to the queue.
        
        Args:
            name: Task name/description
            priority: Priority level (1=highest, 10=lowest)
            data: Optional task data
        """
        # TODO: Create task
        # TODO: Push to heap (use heapq.heappush)
        # TODO: Increment counter
        if (priority < 1 and priority > 10):
            return "Value has to be in between 1 and 10"
        else:
            task = Task(name=name, priority=priority, data=data)
            heapq.heappush(self.heap, (-priority, self.counter, task))
            self.counter += 1
        
    
    def get_next_task(self) -> Task:
        """
        Remove and return highest priority task.
        
        Returns:
            Task object
            
        Raises:
            IndexError: If queue is empty
        """

        if (self.heap):
            return heapq.heappop(self.heap)[-1]
        else:
            raise IndexError 
        
    def peek(self) -> Task:
        """
        View highest priority task without removing it.
        
        Returns:
            Task object
            
        Raises:
            IndexError: If queue is empty
        """
        if (self.heap):
            return self.heap[0]
        else:
            raise IndexError
    
    def is_empty(self) -> bool:
        """Check if queue is empty."""
        # TODO: Return whether heap is empty
        pass
    
    def __len__(self):
        """Return number of tasks in queue."""
        # TODO: Return heap length
        pass
    
    def __repr__(self):
        """String representation of queue."""
        # TODO: Return formatted string of tasks
        pass


# Test your implementation
"""if __name__ == "__main__":
    print("=== Testing Priority Queue ===\n")
    
    queue = PriorityTaskQueue()
    
    # Test 1: Add tasks
    queue.add_task("Low priority task", priority=5)
    queue.add_task("High priority task", priority=1)
    queue.add_task("Medium priority task", priority=3)
    print(f"Added 3 tasks, queue size: {len(queue)}")
    print(f"Expected: 3\n")
    
    # Test 2: Peek
    next_task = queue.peek()
    print(f"Next task (peek): {next_task}")
    print(f"Queue size after peek: {len(queue)}")
    print(f"Expected: High priority task (priority=1), size=3\n")
    
    # Test 3: Process tasks in priority order
    print("Processing tasks:")
    while not queue.is_empty():
        task = queue.get_next_task()
        print(f"  → {task}")
    print(f"Expected: Tasks in order 1, 3, 5\n")
    
    # Test 4: Empty queue
    print(f"Queue is empty: {queue.is_empty()}")
    print(f"Expected: True")
    
    try:
        queue.get_next_task()
        print("ERROR: Should have raised IndexError!")
    except IndexError:
        print("✓ Correctly raised IndexError on empty queue")"""