# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if(head == None):
            return None

        prev = None
        curr = head
        prec = head.next

        while(prec != None):
            curr.next = prev
            prev = curr
            curr = prec
            prec = prec.next

        curr.next = prev
        
        return curr
