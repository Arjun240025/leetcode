class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        c=set(nums1)
        d=set(nums2)
        res=c&d
        return list(res)