#
# @lc app=leetcode.cn id=977 lang=python
#
# [977] 有序数组的平方
#

# @lc code=start
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        head=0
        tail=len(nums)-1
        k=len(nums)-1
        ans=[0]*len(nums)
        while head<=tail:
            if nums[head]**2<nums[tail]**2:
                ans[k]=nums[tail]**2
                tail-=1
            else:
                ans[k]=nums[head]**2
                head+=1
            k-=1
        return ans
# @lc code=end

