class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        # create a dictionary of each slot
        # make a frequency of how often each slot occurs
        # find the maximum number of slots, subtract that from the cols
        # thats the best

        # make a running sum of the index of the cut

        # add that index to the dictionary

        # Find the max count, subtract that from numRows, that sthe cut. 

        cut_frequency = defaultdict(int)
        wall_sum = sum(wall[0])
        if wall_sum == 1:
            return len(wall)

        for i in range(len(wall)):
            running_sum = 0
            for j in range(len(wall[i])):
                running_sum += wall[i][j]
                cut_frequency[running_sum] = cut_frequency[running_sum] + 1
        cut_frequency[wall_sum] = 0
        max_cut = max(cut_frequency.values())
        return len(wall) - max_cut

        # so the issue is, we are counting the end right now. We can pop off the max,
        ## how do we handle the case when
        
