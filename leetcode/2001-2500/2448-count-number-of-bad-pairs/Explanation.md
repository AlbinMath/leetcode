# LeetCode 2364: Count Number of Bad Pairs

**LeetCode Problem #2364 — Count Number of Bad Pairs**
Solve LeetCode Count Number of Bad Pairs using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Number of Bad Pairs |
| LeetCode | #2364 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** integer array `nums`. A pair of indices `(i, j)` is a **bad pair** if `i < j` and `j - i != nums[j] - nums[i]`.

Return* the total number of **bad pairs** in *`nums`.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [4,1,3,3]`
- **Output:** `5`
- **Explanation:** The pair (0, 1) is a bad pair since 1 - 0 != 1 - 4.
The pair (0, 2) is a bad pair since 2 - 0 != 3 - 4, 2 != -1.
The pair (0, 3) is a bad pair since 3 - 0 != 3 - 4, 3 != -1.
The pair (1, 2) is a bad pair since 2 - 1 != 3 - 1, 1 != 2.
The pair (2, 3) is a bad pair since 3 - 2 != 3 - 3, 1 != 0.
There are a total of 5 bad pairs, so we return 5.

### Example 2
- **Input:** `nums = [1,2,3,4,5]`
- **Output:** `0`
- **Explanation:** There are no bad pairs.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count Number of Bad Pairs**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [4,1,3,3]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.
4. **Verification:** The pair (0, 1) is a bad pair since 1 - 0 != 1 - 4.
The pair (0, 2) is a bad pair since 2 - 0 != 3 - 4, 2 != -1.
The pair (0, 3) is a bad pair since 3 - 0 != 3 - 4, 3 != -1.
The pair (1, 2) is a bad pair since 2 - 1 != 3 - 1, 1 != 2.
The pair (2, 3) is a bad pair since 3 - 2 != 3 - 3, 1 != 0.
There are a total of 5 bad pairs, so we return 5.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def countBadPairs(self, nums: list[int]) -> int:
        n = len(nums)
        total_pairs = n * (n - 1) // 2
        
        freq = {}
        good_pairs = 0
        
        for i, num in enumerate(nums):
            diff = num - i
            count = freq.get(diff, 0)
            
            good_pairs += count
            freq[diff] = count + 1
            
        return total_pairs - good_pairs
```

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [2006. Count Number of Pairs With Absolute Difference K](../../2001-2500/2116-count-number-of-pairs-with-absolute-difference-k/)
- [1248. Count Number of Nice Subarrays](../../1001-1500/1370-count-number-of-nice-subarrays/)
- [1395. Count Number of Teams](../../1501-2000/1511-count-number-of-teams/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-number-of-bad-pairs/)
