"""

Docker hub location of the container:

https://hub.docker.com/r/930209111/assign1
"""

class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        stack = []
        match = [0 for i in range(0, len(s))]
        for i, c in enumerate(s):
            if c == '{':
                stack.append(i)
            elif c == '}' and len(stack) != 0:
                match[i] = match[stack[-1]] = 1
                stack.pop()

        ans, temp = 0, 0
        for i, c in enumerate(match):
            if match[i]:
                temp = temp + 1
                ans = max(ans, temp)
            else:
                temp = 0
        return ans, match



s = Solution()

"""
Paranthesis reference input {{}}}{
"""

target = '{{}}}{'
depth, match = s.longestValidParentheses(target)
# print(depth, match)
result = ''
for i, flag in enumerate(match):
    if flag:
        result += target[i]

print(result)