class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         if len(nums) > len(set(nums)):
            return True
         return False
         '''status = {nums:}
         j=1
         for num in range nums:
            status[num] = dict.append(num: +j)'''
