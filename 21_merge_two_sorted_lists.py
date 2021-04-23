'''
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

 
Example 1:

Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]


Example 2:

Input: l1 = [], l2 = []
Output: []


Example 3:

Input: l1 = [], l2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both l1 and l2 are sorted in non-decreasing order.
'''


##### Iteration #####

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1 is None and l2 is None:
            return None

        head = ListNode(0)  # ListNode{val: 0, next: None}
        current = head

        while l1 and l2:

            if l1.val > l2.val:
                current.next = l2
                l2 = l2.next

            else:  # l1.val <= l2.val
                current.next = l1
                l1 = l1.next

            current = current.next

        current.next = l1 or l2

        return head.next

# (runtime / memory)
#  28 ms / 13.9 MB



##### Recursion ##### 
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        if not l1: 
            return l2
        if not l2: 
            return l1
        if not l1 and not l2: 
            return None 
        
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else: # l1.val < l2.val:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
'''
# (runtime / memory)
#  32 ms / 14.2 MB
