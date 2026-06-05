class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_D = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in nums_D:
                return [nums_D[diff], i]
            nums_D[n] = i
