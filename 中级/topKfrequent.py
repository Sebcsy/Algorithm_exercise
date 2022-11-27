import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        map={}
        for i in range(len(nums)):
            map[nums[i]]=map.get(nums[i],0)+1
        