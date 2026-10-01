class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Two pointer approach:
        # Start pointers at start and end
        # If sum(pointers) < target, tick forward pointer
        # If sum(pointers) > target, tick back pointer
        # Else, return pointers 

        f, b = 0, len(numbers) - 1 

        for _ in range(len(numbers)):
            fwd = numbers[f]
            bckwd = numbers[b]

            if fwd + bckwd < target:
                f += 1
            elif fwd + bckwd > target:
                b -= 1
            else:
                return [f + 1, b + 1]