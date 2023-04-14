class Solution:
    def intToRoman(self, num: int) -> str:
        hash_map = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}# hash_map = {key:'value'}
        res = ''
        for key in hash_map:
            res += hash_map[key] * (num // key) #计算需要添加多少个key值的value
            num %= key # 给num降位
        return res