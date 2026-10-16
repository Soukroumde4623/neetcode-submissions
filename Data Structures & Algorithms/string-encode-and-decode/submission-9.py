class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = ""
        if len(strs)==0:
            return "" 
        for p in strs:
            encode += f"{len(p)}#{p}"
        return encode

    def decode(self, s: str) -> List[str]:
        liste = list()
        i =0        
        while i<len(s):
             j =i
             while s[j]!="#":
                    j+=1
             len_string = int(s[i:j])
             start = j+1
             end = j+1+len_string
             string = s[start:end]
             liste.append(string)
             i =end
             
        return liste
