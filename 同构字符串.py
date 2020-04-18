class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmaps = {}
        hashmapt = {}
        for i in range(len(s)):
            if s[i] not in hashmaps and t[i] not in hashmapt:
                hashmaps[s[i]] = i
                hashmapt[t[i]] = i
            else:
                if hashmaps.get(s[i]) == None or hashmapt.get(t[i]) == None:
                    return False
                else:
                    if (hashmaps.get(s[i]) != hashmapt.get(t[i])):
                        return False
        return True
