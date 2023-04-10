class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def findKth(k):# 定义函数在有序数组中找到第k个元素
            index1, index2 = 0, 0 #index1,index2分别标记nums1,nums2的左端边界
            while True:  
                if m == index1:
                    return nums2[index2 + k - 1]
                if n == index2:
                    return nums1[index1 + k - 1]
                if k == 1:
                    return min(nums1[index1], nums2[index2])
                
                newindex1 = min(index1 + k // 2 - 1, m - 1)
                newindex2 = min(index2 + k // 2 - 1, n - 1)# 新数组的第k/2个数字，但是不能超过数组长度
                if nums1[newindex1] <= nums2[newindex2]: # 中位数不会出现在较小数组的前k/2个数字
                    k -= newindex1 - index1 + 1 # 更新k的值，减去删除的元素个数
                    index1 = newindex1 + 1
                else:
                    k -= newindex2 - index2 + 1
                    index2 = newindex2 + 1
        m, n = len(nums1), len(nums2)
        midval = (findKth((m + n + 1) // 2) + findKth((m + n + 2) // 2)) / 2# 合并奇偶两种情况
        return midval
        