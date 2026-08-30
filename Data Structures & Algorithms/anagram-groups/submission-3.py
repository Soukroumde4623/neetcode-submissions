class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups ={}

        for st in strs:
            key = "".join(sorted(st))
            if key not in groups:
                groups[key]=[]

            groups[key].append(st)
        
        return list(groups.values())