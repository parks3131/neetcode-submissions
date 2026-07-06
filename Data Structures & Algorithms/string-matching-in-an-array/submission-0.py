class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []
        for word in words:
            for innerloopwords in words:
                if innerloopwords != word and innerloopwords in word and innerloopwords not in result:
                    result.append(innerloopwords)
        return result
                