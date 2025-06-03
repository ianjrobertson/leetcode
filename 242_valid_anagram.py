class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # okay so we want to see if all the letters in s are in t exactly 1.
        # so we could make a distribution of letters using a map. 

        # then iteratre through t, and decrement the frequency whenever we encounter the same letter

        # if the values of the dict are all zero. return true

        distribution = dict()

        for c in s:
            if c in distribution.keys():
                distribution[c] += 1
            else:
                distribution[c] = 1
        
        for c in t:
            if c in distribution.keys(): ## Could modify to say if it is 0, delete it from the keys. 
                distribution[c] -= 1
            else:
                return False

        for num in distribution.values():
            if num != 0:
                return False
    
        return True
