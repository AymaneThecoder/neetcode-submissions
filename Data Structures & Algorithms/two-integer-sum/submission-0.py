class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i, num in enumerate(nums):
            search = target - num
            if search in d:
                return [ d[search],i]
            else:
                d[num]= i  
        


