# LeetCode 1614: Maximum Nesting Depth of the Parentheses

**LeetCode Problem #1614 — Maximum Nesting Depth of the Parentheses**
Solve LeetCode Maximum Nesting Depth of the Parentheses using Java and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Nesting Depth of the Parentheses |
| LeetCode | #1614 |
| Difficulty | Easy |
| Language | Java |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given a **valid parentheses string** `s`, return the **nesting depth** of* *`s`. The nesting depth is the **maximum** number of nested parentheses.

## Constraints
- `1 <= s.length <= 100`
- `s` consists of digits `0-9` and characters `'+'`, `'-'`, `'*'`, `'/'`, `'('`, and `')'`.
- It is guaranteed that parentheses expression `s` is a VPS.

## Examples
### Example 1
- **Input:** `s = "(1+(2*3)+((8)/4))+1"`
- **Output:** `3`
- **Explanation:** Digit 8 is inside of 3 nested parentheses in the string.

### Example 2
- **Input:** `s = "(1)+((2))+(((3)))"`
- **Output:** `3`
- **Explanation:** Digit 3 is inside of 3 nested parentheses in the string.

### Example 3
- **Input:** `s = "()(())((()()))"`
- **Output:** `3`

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code tracks the current `depth` using a counter. For each `(`, increment depth and update `maxDepth`. For each `)`, decrement depth. The maximum value of `depth` during the scan is the answer.

Time complexity is $O(N)$ and space complexity is $O(1)$.

## Algorithm
1. Initialize state variables / data structure (**Stack**).
2. Process elements sequentially using **Stack Push / Pop Parsing**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `s = "(1+(2*3)+((8)/4))+1"`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** Digit 8 is inside of 3 nested parentheses in the string.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
Java

## Source Code
- [solution.java](./solution.java)


```java
class Solution {
    public int maxDepth(String s) {
        int depth = 0;
        int maxDepth = 0;

        for (char c : s.toCharArray()) {
            if (c == '(') {
                depth++;
                maxDepth = Math.max(maxDepth, depth);
            } 
            else if (c == ')') {
                depth--;
            }
        }

        return maxDepth;
    }
}
```

## Why This Works
By utilizing **Stack & Queue**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1111. Maximum Nesting Depth of Two Valid Parentheses Strings](../../1001-1500/1208-maximum-nesting-depth-of-two-valid-parentheses-strings/)
- [104. Maximum Depth of Binary Tree](../../0001-0500/0104-maximum-depth-of-binary-tree/)
- [559. Maximum Depth of N-ary Tree](../../0501-1000/0774-maximum-depth-of-n-ary-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/)
