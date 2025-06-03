class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        match = dict()
        words = s.split()

        if len(pattern) != len(words): 
            return False

        for i in range(len(pattern)):
            letter = pattern[i]
            word = words[i]

            if letter in match.keys():
                if match[letter] != word:
                    return False
            elif word in match.values():
                return False
            else:
                match[letter] = word
        return True
