class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            left, right = 0, len(row) - 1
            while left <= right:
                mid = (left+right) // 2
                guess = row[mid]
                if guess == target:
                    return True
                elif guess > target:
                    right -= 1
                else:
                    left += 1
        return False