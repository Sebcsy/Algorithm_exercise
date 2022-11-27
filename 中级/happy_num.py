class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        num=0
        table=[]
        while True:
            temp=str(n)
            for i in temp:
                j=int(i)
                num+=j**2
            if num ==1:
                return True
            
            if num in table:
                return False
            
            table.append(num)
            n=num
            num=0
            