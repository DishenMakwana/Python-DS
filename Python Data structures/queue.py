class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.is_empty():
            return 'Queue is empty'
        return self.queue.pop(0)

    def is_empty(self):
        if len(self.queue) <= 0:
            return True
        return False

    def state(self):
        if self.is_empty():
            return 'Queue is empty'
        return self.queue

    def size(self):
        return len(self.queue)


queue = Queue()

# Operations on empty queue
print(queue.state())
print(queue.dequeue())
print(queue.size())
print(queue.is_empty())

# Adding data to queue
queue.enqueue(9)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(90)

# Operations after enqueuing
print('Queue Size:',queue.size())
print('Current queue:',queue.state())
print('Dequeue Operation ',queue.dequeue())
print('Current queue: ',queue.state())
print('Dequeue Operation ',queue.dequeue())
print('Current queue: ',queue.state())
print('Queue empty? ',queue.is_empty())
print('Queue Size: ',queue.size())