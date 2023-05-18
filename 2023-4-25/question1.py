class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        tag = (dividend < 0) != (divisor < 0) # 被除数和除数不同时为负数时，商为负数
        dividend = abs(dividend)
        divisor = abs(divisor) # 对被除数和除数取绝对值
        if dividend < divisor: # 被除数小于除数时，商为0
            return 0
        res, div, temp = 0, divisor, 1
        while dividend >= divisor:
            while dividend > (div << 1): # 让除数每次*2，temp记录除数的个数
                div <<= 1
                temp <<= 1
            dividend -= div # 减去temp个divisor
            div = divisor # 复位div
            res += temp # 加上每次循环的个数
            temp = 1 # 复位temp

        res = -res if tag else res
        return res if -2**31 <= res <= 2**31 - 1 else min(max(res, -2**31), 2**31 - 1)