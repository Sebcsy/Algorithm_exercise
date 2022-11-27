class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        head=0
        tail=len(nums)-1
        index=0
        while index<= tail:
            if nums[index]==0:
                nums[head],nums[index]=nums[index],nums[head]
                head+=1
                index+=1
            elif nums[index]==1:
                index+=1
            elif nums[index]==2:
                nums[tail],nums[index]=nums[index],nums[tail]
                tail-=1
