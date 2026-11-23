# LeetCode 22: Generate Parentheses

**LeetCode Problem #22 — Generate Parentheses**
Solve LeetCode Generate Parentheses using C++, JavaScript, Python and Backtracking. This solution finds the optimal result using Backtracking Recursive Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Generate Parentheses |
| LeetCode | #22 |
| Difficulty | Medium |
| Language | C++, JavaScript, Python |
| Algorithm | Backtracking Recursive Search |
| Data Structure | Recursion Tree |
| Pattern | Backtracking |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given `n` pairs of parentheses, write a function to *generate all combinations of well-formed parentheses*.

## Constraints
- `1 <= n <= 8`

## Examples
### Example 1
- **Input:** `n = 3`
- **Output:** `["((()))","(()())","(())()","()(())","()()()"]`

### Example 2
- **Input:** `n = 1`
- **Output:** `["()"]`

## Key Insight
Leverage **Backtracking** with **Recursion Tree** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Generate Parentheses**, we observe the problem requirements and utilize the **Stack & Queue** technique. We iterate through the inputs using **Stack Push / Pop Parsing**, leveraging a **Stack** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Stack**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 3`.
2. **Processing Steps:** We apply **Backtracking Recursive Search** using our **Recursion Tree**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `["((()))","(()())","(())()","()(())","()()()"]`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Recursion Tree.

## Pattern
**Backtracking**

## Topics
- Backtracking
- Recursion

## Language
C++, JavaScript, Python

## Source Code
- [solution.cpp](./solution.cpp)
- [solution.js](./solution.js)
- [solution.py](./solution.py)


### C++
```cpp
class Solution {
public:
    vector<string> result;

    void backtrack(string current, int open, int close, int n) {
        // A valid combination is complete
        if (current.length() == 2 * n) {
            result.push_back(current);
            return;
        }

        // Add '(' if we still have opening parentheses
        if (open < n) {
            backtrack(current + "(", open + 1, close, n);
        }

        // Add ')' only when there are unmatched '('
        if (close < open) {
            backtrack(current + ")", open, close + 1, n);
        }
    }

    vector<string> generateParenthesis(int n) {
        backtrack("", 0, 0, n);
        return result;
    }
};
```

### JavaScript
```javascript
var generateParenthesis = function(n) {
    const result = [];

    function backtrack(current, open, close) {
        if (current.length === 2 * n) {
            result.push(current);
            return;
        }

        // Add an opening parenthesis if available
        if (open < n) {
            backtrack(current + "(", open + 1, close);
        }

        // Add a closing parenthesis only if it stays valid
        if (close < open) {
            backtrack(current + ")", open, close + 1);
        }
    }

    backtrack("", 0, 0);
    return result;
};
```

### Python
```python
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(current, open_count, close_count):
            if len(current) == 2 * n:
                result.append(current)
                return

            # Add '(' if we have unused opening parentheses
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)

            # Add ')' only if it won't make the string invalid
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return result
```

## Why This Works
By utilizing **Backtracking**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [2267.  Check if There Is a Valid Parentheses String Path](../../2001-2500/2349-check-if-there-is-a-valid-parentheses-string-path/)
- [20. Valid Parentheses](../../0001-0500/0020-valid-parentheses/)
- [32. Longest Valid Parentheses](../../0001-0500/0032-longest-valid-parentheses/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/generate-parentheses/)
