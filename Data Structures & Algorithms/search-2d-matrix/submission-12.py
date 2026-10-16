class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) * len(matrix[0])
        while left < right:
            mid = left + ((right-left) // 2)
            mid_q, mid_r = divmod(mid,len(matrix[0]))
            if matrix[mid_q][mid_r] == target:
                return True
            elif matrix[mid_q][mid_r] < target:
                left = mid + 1
            else:
                right = mid
        return False
        