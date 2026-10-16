class Solution:
    def sortArray(self, nums):
        n = len(nums)

        def heapify(n, i):
            while True:
                m = i
                l, r = 2*i+1, 2*i+2
                if l < n and nums[l] > nums[m]:
                    m = l
                if r < n and nums[r] > nums[m]:
                    m = r
                if m == i:
                    break
                nums[i], nums[m] = nums[m], nums[i]
                i = m

        for i in range(n//2-1, -1, -1):
            heapify(n, i)

        for i in range(n-1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            heapify(i, 0)

        return nums
