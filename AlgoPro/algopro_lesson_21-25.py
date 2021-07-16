#lesson 21
#Valid parethenses
class Solution(object):
    def isValid(self, s):
        #map to parethenes pair
        parens = {
            '[' : ']',
            '{' : '}',
            '(' : ')',
        }
        #map inverted of above map
        inv_parens = {v:k for k, v in parens.items()}
        stack = []
        for c in s:
            if c in parens:
                stack.append(c)
            elif c in inv_parens:
                if len(stack) == 0 or stack[-1] != inv_parens[c]:
                    return False
                else:
                    stack.pop()
        return len(stack) == 0

#test input
print(Solution().isValid('(){([])}'))
print(Solution().isValid('(){(['))