class IsAnagram:
    def sorting(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
    
    def hashing(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash = {}
        for i in range(len(s)):
            if s[i] in hash:
                hash[s[i]] += 1
            else:
                hash[s[i]] = 1
        for i in range(len(t)):
            if t[i] in hash and hash[t[i]] > 0:
                hash[t[i]] -= 1
            else:
                return False
        return True