# LeetCode 1896: Minimum Cost to Change the Final Value of Expression

**LeetCode Problem #1896 — Minimum Cost to Change the Final Value of Expression**
Solve LeetCode Minimum Cost to Change the Final Value of Expression using C++ and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Cost to Change the Final Value of Expression |
| LeetCode | #1896 |
| Difficulty | Hard |
| Language | C++ |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **valid** boolean expression as a string `expression` consisting of the characters `'1'`,`'0'`,`'&'` (bitwise **AND** operator),`'|'` (bitwise **OR** operator),`'('`, and `')'`.

For example, `"()1|1"` and `"(1)&()"` are **not valid** while `"1"`, `"(((1))|(0))"`, and `"1|(0&(1))"` are **valid** expressions.

Return* the **minimum cost** to change the final value of the expression*.

For example, if `expression = "1|1|(0&0)&1"`, its **value** is `1|1|(0&0)&1 = 1|1|0&1 = 1|0&1 = 1&1 = 1`. We want to apply operations so that the** new** expression evaluates to `0`.

The **cost** of changing the final value of an expression is the **number of operations** performed on the expression. The types of **operations** are described as follows:

Turn a `'1'` into a `'0'`. 
 Turn a `'0'` into a `'1'`. 
 Turn a `'&'` into a `'|'`. 
 Turn a `'|'` into a `'&'`.

**Note:** `'&'` does **not** take precedence over `'|'` in the **order of calculation**. Evaluate parentheses **first**, then in **left-to-right** order.

## Constraints
- `1 <= expression.length <= 10^5`
- `expression` only contains `'1'`,`'0'`,`'&'`,`'|'`,`'('`, and `')'`
- All parentheses are properly matched.
- There will be no empty parentheses (i.e: `"()"` is not a substring of `expression`).

## Examples
### Example 1
- **Input:** `expression = "1&(0|1)"`
- **Output:** `1`
- **Explanation:** We can turn "1&(0

### Example 2
- **Input:** `expression = "(0&0)&(0&0&0)"`
- **Output:** `3`
- **Explanation:** We can turn "(0

### Example 3
- **Input:** `expression = "(0|(1|0&1))"`
- **Output:** `1`
- **Explanation:** We can turn "(0|(

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Minimum Cost to Change the Final Value of Expression**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `expression = "1&(0|1)"`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** We can turn "1&(0

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
#include <string>
#include <vector>
#include <algorithm>
#include <utility>
using namespace std;

class Solution {
public:
    int minOperationsToFlip(string expression) {
        // Each entry stores {evaluated_value, min_cost_to_flip}
        vector<pair<int, int>> vals;
        vector<char> ops;
        
        auto apply_op = [&]() {
            char op = ops.back();
            ops.pop_back();
            
            auto [v2, c2] = vals.back(); vals.pop_back();
            auto [v1, c1] = vals.back(); vals.pop_back();
            
            int new_val, new_cost;
            if (op == '&') {
                new_val = v1 & v2;
                if (v1 == 1 && v2 == 1) {
                    new_cost = min(c1, c2);
                } else if (v1 == 0 && v2 == 0) {
                    new_cost = 1 + min(c1, c2);
                } else {
                    // One is 1, one is 0 -> changing '&' to '|' costs 1
                    new_cost = 1;
                }
            } else { // op == '|'
                new_val = v1 | v2;
                if (v1 == 0 && v2 == 0) {
                    new_cost = min(c1, c2);
                } else if (v1 == 1 && v2 == 1) {
                    new_cost = 1 + min(c1, c2);
                } else {
                    // One is 1, one is 0 -> changing '|' to '&' costs 1
                    new_cost = 1;
                }
            }
            vals.push_back({new_val, new_cost});
        };
        
        for (char c : expression) {
            if (c == '(' || c == '&' || c == '|') {
                ops.push_back(c);
            } else {
                if (c == '0' || c == '1') {
                    vals.push_back({c - '0', 1});
                } else if (c == ')') {
                    // Pop the matching '('
                    ops.pop_back();
                }
                // Enforce left-to-right evaluation whenever an operand completes
                if (!ops.empty() && (ops.back() == '&' || ops.back() == '|')) {
                    apply_op();
                }
            }
        }
        
        return vals.back().second;
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
- [1737. Change Minimum Characters to Satisfy One of Three Conditions](../../1501-2000/1859-change-minimum-characters-to-satisfy-one-of-three-conditions/)
- [1130. Minimum Cost Tree From Leaf Values](../../1001-1500/1228-minimum-cost-tree-from-leaf-values/)
- [1217. Minimum Cost to Move Chips to The Same Position](../../1001-1500/1329-minimum-cost-to-move-chips-to-the-same-position/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-cost-to-change-the-final-value-of-expression/)
