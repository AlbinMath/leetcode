# LeetCode 2232: Minimize Result by Adding Parentheses to Expression

**LeetCode Problem #2232 — Minimize Result by Adding Parentheses to Expression**
Solve LeetCode Minimize Result by Adding Parentheses to Expression using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimize Result by Adding Parentheses to Expression |
| LeetCode | #2232 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** string `expression` of the form `"<num1>+<num2>"` where `<num1>` and `<num2>` represent positive integers.

Add a pair of parentheses to `expression` such that after the addition of parentheses, `expression` is a **valid** mathematical expression and evaluates to the **smallest** possible value. The left parenthesis **must** be added to the left of `'+'` and the right parenthesis **must** be added to the right of `'+'`.

Return `expression`* after adding a pair of parentheses such that *`expression`* evaluates to the **smallest** possible value.* If there are multiple answers that yield the same result, return any of them.

The input has been generated such that the original value of `expression`, and the value of `expression` after adding any pair of parentheses that meets the requirements fits within a signed 32-bit integer.

## Constraints
- `3 <= expression.length <= 10`
- `expression` consists of digits from `'1'` to `'9'` and `'+'`.
- `expression` starts and ends with digits.
- `expression` contains exactly one `'+'`.
- The original value of `expression`, and the value of `expression` after adding any pair of parentheses that meets the requirements fits within a signed 32-bit integer.

## Examples
### Example 1
- **Input:** `expression = "247+38"`
- **Output:** `"2(47+38)"`
- **Explanation:** The `expression` evaluates to 2 * (47 + 38) = 2 * 85 = 170.
Note that "2(4)7+38" is invalid because the right parenthesis must be to the right of the `'+'`.
It can be shown that 170 is the smallest possible value.

### Example 2
- **Input:** `expression = "12+34"`
- **Output:** `"1(2+3)4"`
- **Explanation:** The expression evaluates to 1 * (2 + 3) * 4 = 1 * 5 * 4 = 20.

### Example 3
- **Input:** `expression = "999+999"`
- **Output:** `"(999+999)"`
- **Explanation:** The `expression` evaluates to 999 + 999 = 1998.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Minimize Result by Adding Parentheses to Expression**, we observe the problem requirements and utilize the **Stack & Queue** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `expression = "247+38"`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"2(47+38)"`.
4. **Verification:** The `expression` evaluates to 2 * (47 + 38) = 2 * 85 = 170.
Note that "2(4)7+38" is invalid because the right parenthesis must be to the right of the `'+'`.
It can be shown that 170 is the smallest possible value.

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
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution(object):
    def minimizeResult(self, expression):
        left, right = expression.split('+')
        best_val = float('inf')
        best_expr = ""

        for i in range(len(left)):
            a = int(left[:i]) if i > 0 else 1
            b = int(left[i:])

            for j in range(1, len(right) + 1):
                c = int(right[:j])
                d = int(right[j:]) if j < len(right) else 1

                val = a * (b + c) * d
                if val < best_val:
                    best_val = val
                    best_expr = left[:i] + "(" + left[i:] + "+" + right[:j] + ")" + right[j:]

        return best_expr
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
- [10. Regular Expression Matching](../../0001-0500/0010-regular-expression-matching/)
- [282. Expression Add Operators](../../0001-0500/0282-expression-add-operators/)
- [736. Parse Lisp Expression](../../0501-1000/0736-parse-lisp-expression/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimize-result-by-adding-parentheses-to-expression/)
