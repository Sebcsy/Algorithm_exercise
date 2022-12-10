#
# @lc app=leetcode.cn id=209 lang=python
#
# [209] 长度最小的子数组
#

# @lc code=start
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        i=0
        result=float("inf")
        sum=0
        for j in range(len(nums)):
            sum+=nums[j]
            # 注意这里是while，当resul大于等于目标时要开始循环向前移动起始位置。
            while sum>=target:
                result=min(result,j-i+1)
                sum-=nums[i]
                i+=1
        return 0 if result==float("inf") else result
# @lc code=end

