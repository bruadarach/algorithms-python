'''
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.
Return the decimal value of the number in the linked list.

 
Example 1:
(1) ---> (0) ---> (1)

Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10

Example 2:

Input: head = [0]
Output: 0

Example 3:

Input: head = [1]
Output: 1

Example 4:

Input: head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
Output: 18880

Example 5:

Input: head = [0,0]
Output: 0
 

Constraints:

The Linked List is not empty.
Number of nodes will not exceed 30.
Each node's value is either 0 or 1.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:

        current = head
        binary_list = []
        while current:
            binary_list.append(current.val)
            current = current.next

        result = 0
        for i, val in enumerate(binary_list[::-1]):
            result += (2**i)*val
        return result

# (runtime / memory)
#  28 ms / 14.3 MB


'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        if head.next == None:
          return head.val
        
        result = []
        while head:
          result.append(str(head.val))
          head = head.next

        return int("".join(result), 2)
'''
# (runtime / memory)
#  20 ms / 14.3 MB



'''
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        answer = 0
        while head: 
            answer = 2*answer + head.val 
            head = head.next 
        return answer 
'''
# (runtime / memory)
#  32 ms / 14.2 MB
