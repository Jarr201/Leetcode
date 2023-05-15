class Solution:
    def addDigits(self, num: int) -> int:
        stack = [num]
        while stack and stack[-1] >= 10:
            num, tot = stack.pop(), 0
            while num > 0:
                tot += num % 10
                num = num // 10
            stack.append(tot)
        return num if not stack else stack[-1]