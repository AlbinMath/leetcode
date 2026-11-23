# LeetCode 1702: Maximum Binary String After Change

**LeetCode Problem #1702 — Maximum Binary String After Change**
Solve LeetCode Maximum Binary String After Change using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Binary String After Change |
| LeetCode | #1702 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a binary string `binary` consisting of only `0`'s or `1`'s. You can apply each of the following operations any number of times:

Operation 1: If the number contains the substring `"00"`, you can replace it with `"10"`.

For example, `" 00 010" -> " 10 010`" 
 
 
 Operation 2: If the number contains the substring `"10"`, you can replace it with `"01"`.
 
 For example, `"000 10 " -> "000 01 "`

*Return the **maximum binary string** you can obtain after any number of operations. Binary string `x` is greater than binary string `y` if `x`'s decimal representation is greater than `y`'s decimal representation.*

## Constraints
- `1 <= binary.length <= 10^5`
- `binary` consist of `'0'` and `'1'`.

## Examples
### Example 1
- **Input:** `binary = "000110"`
- **Output:** `"111011"`
- **Explanation:** A valid transformation sequence can be:
"0001 10 " -> "0001 01 " 
" 00 0101" -> " 10 0101" 
"1 00 101" -> "1 10 101" 
"110 10 1" -> "110 01 1" 
"11 00 11" -> "11 10 11"

### Example 2
- **Input:** `binary = "01"`
- **Output:** `"01"`
- **Explanation:** "01" cannot be transformed any further.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Binary String After Change**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `binary = "000110"`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"111011"`.
4. **Verification:** A valid transformation sequence can be:
"0001 10 " -> "0001 01 " 
" 00 0101" -> " 10 0101" 
"1 00 101" -> "1 10 101" 
"110 10 1" -> "110 01 1" 
"11 00 11" -> "11 10 11"

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
    def maximumBinaryString(self, binary: str) -> str:
        first = binary.find('0')
        if first == -1:
            return binary

        zeros = binary.count('0')
        n = len(binary)
        pos = first + zeros - 1  # index of the single remaining zero

        res = ['1'] * n
        res[pos] = '0'
        return ''.join(res)
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
- [1422. Maximum Score After Splitting a String](../../1501-2000/1537-maximum-score-after-splitting-a-string/)
- [606. Construct String from Binary Tree](../../0501-1000/0606-construct-string-from-binary-tree/)
- [761. Special Binary String](../../0501-1000/0763-special-binary-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-binary-string-after-change/)
