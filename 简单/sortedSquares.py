class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        head=0
        tail=len(nums)-1
        n=len(nums)-1
        res=[-1]*len(nums)
        while head <= tail:
            left=nums[head]**2
            right=nums[tail]**2
            if left>right:
                res[n]=left
                head+=1
            else:
                res[n]=right
                tail-=1
            n-=1
        return res