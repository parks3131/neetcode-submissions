class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        length = len(strs)
        dummy = strs
        output = []
        t=0
        while length !=0:
            indices=[]
            output.append([])
            output[t].append(strs[0])

            for i in range(1,length):
                if(sorted(strs[0]) == sorted(strs[i])):
                    output[t].append(strs[i])
                    indices.append(i)
                    
            for i in reversed(indices):
                dummy.pop(i)
            dummy.pop(0)
            strs = dummy
            t+=1
            length = len(dummy)
        return output
            
            