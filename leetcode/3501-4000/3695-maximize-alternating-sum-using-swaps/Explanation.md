# LeetCode 3695: Maximize Alternating Sum Using Swaps

**LeetCode Problem #3695 — Maximize Alternating Sum Using Swaps**
Solve LeetCode Maximize Alternating Sum Using Swaps using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximize Alternating Sum Using Swaps |
| LeetCode | #3695 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums`.

You want to maximize the **alternating sum** of `nums`, which is defined as the value obtained by **adding** elements at even indices and **subtracting** elements at odd indices. That is, `nums[0] - nums[1] + nums[2] - nums[3]...`

You are also given a 2D integer array `swaps` where `swaps[i] = [p_i, q_i]`. For each pair `[p_i, q_i]` in `swaps`, you are allowed to swap the elements at indices `p_i` and `q_i`. These swaps can be performed any number of times and in any order.

Return the maximum possible **alternating sum** of `nums`.

## Constraints
- `2 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`
- `0 <= swaps.length <= 10^5`
- `swaps[i] = [p_i, q_i]`
- `0 <= p_i < q_i <= nums.length - 1`
- `[p_i, q_i] != [p_j, q_j]`

## Examples
### Example 1
- **Input:** `nums = [1,2,3], swaps = [[0,2],[1,2]]`
- **Output:** `4`
- **Explanation:** The maximum alternating sum is achieved when `nums` is `[2, 1, 3]` or `[3, 1, 2]`. As an example, you can obtain `nums = [2, 1, 3]` as follows. 

 
 Swap `nums[0]` and `nums[2]`. `nums` is now `[3, 2, 1]`. 
 Swap `nums[1]` and `nums[2]`. `nums` is now `[3, 1, 2]`. 
 Swap `nums[0]` and `nums[2]`. `nums` is now `[2, 1, 3]`.

### Example 2
- **Input:** `nums = [1,2,3], swaps = [[1,2]]`
- **Output:** `2`
- **Explanation:** The maximum alternating sum is achieved by not performing any swaps.

### Example 3
- **Input:** `nums = [1,1000000000,1,1000000000,1,1000000000], swaps = []`
- **Output:** `-2999999997`
- **Explanation:** Since we cannot perform any swaps, the maximum alternating sum is achieved by not performing any swaps.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Maximize Alternating Sum Using Swaps**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3], swaps = [[0,2],[1,2]]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** The maximum alternating sum is achieved when `nums` is `[2, 1, 3]` or `[3, 1, 2]`. As an example, you can obtain `nums = [2, 1, 3]` as follows. 

 
 Swap `nums[0]` and `nums[2]`. `nums` is now `[3, 2, 1]`. 
 Swap `nums[1]` and `nums[2]`. `nums` is now `[3, 1, 2]`. 
 Swap `nums[0]` and `nums[2]`. `nums` is now `[2, 1, 3]`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Dictionary / Hash Map.

## Pattern
**Hash Map**

## Topics
- Hash Table
- Array
- Complement Lookup

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from collections import defaultdict
from typing import List

class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))

    def find(self, x: int) -> int:
        root = x
        while self.parent[root] != root:
            root = self.parent[root]
        while x != root:
            nxt = self.parent[x]
            self.parent[x] = root
            x = nxt
        return root

    def union(self, x: int, y: int):
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            self.parent[ry] = rx


class Solution:
    def maxAlternatingSum(self, nums: List[int], swaps: List[List[int]]) -> int:
        n = len(nums)
        dsu = DSU(n)

        for u, v in swaps:
            dsu.union(u, v)

        # Group indices by connected component root
        comp_indices = defaultdict(list)
        for i in range(n):
            root = dsu.find(i)
            comp_indices[root].append(i)

        total_sum = 0

        for indices in comp_indices.values():
            # Count available even positions
            even_count = sum(1 for idx in indices if idx % 2 == 0)

            # Extract and sort values belonging to this component in descending order
            vals = sorted((nums[idx] for idx in indices), reverse=True)

            # Assign largest values to even indices (+) and remaining to odd indices (-)
            for i, val in enumerate(vals):
                if i < even_count:
                    total_sum += val
                else:
                    total_sum -= val

        return total_sum
```

## Why This Works
By utilizing **Hash Map**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Using the same element twice.
2. Checking the map before inserting elements in the correct order.
3. Inefficient hash functions or unnecessary duplicate key updates.

## Interview Notes
- **Tests:** Hash map usage, complement/frequency lookup, and $O(n)$ time optimization.
- **Follow-up:** Can you solve the problem in $O(1)$ extra space if the input array is sorted?

## Related Problems
- [1864. Minimum Number of Swaps to Make the Binary String Alternating](../../1501-2000/1864-minimum-number-of-swaps-to-make-the-binary-string-alternating/)
- [3551. Minimum Swaps to Sort by Digit Sum](../../3501-4000/3551-minimum-swaps-to-sort-by-digit-sum/)
- [3868. Minimum Cost to Equalize Arrays Using Swaps](../../3501-4000/3868-minimum-cost-to-equalize-arrays-using-swaps/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximize-alternating-sum-using-swaps/)
