class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for m in matrix:
            if target > m[-1]:
                continue
            else:
                if target in m:
                    return True
                else:
                    return False