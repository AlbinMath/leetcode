# LeetCode 3404: Count Special Subsequences

**LeetCode Problem #3404 — Count Special Subsequences**
Solve LeetCode Count Special Subsequences using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Special Subsequences |
| LeetCode | #3404 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an array `nums` consisting of positive integers.

A **special subsequence** is defined as a subsequence of length 4, represented by indices `(p, q, r, s)`, where `p < q < r < s`. This subsequence **must** satisfy the following conditions:

`nums[p] * nums[r] == nums[q] * nums[s]` 
 There must be *at least* **one** element between each pair of indices. In other words, `q - p > 1`, `r - q > 1` and `s - r > 1`.

Return the *number* of different **special** **subsequences** in `nums`.

## Constraints
- `7 <= nums.length <= 1000`
- `1 <= nums[i] <= 1000`

## Examples
### Example 1
- **Input:** `nums = [1,2,3,4,3,6,1]`
- **Output:** `1`
- **Explanation:** There is one special subsequence in `nums`. 

 
 `(p, q, r, s) = (0, 2, 4, 6)`:

 
 This corresponds to elements `(1, 3, 3, 1)`. 
 `nums[p] * nums[r] = nums[0] * nums[4] = 1 * 3 = 3` 
 `nums[q] * nums[s] = nums[2] * nums[6] = 3 * 1 = 3`

### Example 2
- **Input:** `nums = [3,4,3,4,3,4,3,4]`
- **Output:** `3`
- **Explanation:** There are three special subsequences in `nums`. 

 
 `(p, q, r, s) = (0, 2, 4, 6)`:

 
 This corresponds to elements `(3, 3, 3, 3)`. 
 `nums[p] * nums[r] = nums[0] * nums[4] = 3 * 3 = 9` 
 `nums[q] * nums[s] = nums[2] * nums[6] = 3 * 3 = 9` 
 
 
 `(p, q, r, s) = (1, 3, 5, 7)`:
 
 This corresponds to elements `(4, 4, 4, 4)`. 
 `nums[p] * nums[r] = nums[1] * nums[5] = 4 * 4 = 16` 
 `nums[q] * nums[s] = nums[3] * nums[7] = 4 * 4 = 16` 
 
 
 `(p, q, r, s) = (0, 2, 5, 7)`:
 
 This corresponds to elements `(3, 3, 4, 4)`. 
 `nums[p] * nums[r] = nums[0] * nums[5] = 3 * 4 = 12` 
 `nums[q] * nums[s] = nums[2] * nums[7] = 3 * 4 = 12`

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Count Special Subsequences**, we observe the problem requirements and utilize the **Dynamic Programming** technique. By maintaining a **DP Table / Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **DP Table / Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3,4,3,6,1]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** There is one special subsequence in `nums`. 

 
 `(p, q, r, s) = (0, 2, 4, 6)`:

 
 This corresponds to elements `(1, 3, 3, 1)`. 
 `nums[p] * nums[r] = nums[0] * nums[4] = 1 * 3 = 3` 
 `nums[q] * nums[s] = nums[2] * nums[6] = 3 * 1 = 3`

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
from typing import List
from math import gcd
from collections import defaultdict

class Solution:
    def numberOfSubsequences(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = defaultdict(int)
        ans = 0

        for r in range(4, n - 2):
            q = r - 2
            for p in range(q - 1):          # p <= q - 2
                g = gcd(nums[p], nums[q])
                cnt[(nums[p] // g, nums[q] // g)] += 1
            for s in range(r + 2, n):
                g = gcd(nums[s], nums[r])
                ans += cnt.get((nums[s] // g, nums[r] // g), 0)

        return ans
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
- [730. Count Different Palindromic Subsequences](../../0501-1000/0730-count-different-palindromic-subsequences/)
- [2842. Count K-Subsequences of a String With Maximum Beauty](../../2501-3000/2842-count-k-subsequences-of-a-string-with-maximum-beauty/)
- [1995. Count Special Quadruplets](../../1501-2000/1995-count-special-quadruplets/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-special-subsequences/)
