class Solution:
    def countPoints(self, rings: str) -> int:
        rods = dict()
        for i in range(0, len(rings), 2):
            color = rings[i]
            rod = rings[i + 1]

            if rod in rods:
                rods[rod].add(color)
            else:
                rods[rod] = set([color])
        
        rod_count = 0
        for rod in rods:
            if 'R' in rods[rod] and 'B' in rods[rod] and 'G' in rods[rod]:
                rod_count += 1
                
        return rod_count
