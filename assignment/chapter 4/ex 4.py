class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0


def enqueue(self, value):
    new_node = ListNode(value)

    if self.head is None:
        self.head = self.tail = new_node
    else:
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

        self.size += 1

def dequeue(self):
    if self.tail is None:
        raise IndexError("dequeue from empty queue")
            
    value = self.tail.value

    if self.head == self.tail:
        self.head = self.tail = None
    else:
        self.tail = self.tail.prev
        self.tail.next = None

        self.size -= 1
        return value
def __repr__(self):
    elements = []
    current = self.head

    while current:
        elements.append(str(current.value))
        current = current.next

        return f"<Queue ({self.size} elements): [{', '.join(elements)}]>"


myQueue = Queue()

myQueue.enqueue('A')
myQueue.enqueue('B')
myQueue.enqueue('C')
print(myQueue)
