# LeetCode 3209: Number of Subarrays With AND Value of K

**LeetCode Problem #3209 — Number of Subarrays With AND Value of K**
Solve LeetCode Number of Subarrays With AND Value of K using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Subarrays With AND Value of K |
| LeetCode | #3209 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given an array of integers `nums` and an integer `k`, return the number of subarrays of `nums` where the bitwise `AND` of the elements of the subarray equals `k`.

## Constraints
- `1 <= nums.length <= 10^5`
- `0 <= nums[i], k <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [1,1,1], k = 1`
- **Output:** `6`
- **Explanation:** All subarrays contain only 1's.

### Example 2
- **Input:** `nums = [1,1,2], k = 1`
- **Output:** `3`
- **Explanation:** Subarrays having an `AND` value of 1 are: [

### Example 3
- **Input:** `nums = [1,2,3], k = 2`
- **Output:** `2`
- **Explanation:** Subarrays having an `AND` value of 2 are: `[1, 2 ,3]`, [1,

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Number of Subarrays With AND Value of K**, we observe the problem requirements and utilize the **Bit Manipulation** technique. By maintaining a **Integer Bitmask**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Integer Bitmask** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,1,1], k = 1`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `6`.
4. **Verification:** All subarrays contain only 1's.

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
class Solution(object):
    def countSubarrays(self, nums, k):
        ans = 0
        cur = {}
        for x in nums:
            nxt = {x: 1}
            for v, c in cur.items():
                w = v & x
                nxt[w] = nxt.get(w, 0) + c
            cur = nxt
            ans += cur.get(k, 0)
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
- [2447. Number of Subarrays With GCD Equal to K](../../2001-2500/2447-number-of-subarrays-with-gcd-equal-to-k/)
- [2470. Number of Subarrays With LCM Equal to K](../../2001-2500/2470-number-of-subarrays-with-lcm-equal-to-k/)
- [995. Minimum Number of K Consecutive Bit Flips](../../0501-1000/0995-minimum-number-of-k-consecutive-bit-flips/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-subarrays-with-and-value-of-k/)
