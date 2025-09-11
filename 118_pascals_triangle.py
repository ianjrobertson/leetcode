class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for row in range(numRows):
            triangle_row = []
            if row == 0:
                triangle.append([1])
                continue
            if row == 1:
                triangle.append([1,1])
                continue
            for col in range(0, row + 1):
                if col == 0 or col == row:
                    triangle_row.append(1)
                else:
                    value = triangle[row - 1][col - 1] + triangle[row - 1][col]
                    triangle_row.append(value) 
            triangle.append(triangle_row)
    
        return triangle

                

