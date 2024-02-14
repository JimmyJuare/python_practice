class Queue:
    def __init__(self) -> None:
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)
    def denqueue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print('queue is empty')
            
    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print('queue is empty')
    def size(self):
        return len(self.items)

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.denqueue()
print(queue.size())
print(queue.front())
