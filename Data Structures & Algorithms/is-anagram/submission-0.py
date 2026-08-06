class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}

        s_len = len(s)
        t_len = len(t)

        if s_len != t_len:
            return False

        for idx in range(s_len):
            if s[idx] in s_dict:
                s_dict[s[idx]] += 1
            else:
                s_dict[s[idx]] = 1

            if t[idx] in t_dict:
                t_dict[t[idx]] += 1
            else:
                t_dict[t[idx]] = 1
        
        return s_dict == t_dict