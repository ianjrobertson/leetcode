class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        split = []
        for word in words:
            split_words = word.split(separator)
            split = [*split, *split_words]

        clean_split = []
        for word in split:
            if word != '':
                clean_split.append(word)
        
        return clean_split
