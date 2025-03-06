class ValidParentheses:
    def brute_force(self, s):
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()', '')
            s = s.replace('{}', '')
            s = s.replace('[]', '')
        return s == ''

    def stack(self, s):
        stack = []
        closing = {')' : '(', '}' : '{', ']' : '['}
        for x in s:
            if x in closing:
                if stack and stack[-1] == closing[x]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(x)
        return len(stack) == 0