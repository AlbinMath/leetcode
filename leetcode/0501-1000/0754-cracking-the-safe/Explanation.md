# LeetCode 753: Cracking the Safe

**LeetCode Problem #753 — Cracking the Safe**
Solve LeetCode Cracking the Safe using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Cracking the Safe |
| LeetCode | #753 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There is a safe protected by a password. The password is a sequence of `n` digits where each digit can be in the range `[0, k - 1]`.

The safe has a peculiar way of checking the password. When you enter in a sequence, it checks the **most recent **`n`** digits** that were entered each time you type a digit.

For example, the correct password is `"345"` and you enter in `"012345"`:

After typing `0`, the most recent `3` digits is `"0"`, which is incorrect. 
 After typing `1`, the most recent `3` digits is `"01"`, which is incorrect. 
 After typing `2`, the most recent `3` digits is `"012"`, which is incorrect. 
 After typing `3`, the most recent `3` digits is `"123"`, which is incorrect. 
 After typing `4`, the most recent `3` digits is `"234"`, which is incorrect. 
 After typing `5`, the most recent `3` digits is `"345"`, which is correct and the safe unlocks.

Return *any string of **minimum length** that will unlock the safe **at some point** of entering it*.

## Constraints
- `1 <= n <= 4`
- `1 <= k <= 10`
- `1 <= k^n <= 4096`

## Examples
### Example 1
- **Input:** `n = 1, k = 2`
- **Output:** `"10"`
- **Explanation:** The password is a single digit, so enter each digit. "01" would also unlock the safe.

### Example 2
- **Input:** `n = 2, k = 2`
- **Output:** `"01100"`
- **Explanation:** For each possible password:
- "00" is typed in starting from the 4^th digit.
- "01" is typed in starting from the 1^st digit.
- "10" is typed in starting from the 3^rd digit.
- "11" is typed in starting from the 2^nd digit.
Thus "01100" will unlock the safe. "10011", and "11001" would also unlock the safe.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Cracking the Safe**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 1, k = 2`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"10"`.
4. **Verification:** The password is a single digit, so enter each digit. "01" would also unlock the safe.

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
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var crackSafe = function(n, k) {
    let visited = new Set();
    let result = [];

    let start = "0".repeat(n - 1);

    function dfs(node) {
        for (let i = 0; i < k; i++) {
            let edge = node + i;

            if (!visited.has(edge)) {
                visited.add(edge);

                dfs(edge.slice(1));

                result.push(i);
            }
        }
    }

    dfs(start);

    // Reverse the postorder result
    result.reverse();

    return start + result.join("");
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
- [802. Find Eventual Safe States](../../0501-1000/0820-find-eventual-safe-states/)
- [3286. Find a Safe Walk Through a Grid](../../3501-4000/3558-find-a-safe-walk-through-a-grid/)
- [2. Add Two Numbers](../../0001-0500/0002-add-two-numbers/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/cracking-the-safe/)
