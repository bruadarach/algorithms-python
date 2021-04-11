'''
Given a non-empty, singly linked list with head node head, return a middle node of linked list.
If there are two middle nodes, return the second middle node.
 

Example 1:

Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.


Example 2:

Input: [1,2,3,4,5,6]
Output: Node 4 from this list (Serialization: [4,5,6])
Since the list has two middle nodes with values 3 and 4, we return the second one.
 

Note:

The number of nodes in the given list will be between 1 and 100.
'''


# Definition for singly-linked list.

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

# (runtime / memory)
#  28 ms / 14.1 MB



'''
class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution(object):
    
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
        
    def middleNode(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
 

if __name__ == "__main__":
    
    e1 = Element(1)
    e2 = Element(2)
    e3 = Element(3)
    e4 = Element(4)
    e5 = Element(5)
    e6 = Element(6)
    
    ll = Solution(e1)
    ll.append(e2)
    ll.append(e3)
    ll.append(e4)
    ll.append(e5)
    ll.append(e6)
    
    print(ll.head.value)
    print(ll.head.next.value)
    print(ll.head.next.next.value)
    print(ll.head.next.next.next.value)
    print(ll.head.next.next.next.next.value)
    print(ll.head.next.next.next.next.next.value)
    
    answer = ll.middleNode()
    print('The answer is:', answer.value)
'''
