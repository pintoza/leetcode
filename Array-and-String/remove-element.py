class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        n = len(nums)

        k = 0
        j = 0

        for i in range(n):
            if nums[i] != val:
                nums[j] = nums[i]
                k += 1
                j += 1

        del nums[k:]

        return k