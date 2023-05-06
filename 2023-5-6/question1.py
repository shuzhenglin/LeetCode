class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1 = num1[::-1]
        num2 = num2[::-1]
        temp_list = []
        for a in num1:
            carry = 0
            ans = ''
            for b in num2:
                ans += str((int(a)*int(b) + carry) % 10)
                carry = (int(a)*int(b) + carry) // 10
            if carry > 0:
                ans += str(carry)
            temp_list.append(ans[::-1])
        res = 0
        for idx, num in enumerate(temp_list):
            res += int(num) * 10 ** idx
        return str(res)