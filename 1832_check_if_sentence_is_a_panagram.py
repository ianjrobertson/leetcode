class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        letters = set()
        for c in sentence:
            letters.add(c)
        
        return len(letters) == 26
