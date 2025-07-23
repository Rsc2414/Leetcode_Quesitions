class Solution:
    def makeFancyString(self, s: str) -> str:
        i = 0
        j = 1
        k = 2
        

        if len(s) < 3:
            return s
        s = list(s)

        
        while k < len(s):
            if s[i] == s[j] and s[j] == s[k]:
                s[i] = ''
            i += 1
            j += 1
            k += 1
        
        return ''.join(s)

        
