# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sum = curr = ListNode

        tmp = val = 0
        while tmp or l1 or l2:
            val=tmp
            if l1 :
                val+=l1.val
                l1= l1.next
            if l2:
                val+=l2.val
                l2= l2.next
            
            tmp = val // 10
            val = val % 10

            curr.next = ListNode(val)
            curr = curr.next
        
        return sum.next

