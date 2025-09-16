class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        a = points[0]
        b = points[1]
        c = points[2]

        if a == b or b == c or a == c:
            return False

        slope_ab = self.get_slope(a, b)
        slope_bc = self.get_slope(b, c)

        return slope_ab != slope_bc

    def get_slope(self, point_1, point_2):
        if point_2[0] == point_1[0]:
            return None
        return (point_2[1] - point_1[1]) / (point_2[0] - point_1[0])
