#
# @lc app=leetcode.cn id=203 lang=python
#
# [203] 移除链表元素
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head==None:
            return None
        fakehead = ListNode(next=head)
        curr=fakehead
        while curr.next!=None:
            if curr.next.val==val:
                curr.next=curr.next.next
            else:
                curr=curr.next
        return fakehead.next
# @lc code=end