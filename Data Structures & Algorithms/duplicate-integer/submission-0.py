class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lenght = len(nums)
        nums = set(nums)
        if  len(nums) == lenght:
            return False
        else:
            return True 
        