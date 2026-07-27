# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
          return head

        curr = head.next
        prev = head
        prev.next = None
        print(head)
        print(curr.val)
        while curr :
          head = curr
          print(head, curr)
          curr = curr.next
          head.next = prev
          prev = head

        return head