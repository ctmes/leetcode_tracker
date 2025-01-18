class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            low, high = row[0], row[-1]

            if target < low or target > high:
                continue

            if target == low or target == high:
                print("Equals")
                return True
            
            l, r = 0, len(row) - 1
            while l <= r:
                m = (l+r) // 2

                if target == row[m]:
                    print("m found")
                    return True
                
                if target < row[m]:
                    r -= 1
                
                else:
                    l += 1

        return False

        

        
