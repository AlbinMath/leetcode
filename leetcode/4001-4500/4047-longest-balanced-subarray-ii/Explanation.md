# LeetCode 3721: Longest Balanced Subarray II

**LeetCode Problem #3721 — Longest Balanced Subarray II**
Solve LeetCode Longest Balanced Subarray II using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Balanced Subarray II |
| LeetCode | #3721 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums`.

A ** subarray ** is called **balanced** if the number of **distinct even** numbers in the subarray is equal to the number of **distinct odd** numbers.

Return the length of the **longest** balanced subarray.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^5`

## Examples
### Example 1
- **Input:** `nums = [2,5,4,3]`
- **Output:** `4`
- **Explanation:** The longest balanced subarray is `[2, 5, 4, 3]`. 
 It has 2 distinct even numbers `[2, 4]` and 2 distinct odd numbers `[5, 3]`. Thus, the answer is 4.

### Example 2
- **Input:** `nums = [3,2,2,5,4]`
- **Output:** `5`
- **Explanation:** The longest balanced subarray is `[3, 2, 2, 5, 4]`. 
 It has 2 distinct even numbers `[2, 4]` and 2 distinct odd numbers `[3, 5]`. Thus, the answer is 5.

### Example 3
- **Input:** `nums = [1,2,3,2]`
- **Output:** `3`
- **Explanation:** The longest balanced subarray is `[2, 3, 2]`. 
 It has 1 distinct even number `[2]` and 1 distinct odd number `[3]`. Thus, the answer is 3.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Longest Balanced Subarray II**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,5,4,3]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** The longest balanced subarray is `[2, 5, 4, 3]`. 
 It has 2 distinct even numbers `[2, 4]` and 2 distinct odd numbers `[5, 3]`. Thus, the answer is 4.

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
    def longestBalanced(self, nums):
        n = len(nums)
        mn = [0] * (4 * n)
        mx = [0] * (4 * n)
        ad = [0] * (4 * n)

        def update(node, l, r, ql, qr, v):
            if ql <= l and r <= qr:
                mn[node] += v
                mx[node] += v
                ad[node] += v
                return
            mid = (l + r) // 2
            if ql <= mid:
                update(2 * node, l, mid, ql, qr, v)
            if qr > mid:
                update(2 * node + 1, mid + 1, r, ql, qr, v)
            a, b = 2 * node, 2 * node + 1
            mn[node] = min(mn[a], mn[b]) + ad[node]
            mx[node] = max(mx[a], mx[b]) + ad[node]

        def find(node, l, r, qr, acc):
            if l > qr:
                return -1
            if mn[node] + acc > 0 or mx[node] + acc < 0:
                return -1
            if l == r:
                return l
            mid = (l + r) // 2
            acc += ad[node]
            res = find(2 * node, l, mid, qr, acc)
            if res != -1:
                return res
            return find(2 * node + 1, mid + 1, r, qr, acc)

        last = {}
        ans = 0
        for r, v in enumerate(nums):
            p = last.get(v, -1)
            update(1, 0, n - 1, p + 1, r, 1 if v % 2 == 0 else -1)
            last[v] = r
            l = find(1, 0, n - 1, r, 0)
            if l != -1:
                ans = max(ans, r - l + 1)
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
- [3719. Longest Balanced Subarray I](../../4001-4500/4045-longest-balanced-subarray-i/)
- [978. Longest Turbulent Subarray](../../1001-1500/1020-longest-turbulent-subarray/)
- [1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit](../../1501-2000/1549-longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-balanced-subarray-ii/)
