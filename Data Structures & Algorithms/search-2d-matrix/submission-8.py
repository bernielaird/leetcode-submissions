class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        while l <= r:
            temp = (l + r) // 2
            if matrix[temp][0] == target:
                return True
            if matrix[temp][0] < target:
                l = temp + 1
            else:
                r = temp - 1

        temp = r

        if temp < 0:
            return False

        array = matrix[temp]
        l, r = 0, len(matrix[temp]) - 1
        while l <= r:
            val = (l + r) // 2
            if array[val] == target:
                return True
            if array[val] < target:
                l = val + 1
            else:
                r = val - 1

        return False