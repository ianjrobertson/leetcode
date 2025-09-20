class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # so maybe we have a dictionary
        # the key is the number, the value is a list of indexes. 
        # 3 numbers
        # [0], 2 after, make 2 pairs
        # [1], 1 after, make 1 pair
        # [2], 0 after, make 0 pair = 3 pair

        # 4 numbers
        # [0], 3 after, make 3 pairs
        # [1], 2 after, make 2 pairs
        # [2], 1 after, make 1 pair
        # [0], 0 after, make 0 pair = 6 pair

        # 5 numbers
        # 4,3,2,1,0 = 10 5(5 - 1) / 2
        # 6 numbers
        # 5,4,3,2,1,0 = 15 6(6 - 1)

        dist = defaultdict(int)
        pairs = 0

        for num in nums: 
            dist[num] += 1
        
        for key in dist:
            pairs += (dist[key] * (dist[key] - 1)) / 2

        return math.floor(pairs)
            
