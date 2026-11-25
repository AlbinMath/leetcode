# LeetCode 1758: Minimum Changes To Make Alternating Binary String

**LeetCode Problem #1758 — Minimum Changes To Make Alternating Binary String**
Solve LeetCode Minimum Changes To Make Alternating Binary String using C++ and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Changes To Make Alternating Binary String |
| LeetCode | #1758 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a string `s` consisting only of the characters `'0'` and `'1'`. In one operation, you can change any `'0'` to `'1'` or vice versa.

The string is called alternating if no two adjacent characters are equal. For example, the string `"010"` is alternating, while the string `"0100"` is not.

Return *the **minimum** number of operations needed to make* `s` *alternating*.

## Constraints
- `1 <= s.length <= 10^4`
- `s[i]` is either `'0'` or `'1'`.

## Examples
### Example 1
- **Input:** `s = "0100"`
- **Output:** `1`
- **Explanation:** If you change the last character to '1', s will be "0101", which is alternating.

### Example 2
- **Input:** `s = "10"`
- **Output:** `0`
- **Explanation:** s is already alternating.

### Example 3
- **Input:** `s = "1111"`
- **Output:** `2`
- **Explanation:** You need two operations to reach "0101" or "1010".

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Changes To Make Alternating Binary String**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "0100"`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** If you change the last character to '1', s will be "0101", which is alternating.

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
    int minOperations(string s) {
        int count1 = 0;
        int count2 = 0;

        for (int i = 0; i < s.size(); i++) {
            // Pattern 1: 010101...
            if (i % 2 == 0) {
                if (s[i] != '0') count1++;
                if (s[i] != '1') count2++;
            }
            // Pattern 2: 101010...
            else {
                if (s[i] != '1') count1++;
                if (s[i] != '0') count2++;
            }
        }

        return min(count1, count2);
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
- [2914. Minimum Number of Changes to Make Binary String Beautiful](../../2501-3000/2914-minimum-number-of-changes-to-make-binary-string-beautiful/)
- [1864. Minimum Number of Swaps to Make the Binary String Alternating](../../1501-2000/1864-minimum-number-of-swaps-to-make-the-binary-string-alternating/)
- [1888. Minimum Number of Flips to Make the Binary String Alternating](../../1501-2000/1888-minimum-number-of-flips-to-make-the-binary-string-alternating/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/)
