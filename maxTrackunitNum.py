class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        unitNum=sorted(boxTypes ,key=lambda x: -x[1])
        res=0
        for i in unitNum:
            res+=i[1]*min(i[0],truckSize)
            truckSize-=i[0]
            if truckSize<=0:
                break
        return res