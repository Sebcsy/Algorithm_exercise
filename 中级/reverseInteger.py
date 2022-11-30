class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==0:
            return 0
        x=str(x)
        if x[0]=='-':
            x=int(x[:0:-1])
            if -2**31 <x<2**31 - 1:
                return -x
            else:
                return 0
        else:
            x=int(x[::-1])
            if -2**31 <x<2**31 - 1:
                return x
            else:
                return 0