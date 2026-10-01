class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod_without_0 = 1
        zero_indices = []
        output = []
        for i, num in enumerate(nums):
            if num == 0: 
                zero_indices.append(i)
            else:
                prod_without_0 *= num

        if len(zero_indices) > 1: return [0] * len(nums)
        for i, num in enumerate(nums):
            # Case where input has 0s
            if len(zero_indices) != 0:
                if i in zero_indices:
                    output.append(prod_without_0)
                else:
                    output.append(0)
            # Case where input does not have 0s
            else:
                output.append(prod_without_0 // num)

        return output