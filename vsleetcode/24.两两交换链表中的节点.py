#
# @lc app=leetcode.cn id=24 lang=python
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy_head=ListNode(next=head)
        pre=dummy_head
        while pre.next and pre.next.next:
            cur=pre.next
            post=pre.next.next

            #  pre(dummy_head)->cur(head)(0)->post(1)    变化前
            cur.next=post.next
            post.next=cur
            pre.next=post

            pre=cur
            # dummy_head->(0)->pre(1)->下一轮cur(2)->下一轮post(3)   变化后
        return dummy_head.next
# @lc code=end

