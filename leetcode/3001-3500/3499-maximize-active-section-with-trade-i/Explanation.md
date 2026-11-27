# LeetCode 3499: Maximize Active Section with Trade I

**LeetCode Problem #3499 — Maximize Active Section with Trade I**
Solve LeetCode Maximize Active Section with Trade I using C++ and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximize Active Section with Trade I |
| LeetCode | #3499 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a binary string `s` of length `n`, where:

`'1'` represents an **active** section. 
 `'0'` represents an **inactive** section.

You can perform **at most one trade** to maximize the number of active sections in `s`. In a trade, you:

Convert a contiguous block of `'1'`s that is surrounded by `'0'`s to all `'0'`s. 
 Afterward, convert a contiguous block of `'0'`s that is surrounded by `'1'`s to all `'1'`s.

Return the **maximum** number of active sections in `s` after making the optimal trade.

**Note:** Treat `s` as if it is **augmented** with a `'1'` at both ends, forming `t = '1' + s + '1'`. The augmented `'1'`s **do not** contribute to the final count.

## Constraints
- `1 <= n == s.length <= 10^5`
- `s[i]` is either `'0'` or `'1'`

## Examples
### Example 1
- **Input:** `s = "01"`
- **Output:** `1`
- **Explanation:** Because there is no block of `'1'`s surrounded by `'0'`s, no valid trade is possible. The maximum number of active sections is 1.

### Example 2
- **Input:** `s = "0100"`
- **Output:** `4`
- **Explanation:** String `"0100"` &rarr; Augmented to `"101001"`. 
 Choose `"0100"`, convert "10

### Example 3
- **Input:** `s = "1000100"`
- **Output:** `7`
- **Explanation:** String `"1000100"` &rarr; Augmented to `"110001001"`. 
 Choose `"000100"`, convert "11000

### Example 4
- **Input:** `s = "01010"`
- **Output:** `4`
- **Explanation:** String `"01010"` &rarr; Augmented to `"1010101"`. 
 Choose `"010"`, convert "10

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Maximize Active Section with Trade I**, we observe the problem requirements and utilize the **Monotonic Stack** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "01"`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** Because there is no block of `'1'`s surrounded by `'0'`s, no valid trade is possible. The maximum number of active sections is 1.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)


```cpp
class Solution {
public:
    int maxActiveSectionsAfterTrade(string s) {
        int n = s.size();

        // Number of existing 1s
        int base = count(s.begin(), s.end(), '1');

        // Augmented string
        string t = "1" + s + "1";

        int ans = base;

        int i = 1;

        while (i < n + 1) {
            // Skip 0s
            if (t[i] == '0') {
                i++;
                continue;
            }

            // Find a block of 1s
            int l = i;

            while (i < n + 1 && t[i] == '1') {
                i++;
            }

            int r = i - 1;

            // This 1-block must be surrounded by 0s
            if (l > 1 && r < n &&
                t[l - 1] == '0' &&
                t[r + 1] == '0') {

                // Count zeros on the left
                int left = l - 1;
                while (left >= 0 && t[left] == '0') {
                    left--;
                }

                int leftZeros = l - left - 1;

                // Count zeros on the right
                int right = r + 1;
                while (right < n + 2 && t[right] == '0') {
                    right++;
                }

                int rightZeros = right - r - 1;

                // After the trade, these two zero blocks
                // become active.
                ans = max(ans, base + leftZeros + rightZeros);
            }
        }

        return ans;
    }
};
```

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [3501. Maximize Active Section with Trade II](../../3501-4000/3501-maximize-active-section-with-trade-ii/)
- [1817. Finding the Users Active Minutes](../../1501-2000/1817-finding-the-users-active-minutes/)
- [1005. Maximize Sum Of Array After K Negations](../../1001-1500/1005-maximize-sum-of-array-after-k-negations/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximize-active-section-with-trade-i/)
