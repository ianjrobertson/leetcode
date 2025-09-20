class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_count = dict()
        for jewel in jewels:
            jewel_count[jewel] = 0
        
        for stone in stones:
            if stone in jewel_count:
                jewel_count[stone] += 1
        
        return sum(jewel_count.values())
