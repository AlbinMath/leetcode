class Solution:
    def reversePairs(self, nums):
        def merge_sort(a):
            if len(a) < 2:
                return 0
            m = len(a)//2
            left, right = a[:m], a[m:]
            count = merge_sort(left) + merge_sort(right)
            j = 0
            for x in left:
                while j < len(right) and x > 2*right[j]:
                    j += 1
                count += j
            i = j = 0
            a[:] = []
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    a.append(left[i])
                    i += 1
                else:
                    a.append(right[j])
                    j += 1
            a.extend(left[i:])
            a.extend(right[j:])
            return count
        return merge_sort(nums)
