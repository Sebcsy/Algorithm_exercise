#
# @lc app=leetcode.cn id=704 lang=python
#
# [704] 二分查找
#

# @lc code=start
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left=0
        right=len(nums)-1
        while left<=right:
            middle=(left+right)//2
            if nums[middle]>target:
                right=middle-1
            elif nums[middle]<target:
                left=middle+1
            else:
                return middle
        
        return -1

# @lc code=end

