# LeetCode 2183: Count Array Pairs Divisible by K

**LeetCode Problem #2183 — Count Array Pairs Divisible by K**
Solve LeetCode Count Array Pairs Divisible by K using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Array Pairs Divisible by K |
| LeetCode | #2183 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given a **0-indexed** integer array `nums` of length `n` and an integer `k`, return *the **number of pairs*** `(i, j)` *such that:*

`0 <= i < j <= n - 1` *and* 
 `nums[i] * nums[j]` *is divisible by* `k`.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i], k <= 10^5`

## Examples
### Example 1
- **Input:** `nums = [1,2,3,4,5], k = 2`
- **Output:** `7`
- **Explanation:** The 7 pairs of indices whose corresponding products are divisible by 2 are
(0, 1), (0, 3), (1, 2), (1, 3), (1, 4), (2, 3), and (3, 4).
Their products are 2, 4, 6, 8, 10, 12, and 20 respectively.
Other pairs such as (0, 2) and (2, 4) have products 3 and 15 respectively, which are not divisible by 2.

### Example 2
- **Input:** `nums = [1,2,3,4], k = 5`
- **Output:** `0`
- **Explanation:** There does not exist any pair of indices whose corresponding product is divisible by 5.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Count Array Pairs Divisible by K**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3,4,5], k = 2`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `7`.
4. **Verification:** The 7 pairs of indices whose corresponding products are divisible by 2 are
(0, 1), (0, 3), (1, 2), (1, 3), (1, 4), (2, 3), and (3, 4).
Their products are 2, 4, 6, 8, 10, 12, and 20 respectively.
Other pairs such as (0, 2) and (2, 4) have products 3 and 15 respectively, which are not divisible by 2.

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
from math import gcd
from collections import Counter
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        c, ans = Counter(), 0
        for x in nums:
            g = gcd(x, k)
            ans += sum(v for d, v in c.items() if g * d % k == 0)
            c[g] += 1
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
- [1497. Check If Array Pairs Are Divisible by k](../../1001-1500/1497-check-if-array-pairs-are-divisible-by-k/)
- [629. K Inverse Pairs Array](../../0501-1000/0629-k-inverse-pairs-array/)
- [1814. Count Nice Pairs in an Array](../../1501-2000/1814-count-nice-pairs-in-an-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-array-pairs-divisible-by-k/)
