class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dedup = set(nums)
        if len(nums) != len(dedup):
            return True
        return False
        