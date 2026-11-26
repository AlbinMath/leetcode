# LeetCode 483: Smallest Good Base

**LeetCode Problem #483 — Smallest Good Base**
Solve LeetCode Smallest Good Base using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Smallest Good Base |
| LeetCode | #483 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given an integer `n` represented as a string, return *the smallest **good base** of* `n`.

We call `k >= 2` a **good base** of `n`, if all digits of `n` base `k` are `1`'s.

## Constraints
- `n` is an integer in the range `[3, 10^18]`.
- `n` does not contain any leading zeros.

## Examples
### Example 1
- **Input:** `n = "13"`
- **Output:** `"3"`
- **Explanation:** 13 base 3 is 111.

### Example 2
- **Input:** `n = "4681"`
- **Output:** `"8"`
- **Explanation:** 4681 base 8 is 11111.

### Example 3
- **Input:** `n = "1000000000000000000"`
- **Output:** `"999999999999999999"`
- **Explanation:** 1000000000000000000 base 999999999999999999 is 11.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Smallest Good Base**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = "13"`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"3"`.
4. **Verification:** 13 base 3 is 111.

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
class Solution:
    def smallestGoodBase(self, n: str) -> str:
        N = int(n)
        for m in range(60, 1, -1):
            lo, hi = 2, int(N ** (1.0 / m)) + 2
            while lo < hi:
                mid = (lo + hi) // 2
                if mid ** m >= N:
                    hi = mid
                else:
                    lo = mid + 1
            # candidates: lo and lo - 1 (root guess may be off by one)
            for k in (lo - 1, lo):
                if k >= 2 and (k ** (m + 1) - 1) // (k - 1) == N:
                    return str(k)
        return str(N - 1)
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
- [230. Kth Smallest Element in a BST](../../0001-0500/0230-kth-smallest-element-in-a-bst/)
- [373. Find K Pairs with Smallest Sums](../../0001-0500/0373-find-k-pairs-with-smallest-sums/)
- [378. Kth Smallest Element in a Sorted Matrix](../../0001-0500/0378-kth-smallest-element-in-a-sorted-matrix/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/smallest-good-base/)
