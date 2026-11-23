# LeetCode 2267:  Check if There Is a Valid Parentheses String Path

**LeetCode Problem #2267 —  Check if There Is a Valid Parentheses String Path**
Solve LeetCode  Check if There Is a Valid Parentheses String Path using C++ and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem |  Check if There Is a Valid Parentheses String Path |
| LeetCode | #2267 |
| Difficulty | Hard |
| Language | C++ |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
A parentheses string is a **non-empty** string consisting only of `'('` and `')'`. It is **valid** if **any** of the following conditions is **true**:

It is `()`. 
 It can be written as `AB` (`A` concatenated with `B`), where `A` and `B` are valid parentheses strings. 
 It can be written as `(A)`, where `A` is a valid parentheses string.

You are given an `m x n` matrix of parentheses `grid`. A **valid parentheses string path** in the grid is a path satisfying **all** of the following conditions:

The path starts from the upper left cell `(0, 0)`. 
 The path ends at the bottom-right cell `(m - 1, n - 1)`. 
 The path only ever moves **down** or **right**. 
 The resulting parentheses string formed by the path is **valid**.

Return `true` *if there exists a **valid parentheses string path** in the grid.* Otherwise, return `false`.

## Constraints
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 100`
- `grid[i][j]` is either `'('` or `')'`.

## Examples
### Example 1
- **Input:** `grid = [["(","(","("],[")","(",")"],["(","(",")"],["(","(",")"]]`
- **Output:** `true`
- **Explanation:** The above diagram shows two possible paths that form valid parentheses strings.
The first path shown results in the valid parentheses string "()(())".
The second path shown results in the valid parentheses string "((()))".
Note that there may be other valid parentheses string paths.

### Example 2
- **Input:** `grid = [[")",")"],["(","("]]`
- **Output:** `false`
- **Explanation:** The two possible paths form the parentheses strings "))(" and ")((". Since neither of them are valid parentheses strings, we return false.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
Uses **DP with state tracking**. At each cell, track the set of possible open-parenthesis counts. Moving right or down, increment count for `(` and decrement for `)`. A path is valid if we reach the bottom-right with count exactly 0. Prune states where count goes negative.

## Algorithm
1. Initialize state variables / data structure (**Stack**).
2. Process elements sequentially using **Stack Push / Pop Parsing**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [["(","(","("],[")","(",")"],["(","(",")"],["(","(",")"]]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** The above diagram shows two possible paths that form valid parentheses strings.
The first path shown results in the valid parentheses string "()(())".
The second path shown results in the valid parentheses string "((()))".
Note that there may be other valid parentheses string paths.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)


```cpp
class Solution {
public:
    bool hasValidPath(vector<vector<char>>& grid) {
        int m = grid.size();
        int n = grid[0].size();

        int len = m + n - 1;

        // Valid parentheses string must have even length
        if (len % 2 != 0)
            return false;

        // dp[i][j][balance]
        vector<vector<vector<bool>>> dp(
            m,
            vector<vector<bool>>(n, vector<bool>(len + 1, false))
        );

        // First character must be '('
        if (grid[0][0] == ')')
            return false;

        dp[0][0][1] = true;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {

                if (i == 0 && j == 0)
                    continue;

                for (int balance = 0; balance <= len; balance++) {

                    int prevBalance;

                    if (grid[i][j] == '(')
                        prevBalance = balance - 1;
                    else
                        prevBalance = balance + 1;

                    if (prevBalance < 0 || prevBalance > len)
                        continue;

                    // From top
                    if (i > 0 && dp[i - 1][j][prevBalance])
                        dp[i][j][balance] = true;

                    // From left
                    if (j > 0 && dp[i][j - 1][prevBalance])
                        dp[i][j][balance] = true;
                }
            }
        }

        return dp[m - 1][n - 1][0];
    }
};
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
- [1391. Check if There is a Valid Path in a Grid](../../1501-2000/1507-check-if-there-is-a-valid-path-in-a-grid/)
- [2116. Check if a Parentheses String Can Be Valid](../../2001-2500/2221-check-if-a-parentheses-string-can-be-valid/)
- [1003. Check If Word Is Valid After Substitutions](../../1001-1500/1045-check-if-word-is-valid-after-substitutions/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path/)
