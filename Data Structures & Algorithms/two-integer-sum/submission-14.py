class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            num = nums[i]
            diff = target - num
            for j in range(i+1, len(nums)):
                if nums[j] == diff:
                    return [i, j]
        raise ValueError("No TwoSum in list")