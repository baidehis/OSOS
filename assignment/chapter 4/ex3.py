
class StackBasedQueue():
    def __init__(self):
        self._InboundStack = Stack()
        self._OutboundStack = Stack()
        self._size = 0
        
    def __repr__(self):
        plural = '' if self._size == 1 else 's'
        values = [c for c in self._InboundStack]
        values.extend([c for c in self._OutboundStack][::-1])
        return f'<StackBasedQueue ({self._size} element{plural}): [{", ".join(values)}]'

    def enqueue(self, data):
          # push to inbound stack
         self._InboundStack.push(data)
         self._size += 1

    def dequeue(self):
         # if queue is empty
        if self._size == 0:
            return None
        
        # if outbound stack is empty, transfer elements
        if len(self._OutboundStack) == 0:
            while len(self._InboundStack) > 0:
                self._OutboundStack.push(self._InboundStack.pop())
        
        self._size -= 1
        return self._OutboundStack.pop()
    

q = StackBasedQueue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")

print(q.dequeue())  # A
print(q.dequeue())  # B
