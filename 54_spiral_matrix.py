class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # right till boundary
        # down till boundary
        # left till boundary
        # up till boundary

        # when do we stop? when len(list) == len(matrix) * len(matrix[0]) ?

        right = len(matrix[0])
        down = len(matrix)
        left = 0
        up = 0

        spiral = []
        num_elements = len(matrix) * len(matrix[0])

        row = 0
        col = -1

        while True:
            for _ in range(left, right):
                col += 1
                spiral.append(matrix[row][col])
                if len(spiral) == num_elements:
                    return spiral
            up += 1
            for _ in range(up, down):
                row += 1
                spiral.append(matrix[row][col])
                if len(spiral) == num_elements:
                    return spiral
            right -= 1
            for _ in range(right, left, -1):
                col -= 1
                spiral.append(matrix[row][col])
                if len(spiral) == num_elements:
                    return spiral
            down -= 1
            for _ in range(down, up, -1):
                row -= 1
                spiral.append(matrix[row][col])
                if len(spiral) == num_elements:
                    return spiral
            left += 1
        
        return spiral

