class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, (len(numbers) - 1)
        for i in range(len(numbers)):
            temp = numbers[l] + numbers[r]
            if temp == target:
                return [l + 1, r + 1]
            if temp < target:
                l += 1
            else:
                r -= 1