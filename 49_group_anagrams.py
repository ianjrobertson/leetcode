class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps = dict()

        for word in strs: # O(n)
            sorted_word = "".join(sorted(word))
            if sorted_word in maps.keys():
                curr_anagrams = maps[sorted_word]
                curr_anagrams.append(word)
            else:
                maps[sorted_word] = [word]
        return list(maps.values())
                    
