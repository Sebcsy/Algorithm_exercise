# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lengthA=0
        lengthB=0
        currA,currB=headA,headB
        while(currA): 
            lengthA+=1
            currA=currA.next
        while(currB):
            lengthB+=1
            currB=currB.next
        while lengthA!=lengthB:
            if lengthA>lengthB:
                headA=headA.next
                lengthA-=1
            else:
                headB=headB.next
                lengthB-=1
        while headB!=headA:
            headA=headA.next
            headB=headB.next
        
        return headA