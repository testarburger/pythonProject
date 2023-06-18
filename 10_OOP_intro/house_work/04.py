class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return len(self.items) == self.capacity

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full. Cannot enqueue item:", item)
        else:
            self.items.append(item)
            print("Enqueued item:", item)

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue item.")
        else:
            item = self.items.pop(0)
            print("Dequeued item:", item)


class Ssaki:
    def __init__(self, gatunek):
        self.gatunek = gatunek

    def jest_ssakiem(self):
        print(self.gatunek, "jest ssakiem.")


queue1 = Queue(5)
queue2 = Queue(3)
queue3 = Queue(2)

queue1.enqueue("A")
queue1.enqueue("B")
queue1.enqueue("C")

queue2.enqueue(1)
queue2.enqueue(2)

queue3.enqueue("X")
queue3.enqueue("Y")

queue1.dequeue()
queue1.dequeue()

queue2.dequeue()

queue3.dequeue()

wilk = Ssaki("Wilk")
kon = Ssaki("Koń")
ssaki = Ssaki("Ssaki")

wilk.jest_ssakiem()
kon.jest_ssakiem()
ssaki.jest_ssakiem()
