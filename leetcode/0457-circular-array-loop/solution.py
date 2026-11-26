from typing import List

class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        def get_next(idx: int) -> int:
            return (idx + nums[idx]) % n

        for i in range(n):
            if nums[i] == 0:
                continue

            is_forward = nums[i] > 0
            slow = i
            fast = i

            while True:
                next_slow = get_next(slow)
                if nums[next_slow] == 0 or (nums[next_slow] > 0) != is_forward:
                    break
                next_fast = get_next(fast)
                if nums[next_fast] == 0 or (nums[next_fast] > 0) != is_forward:
                    break
                next_fast = get_next(next_fast)
                if nums[next_fast] == 0 or (nums[next_fast] > 0) != is_forward:
                    break

                slow = next_slow
                fast = next_fast

                if slow == fast:
                    if slow == get_next(slow):
                        break
                    return True
            curr = i
            while nums[curr] != 0 and (nums[curr] > 0) == is_forward:
                nxt = get_next(curr)
                nums[curr] = 0
                curr = nxt

        return False
