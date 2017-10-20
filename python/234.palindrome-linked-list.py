# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        if(head == None or head.next == None):
            return True

        slow = head
        fast = head

        while(fast.next != None and fast.next.next != None):
            slow = slow.next
            fast = fast.next.next

        last = self.reverseList(slow.next)

        while(last):
            if(last.val == head.val):
                last = last.next
                head = head.next
            else:
                return False

        return True

    
    def reverseList(self, head):

        if(head == None or head.next == None):
            return head

        front = None
        mid = head
        end = head.next

        while(end != None):
            mid.next = front
            front = mid
            mid = end
            end = end.next
            mid.next = front

        return mid
