'''
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.


Example 1:

Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]


Example 2:

Input: head = [], val = 1
Output: []


Example 3:

Input: head = [7,7,7,7], val = 7
Output: []
 

Constraints:

The number of nodes in the list is in the range [0, 10^4].
1 <= Node.val <= 50
0 <= k <= 50
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

##### Iteration #####
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:

        current = head
        previous = None

        while current:

            if current.val == val:
                if previous:  # curret.val != val
                    previous.next = current.next
                    current = previous

                else:  # no previous? head.val == val:
                    head = head.next

            else:  # current.val != val
                previous = current

            current = current.next
        return head

# (runtime / memory)
#  64 ms / 17.2 MB


##### Recursion #####
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:

        if not head:
            return None

        if head.val == val:
            head = self.removeElements(head.next, val)
        else:
            head.next = self.removeElements(head.next, val)

        return head
'''
# (runtime / memory)
#  76 ms / 25.6 MB
