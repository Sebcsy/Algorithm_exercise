#
# @lc app=leetcode.cn id=707 lang=python
#
# [707] 设计链表
#

# @lc code=start
class Node(object):
    def __init__(self, x=0):
        self.val = x
        self.next = None

class MyLinkedList(object):

    def __init__(self):
        self.head=Node()
        self.size=0

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index<0 or index>=self.size:
            return -1
        cur = self.head.next
        while index:
            cur=cur.next
            index-=1
        return cur.val



    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        new_Node=Node(val)
        new_Node.next=self.head.next
        self.head.next=new_Node
        self.size+=1


    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        cur=self.head
        while cur.next:
            cur=cur.next

        new_Tail=Node(val)
        cur.next=new_Tail
        self.size+=1


    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index<0:
            self.addAtHead(val=val)
            return
        elif index==self.size:
            self.addAtTail(val)
            return
        elif index>self.size:
            return

        new_Node=Node(val)
        cur=self.head
        while index:
            cur=cur.next
            index-=1
        new_Node.next=cur.next
        cur.next=new_Node
        self.size+=1

                


    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index<0 or index>=self.size:
            return
        
        cur=self.head
        while index:
            cur=cur.next
            index-=1
        cur.next=cur.next.next
        self.size-=1




# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end

