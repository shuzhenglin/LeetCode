class Solution:
    def myPow(self, x: float, n: int) -> float:
        neg = n < 0
        n = abs(n)
        res = 1
        while n:
            if n&1: # 如果n为奇数,将多出的一项x乘入res
                res *= x
            x *= x
            n = n >> 1 # 每次让x=x^2,n每次就要除以2
        return 1/res if neg else res