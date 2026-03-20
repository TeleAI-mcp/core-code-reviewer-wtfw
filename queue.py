class Queue:
    """A simple queue implementation for code review tasks."""
    
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if self.items:
            return self.items.pop(0)
        return None
    
    def is_empty(self):
        return len(self.items) == 0
