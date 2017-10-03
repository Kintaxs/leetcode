# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        fast = slow = head

        while(fast != None and fast.next != None):
            slow, fast = slow.next, fast.next.next
            if(fast == slow):
                return True
        return False
