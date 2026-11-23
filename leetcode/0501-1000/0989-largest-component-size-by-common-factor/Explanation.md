# LeetCode 952: Largest Component Size by Common Factor

**LeetCode Problem #952 — Largest Component Size by Common Factor**
Solve LeetCode Largest Component Size by Common Factor using Python and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Largest Component Size by Common Factor |
| LeetCode | #952 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array of unique positive integers `nums`. Consider the following graph:

There are `nums.length` nodes, labeled `nums[0]` to `nums[nums.length - 1]`, 
 There is an undirected edge between `nums[i]` and `nums[j]` if `nums[i]` and `nums[j]` share a common factor greater than `1`.

Return *the size of the largest connected component in the graph*.

## Constraints
- `1 <= nums.length <= 2 * 10^4`
- `1 <= nums[i] <= 10^5`
- All the values of `nums` are **unique**.

## Examples
### Example 1
- **Input:** `nums = [4,6,15,35]`
- **Output:** `4`

### Example 2
- **Input:** `nums = [20,50,9,63]`
- **Output:** `2`

### Example 3
- **Input:** `nums = [2,3,6,7,4,12,21,39]`
- **Output:** `8`

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Largest Component Size by Common Factor**, we observe the problem requirements and utilize the **Tree & Graph** technique. By maintaining a **Tree / Graph / Grid**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Tree / Graph / Grid** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [4,6,15,35]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Sorted Array.

## Pattern
**Binary Search**

## Topics
- Binary Search
- Divide and Conquer
- Search Space

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        M = max(nums)

        # smallest prime factor sieve
        spf = list(range(M + 1))
        i = 2
        while i * i <= M:
            if spf[i] == i:
                for j in range(i * i, M + 1, i):
                    if spf[j] == j:
                        spf[j] = i
            i += 1

        parent = list(range(M + 1))      # nodes are values/primes up to M

        def find(a: int) -> int:
            while parent[a] != a:
                parent[a] = parent[parent[a]]
                a = parent[a]
            return a

        def union(a: int, b: int) -> None:
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb

        for v in nums:
            x = v
            while x > 1:
                p = spf[x]
                union(v, p)
                while x % p == 0:
                    x //= p

        count = {}
        best = 0
        for v in nums:
            r = find(v)
            count[r] = count.get(r, 0) + 1
            best = max(best, count[r])
        return best
```

## Why This Works
By utilizing **Binary Search**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Applying standard binary search without accounting for array rotation or duplicates.
2. Off-by-one errors when updating boundary pointers (`left = mid + 1` vs `right = mid - 1`).
3. Integer overflow during midpoint calculation (use `mid = left + (right - left) // 2`).

## Interview Notes
- **Tests:** Logarithmic search space reduction, boundary handling, and invariant preservation.
- **Follow-up:** How does performance change if the array contains duplicate elements?

## Related Problems
- [3319. K-th Largest Perfect Subtree Size in Binary Tree](../../3501-4000/3509-k-th-largest-perfect-subtree-size-in-binary-tree/)
- [209. Minimum Size Subarray Sum](../../0001-0500/0209-minimum-size-subarray-sum/)
- [961. N-Repeated Element in Size 2N Array](../../1001-1500/1001-n-repeated-element-in-size-2n-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/largest-component-size-by-common-factor/)
