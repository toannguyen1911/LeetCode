class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            two_sum = numbers[left] + numbers[right]

            if two_sum == target:
                return [left + 1, right + 1]
            if two_sum < target:
                left += 1
                continue
            right -= 1
            
        return [-1, -1]