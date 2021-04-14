'''
Given the head of a singly linked list, reverse the list, and return the reversed list.

 
Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]


Example 2:

Input: head = [1,2]
Output: [2,1]


Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 

Follow up: 

A linked list can be reversed either iteratively or recursively. Could you implement both?
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


##### SOLUTION : ITERATION #####
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        # self.head = head
        # current = self.head
        current = head
        previous = None

        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next

        return previous

# (runtime / memory)
#  28 ms / 15.7 MB



##### SOLUTION : RECURSION #####
'''
class Solution:
    def reverseList(self, head: ListNode, previous=None) -> ListNode:
        
        if not head:
            return previous
  
        current, head.next = head.next, previous
        return self.reverseList(current, head)
'''
# (runtime / memory)
#  40 ms / 20.4 MB

