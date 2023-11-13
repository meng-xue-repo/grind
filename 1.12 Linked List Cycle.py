# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


'''
According to ChatGpt, if a class does not define custom __hash__ and __eq__ methods, the default hash value and equality check is based on object's IDENTITY (Memory Address).
When you want to consider objects equal based on their CONTENT rather than their identity, it's recommended to define custom __hash__ and __eq__
'''
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        node = head

        while node and node not in visited:
            visited.add(node)
            node = node.next

        return node in visited


########## Two pointers solution ##########
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        fast = slow = head

        while fast and slow and slow.next:
            fast = fast.next
            slow = slow.next.next

            if fast == slow:
                return True

        return False
