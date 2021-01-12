
"""
Make a Queue class using a list
# Hint: You can use any Python list method you'd like! 
"""

class Queue(object):
    def __init__(self, head=None):
        self.storage = [head]

    def enqueue(self, new_element):
        self.storage.append(new_element) # 맨 마지막에 값 추가 

    def peek(self):
        return self.storage[0]

    def dequeue(self):
        return self.storage.pop(0) # 맨 처음값 삭제 & 반환


if __name__ == '__main__':
    # Setup
    q = Queue(1)
    q.enqueue(2)
    q.enqueue(3)

    # Test peek
    print(q.peek()) # 1

    # Test dequeue
    print(q.dequeue()) # 1

    # Test enqueue
    q.enqueue(4)

    print(q.dequeue()) # 2
    print(q.dequeue()) # 3 
    print(q.dequeue()) # 4 

    q.enqueue(5)
    print(q.peek()) # 5

