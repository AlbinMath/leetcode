# LeetCode 440: K-th Smallest in Lexicographical Order

**LeetCode Problem #440 — K-th Smallest in Lexicographical Order**
Solve LeetCode K-th Smallest in Lexicographical Order using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | K-th Smallest in Lexicographical Order |
| LeetCode | #440 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given two integers `n` and `k`, return *the* `k^th` *lexicographically smallest integer in the range* `[1, n]`.

## Constraints
- `1 <= k <= n <= 10^9`

## Examples
### Example 1
- **Input:** `n = 13, k = 2`
- **Output:** `10`
- **Explanation:** The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is 10.

### Example 2
- **Input:** `n = 1, k = 1`
- **Output:** `1`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **K-th Smallest in Lexicographical Order**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 13, k = 2`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `10`.
4. **Verification:** The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is 10.

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
    def findKthNumber(self, n: int, k: int) -> int:
        def count(cur):
            first = last = cur
            total = 0
            while first <= n:
                total += min(n, last) - first + 1
                first *= 10
                last = last * 10 + 9
            return total

        cur = 1
        k -= 1
        while k > 0:
            steps = count(cur)
            if steps <= k:
                cur += 1
                k -= steps
            else:
                cur *= 10
                k -= 1
        return cur
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
- [1415. The k-th Lexicographical String of All Happy Strings of Length n](../../1501-2000/1516-the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/)
- [1163. Last Substring in Lexicographical Order](../../1001-1500/1133-last-substring-in-lexicographical-order/)
- [779. K-th Symbol in Grammar](../../0501-1000/0795-k-th-symbol-in-grammar/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/)
