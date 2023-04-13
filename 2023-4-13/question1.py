class Solution:
    def isPalindrome(self, x: int) -> bool:
        ans = str(x)
        n = len(ans) // 2
        for i in range(n):
            if ans[i] == ans[len(ans) - i - 1]:
                continue
            else:
                return False
        return True