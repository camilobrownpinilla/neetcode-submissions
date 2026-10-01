from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurences = defaultdict(int)
        for num in nums:
            occurences[num] += 1

        nums_by_occurence = sorted(set(nums), key=lambda num: occurences[num], reverse=True)
        return nums_by_occurence[:k]
            