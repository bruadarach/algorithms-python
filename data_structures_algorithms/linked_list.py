class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        print_list = '['
        current = self.head
        while True:
            print_list += str(current)
            if current.next == None:
                break
            current = current.next
            print_list += ', '
        print_list += ']'
        return print_list

    def __len__(self):
        counter = 1
        current = self.head
        if self.head is None:
            return None
        while current.next:
            current = current.next
            counter += 1
        return counter

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        counter = 1
        current = self.head
        if position < 1:
            return None
        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter += 1
        return None

    def insert(self, new_element, position):
        counter = 1
        current = self.head
        if position > 1:
            while current and counter < position:
                if counter == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                counter += 1
        elif position == 1:
            new_element.next = self.head
            self.head = new_element

    def delete(self, value):
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next


if __name__ == "__main__":

    e1 = Element(1)
    e2 = Element(2)
    e3 = Element(3)
    e4 = Element(4)
    e5 = Element(5)

    ll = LinkedList(e1)
    ll.append(e2)
    ll.append(e3)
    ll.append(e4)

    print(ll.head.value)  # 1
    print(ll.head.next.value)  # 2
    print(ll.head.next.next.value)  # 3
    print(ll.head.next.next.next.value) # 4 

    print(ll.get_position(1).value)  # 1
    print(ll.get_position(2).value)  # 2
    print(ll.get_position(3).value)  # 3
    print(ll.get_position(4).value)  # 4

    ll.insert(e5, 3)  # e1, e2, e5 , e3, e4
    print(ll.get_position(3).value)  # 5

    ll.delete(1)
    print(ll.get_position(1).value)  # 2
    print(ll.get_position(2).value)  # 5
    print(ll.get_position(3).value)  # 3
    print(ll.get_position(4).value)  # 4

    print('LinkedList :', ll)  # [2, 5, 3, 4]
    print('LinkedList length:', len(ll)) # 4 
