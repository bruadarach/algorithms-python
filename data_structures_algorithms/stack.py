class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
    
    def insert_first(self, new_element):
        if self.head:
            new_element.next = self.head 
            self.head = new_element 
        else:
            self.head = new_element

    def delete_first(self):
        if self.head:
            deleted = self.head
            self.head = self.head.next 
            deleted.next = None
            return deleted
        else:
            return None

class Stack(object):
    def __init__(self, top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        self.ll.insert_first(new_element)

    def pop(self):
        return self.ll.delete_first()


if __name__ == "__main__":
    e1 = Element(1)
    e2 = Element(2)
    e3 = Element(3)
    e4 = Element(4)

    # Start setting up a Stack
    stack = Stack(e1)

    # Test stack functionality
    stack.push(e2)
    stack.push(e3)
    print(stack.pop().value) # 3
    print(stack.pop().value) # 2 
    print(stack.pop().value) # 1 
    print(stack.pop()) # None
    
    stack.push(e4)
    print(stack.pop().value) # 4
