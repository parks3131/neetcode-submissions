class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for string in strs:
            count = [0]*26
            for i in string:
                count[ord(i) - ord("a")]+=1
            hashmap[tuple(count)].append(string)
        return [i for i in hashmap.values()]
