class Solution:#duplicates must also be considered in leetcode 350
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        c = {}

        for i in nums1:
            c[i] = c.get(i, 0) + 1

        res = []

        for i in nums2:
            if i in c and c[i] > 0:
                res.append(i)
                c[i] -= 1

        return res