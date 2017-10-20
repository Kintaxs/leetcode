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
        
        if(head == None or head.next == None):
            return head

        front = None
        end = head.next

        while(end != None):
            head.next = front
            front = head
            head = end
            end = end.next
            head.next = front

        return head
