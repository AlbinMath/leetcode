# LeetCode 3850: Count Sequences to K

**LeetCode Problem #3850 — Count Sequences to K**
Solve LeetCode Count Sequences to K using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Sequences to K |
| LeetCode | #3850 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums`, and an integer `k`.

Start with an initial value `val = 1` and process `nums` from left to right. At each index `i`, you must choose **exactly one** of the following actions:

Multiply `val` by `nums[i]`. 
 Divide `val` by `nums[i]`. 
 Leave `val` unchanged.

After processing all elements, `val` is considered **equal** to `k` only if its final rational value **exactly** equals `k`.

Return the count of **distinct** sequences of choices that result in `val == k`.

**Note:** Division is rational (exact), not integer division. For example, `2 / 4 = 1 / 2`.

## Constraints
- `1 <= nums.length <= 19`
- `1 <= nums[i] <= 6`
- `1 <= k <= 10^15`

## Examples
### Example 1
- **Input:** `nums = [2,3,2], k = 6`
- **Output:** `2`
- **Explanation:** The following 2 distinct sequences of choices result in `val == k`: 

 
 
 
 Sequence 
 Operation on `nums[0]` 
 Operation on `nums[1]` 
 Operation on `nums[2]` 
 Final `val` 
 
 
 
 
 1 
 Multiply: `val = 1 * 2 = 2` 
 Multiply: `val = 2 * 3 = 6` 
 Leave `val` unchanged 
 6 
 
 
 2 
 Leave `val` unchanged 
 Multiply: `val = 1 * 3 = 3` 
 Multiply: `val = 3 * 2 = 6` 
 6

### Example 2
- **Input:** `nums = [4,6,3], k = 2`
- **Output:** `2`
- **Explanation:** The following 2 distinct sequences of choices result in `val == k`: 

 
 
 
 Sequence 
 Operation on `nums[0]` 
 Operation on `nums[1]` 
 Operation on `nums[2]` 
 Final `val` 
 
 
 
 
 1 
 Multiply: `val = 1 * 4 = 4` 
 Divide: `val = 4 / 6 = 2 / 3` 
 Multiply: `val = (2 / 3) * 3 = 2` 
 2 
 
 
 2 
 Leave `val` unchanged 
 Multiply: `val = 1 * 6 = 6` 
 Divide: `val = 6 / 3 = 2` 
 2

### Example 3
- **Input:** `nums = [1,5], k = 1`
- **Output:** `3`
- **Explanation:** The following 3 distinct sequences of choices result in `val == k`: 

 
 
 
 Sequence 
 Operation on `nums[0]` 
 Operation on `nums[1]` 
 Final `val` 
 
 
 
 
 1 
 Multiply: `val = 1 * 1 = 1` 
 Leave `val` unchanged 
 1 
 
 
 2 
 Divide: `val = 1 / 1 = 1` 
 Leave `val` unchanged 
 1 
 
 
 3 
 Leave `val` unchanged 
 Leave `val` unchanged 
 1

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Count Sequences to K**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,3,2], k = 6`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The following 2 distinct sequences of choices result in `val == k`: 

 
 
 
 Sequence 
 Operation on `nums[0]` 
 Operation on `nums[1]` 
 Operation on `nums[2]` 
 Final `val` 
 
 
 
 
 1 
 Multiply: `val = 1 * 2 = 2` 
 Multiply: `val = 2 * 3 = 6` 
 Leave `val` unchanged 
 6 
 
 
 2 
 Leave `val` unchanged 
 Multiply: `val = 1 * 3 = 3` 
 Multiply: `val = 3 * 2 = 6` 
 6

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
from collections import defaultdict

class Solution:
    def countSequences(self, nums: List[int], k: int) -> int:
        vec = {1: (0, 0, 0), 2: (1, 0, 0), 3: (0, 1, 0),
               4: (2, 0, 0), 5: (0, 0, 1), 6: (1, 1, 0)}

        t = [0, 0, 0]
        for idx, p in enumerate((2, 3, 5)):
            while k % p == 0:
                k //= p
                t[idx] += 1
        if k != 1:
            return 0
        target = tuple(t)

        dp = {(0, 0, 0): 1}
        for v in nums:
            a, b, c = vec[v]
            nd = defaultdict(int)
            for (x, y, z), cnt in dp.items():
                nd[(x, y, z)] += cnt
                nd[(x + a, y + b, z + c)] += cnt
                nd[(x - a, y - b, z - c)] += cnt
            dp = nd
        return dp.get(target, 0)
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
- [2183. Count Array Pairs Divisible by K](../../2001-2500/2301-count-array-pairs-divisible-by-k/)
- [2302. Count Subarrays With Score Less Than K](../../2001-2500/2394-count-subarrays-with-score-less-than-k/)
- [2842. Count K-Subsequences of a String With Maximum Beauty](../../3001-3500/3057-count-k-subsequences-of-a-string-with-maximum-beauty/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-sequences-to-k/)
