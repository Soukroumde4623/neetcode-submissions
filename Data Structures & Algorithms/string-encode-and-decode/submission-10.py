
from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        encode = ""
        for p in strs:
            encode += f'{len(p)}#{p}'
        return encode

    def decode(self, s: str) -> List[str]:
        liste = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            len_string = int(s[i:j])
            debut = j + 1
            fin = debut + len_string
            string = s[debut:fin]
            liste.append(string)
            i = fin

        return liste
