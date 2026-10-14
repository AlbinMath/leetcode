
class Solution:
    def validSubarrays(self, nums, k, queries):
        n = len(nums)
        q = len(queries)
        block = max(1, int(n ** 0.5))

        order = sorted(
            [(l, r, i) for i, (l, r) in enumerate(queries)],
            key=lambda x: (
                x[0] // block,
                x[1] if (x[0] // block) % 2 == 0 else -x[1]
            )
        )

        freq = [0] * (max(nums) + 1)
        distinct = 0
        odd_freq = 0
        left, right = 0, -1
        ans = [False] * q

        for l, r, idx in order:
            while left > l:
                left -= 1
                x = nums[left]
                if freq[x] == 0:
                    distinct += 1
                if freq[x] % 2 == 0:
                    odd_freq += 1
                else:
                    odd_freq -= 1
                freq[x] += 1

            while right < r:
                right += 1
                x = nums[right]
                if freq[x] == 0:
                    distinct += 1
                if freq[x] % 2 == 0:
                    odd_freq += 1
                else:
                    odd_freq -= 1
                freq[x] += 1

            while left < l:
                x = nums[left]
                odd_freq += -1 if freq[x] % 2 else 1
                freq[x] -= 1
                if freq[x] == 0:
                    distinct -= 1
                left += 1

            while right > r:
                x = nums[right]
                odd_freq += -1 if freq[x] % 2 else 1
                freq[x] -= 1
                if freq[x] == 0:
                    distinct -= 1
                right -= 1

            ans[idx] = (distinct == k and odd_freq == 0)

        return ans

