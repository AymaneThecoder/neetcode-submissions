class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()
        for num in strs:
            k =sorted(num)
            s =  "".join(k)
            if s in d:
                d[s].append(num)
            else:
                d[s]= [num]
        return list(d.values())

                
        