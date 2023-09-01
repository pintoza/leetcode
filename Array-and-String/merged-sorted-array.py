class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in nums2:

            j = 0

            while j < m:
                if i > nums1[j]:
                    j += 1
                else:
                    break

            nums1.insert(j, i)

            nums1.pop()

            m += 1