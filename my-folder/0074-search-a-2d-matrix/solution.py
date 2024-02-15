class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 1:
            return target in matrix[0]

        if len(matrix) == 2:
            return target in matrix[0] or target in matrix[1]
        
        midpoint = int(len(matrix)/2)
        midpointFirstIndex = matrix[midpoint][0]
        
        if target == midpointFirstIndex:
            return True

        if target < midpointFirstIndex:
            return self.searchMatrix(matrix[:midpoint], target)
        
        elif target > midpointFirstIndex:
            return self.searchMatrix(matrix[midpoint:], target)
