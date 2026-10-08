class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            print(False)
        freq_1 = [0]*26
        freq_2 = [0]*26

        for chari in s:
            index = ord(chari)-ord('a')
            freq_1[index]+=1

        for charii in t:
            index = ord(charii)-ord('a')
            freq_2[index]+=1
        return freq_1 == freq_2

        