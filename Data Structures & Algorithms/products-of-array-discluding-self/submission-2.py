class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod_no_zero = 1
        zero_positions = []

        for i, num in enumerate(nums):
            if num != 0: 
                prod_no_zero *= num
            else:
                zero_positions.append(i)

        if len(zero_positions) > 1:
            return [0] * len(nums)
        
        elif len(zero_positions) == 1:
            zeroed = [0] * len(nums)
            zeroed[zero_positions[0]] = prod_no_zero
            return zeroed

        else:
            answer = []
            for num in nums:
                answer.append(int(prod_no_zero / num))
            return answer

        