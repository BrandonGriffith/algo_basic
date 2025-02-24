class IsPalindrome:
    def two_pointers(self, s: str) -> bool:
        filtered_str = ""
        for c in s:
            if c.isalnum():
                filtered_str += c.lower()
        n = len(filtered_str)
        for i in range(n // 2):
            if filtered_str[i] != filtered_str[n - 1 - i]:
                return False
        return True
