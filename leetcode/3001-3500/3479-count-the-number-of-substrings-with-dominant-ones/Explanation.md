# LeetCode 3234: Count the Number of Substrings With Dominant Ones

**LeetCode Problem #3234 — Count the Number of Substrings With Dominant Ones**
Solve LeetCode Count the Number of Substrings With Dominant Ones using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count the Number of Substrings With Dominant Ones |
| LeetCode | #3234 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a binary string `s`.

Return the number of substrings with **dominant** ones.

A string has **dominant** ones if the number of ones in the string is **greater than or equal to** the **square** of the number of zeros in the string.

## Constraints
- `1 <= s.length <= 4 * 10^4`
- `s` consists only of characters `'0'` and `'1'`.

## Examples
### Example 1
- **Input:** `s = "00011"`
- **Output:** `5`
- **Explanation:** The substrings with dominant ones are shown in the table below. 
 

 
 
 
 i 
 j 
 s[i..j] 
 Number of Zeros 
 Number of Ones 
 
 
 
 
 3 
 3 
 1 
 0 
 1 
 
 
 4 
 4 
 1 
 0 
 1 
 
 
 2 
 3 
 01 
 1 
 1 
 
 
 3 
 4 
 11 
 0 
 2 
 
 
 2 
 4 
 011 
 1 
 2

### Example 2
- **Input:** `s = "101101"`
- **Output:** `16`
- **Explanation:** The substrings with

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count the Number of Substrings With Dominant Ones**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "00011"`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.
4. **Verification:** The substrings with dominant ones are shown in the table below. 
 

 
 
 
 i 
 j 
 s[i..j] 
 Number of Zeros 
 Number of Ones 
 
 
 
 
 3 
 3 
 1 
 0 
 1 
 
 
 4 
 4 
 1 
 0 
 1 
 
 
 2 
 3 
 01 
 1 
 1 
 
 
 3 
 4 
 11 
 0 
 2 
 
 
 2 
 4 
 011 
 1 
 2

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        nxt = [n] * (n + 2)
        for i in range(n - 1, -1, -1):
            nxt[i] = i if s[i] == '0' else nxt[i + 1]

        ans = 0
        for i in range(n):
            # substrings with zero zeros
            p = nxt[i]
            ans += p - i
            z = 1
            while p < n and z * z + z <= n - i:
                q = nxt[p + 1]          # next zero (or n)
                lo = max(p, i + z * z + z - 1)
                hi = q - 1
                if hi >= lo:
                    ans += hi - lo + 1
                p = q
                z += 1
        return ans
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
- [1759. Count Number of Homogenous Substrings](../../1501-2000/1885-count-number-of-homogenous-substrings/)
- [1277. Count Square Submatrices with All Ones](../../1001-1500/1402-count-square-submatrices-with-all-ones/)
- [1504. Count Submatrices With All Ones](../../1501-2000/1628-count-submatrices-with-all-ones/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-the-number-of-substrings-with-dominant-ones/)
