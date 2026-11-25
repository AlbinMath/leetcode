# LeetCode 3864: Minimum Cost to Partition a Binary String

**LeetCode Problem #3864 — Minimum Cost to Partition a Binary String**
Solve LeetCode Minimum Cost to Partition a Binary String using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Cost to Partition a Binary String |
| LeetCode | #3864 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a binary string `s` and two integers `encCost` and `flatCost`.

For each index `i`, `s[i] = '1'` indicates that the `i^th` element is sensitive, and `s[i] = '0'` indicates that it is not.

The string must be partitioned into **segments**. Initially, the entire string forms a single segment.

For a segment of length `L` containing `X` sensitive elements:

If `X = 0`, the cost is `flatCost`. 
 If `X > 0`, the cost is `L * X * encCost`.

If a segment has **even length**, you may split it into **two contiguous segments** of **equal** length and the cost of this split is the **sum** of **costs** of the resulting segments.

Return an integer denoting the **minimum possible total cost** over all valid partitions.

## Constraints
- `1 <= s.length <= 10^5`
- `s` consists only of `'0'` and `'1'`.
- `1 <= encCost, flatCost <= 10^5`

## Examples
### Example 1
- **Input:** `s = "1010", encCost = 2, flatCost = 1`
- **Output:** `6`
- **Explanation:** The entire string `s = "1010"` has length 4 and contains 2 sensitive elements, giving a cost of `4 * 2 * 2 = 16`. 
 Since the length is even, it can be split into `"10"` and `"10"`. Each segment has length 2 and contains 1 sensitive element, so each costs `2 * 1 * 2 = 4`, giving a total of 8. 
 Splitting both segments into four single-character segments yields the segments `"1"`, `"0"`, `"1"`, and `"0"`. A segment containing `"1"` has length 1 and exactly one sensitive element, giving a cost of `1 * 1 * 2 = 2`, while a segment containing `"0"` has no sensitive elements and therefore costs `flatCost = 1`. 
 ​​​​​​​The total cost is thus `2 + 1 + 2 + 1 = 6`, which is the minimum possible total cost.

### Example 2
- **Input:** `s = "1010", encCost = 3, flatCost = 10`
- **Output:** `12`
- **Explanation:** The entire string `s = "1010"` has length 4 and contains 2 sensitive elements, giving a cost of `4 * 2 * 3 = 24`. 
 Since the length is even, it can be split into two segments `"10"` and `"10"`. 
 Each segment has length 2 and contains one sensitive element, so each costs `2 * 1 * 3 = 6`, giving a total of 12, which is the minimum possible total cost.

### Example 3
- **Input:** `s = "00", encCost = 1, flatCost = 2`
- **Output:** `2`
- **Explanation:** The string `s = "00"` has length 2 and contains no sensitive elements, so storing it as a single segment costs `flatCost = 2`, which is the minimum possible total cost.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Cost to Partition a Binary String**, we observe the problem requirements and utilize the **Tree & Graph** technique. We perform a recursive Depth-First Search (DFS) traversal. The algorithm handles base cases at leaf nodes and aggregates results from subtrees back up to the root.

## Algorithm
1. Define base cases for null/leaf nodes.
2. Recursively traverse child nodes.
3. Combine child results to determine current node output.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "1010", encCost = 2, flatCost = 1`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `6`.
4. **Verification:** The entire string `s = "1010"` has length 4 and contains 2 sensitive elements, giving a cost of `4 * 2 * 2 = 16`. 
 Since the length is even, it can be split into `"10"` and `"10"`. Each segment has length 2 and contains 1 sensitive element, so each costs `2 * 1 * 2 = 4`, giving a total of 8. 
 Splitting both segments into four single-character segments yields the segments `"1"`, `"0"`, `"1"`, and `"0"`. A segment containing `"1"` has length 1 and exactly one sensitive element, giving a cost of `1 * 1 * 2 = 2`, while a segment containing `"0"` has no sensitive elements and therefore costs `flatCost = 1`. 
 ​​​​​​​The total cost is thus `2 + 1 + 2 + 1 = 6`, which is the minimum possible total cost.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Tree / Graph / Grid.

## Pattern
**Tree & Graph**

## Topics
- Tree
- Graph
- DFS
- BFS

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def minCost(self, s, encCost, flatCost):
        n = len(s)
        pre = [0] * (n + 1)
        for i, ch in enumerate(s):
            pre[i + 1] = pre[i] + (ch == '1')

        def solve(l, r):
            L = r - l
            X = pre[r] - pre[l]
            whole = flatCost if X == 0 else L * X * encCost
            if L % 2 == 0:
                mid = (l + r) // 2
                split = solve(l, mid) + solve(mid, r)
                return min(whole, split)
            return whole

        return solve(0, n)
```

## Why This Works
By utilizing **Tree & Graph**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [2767. Partition String Into Minimum Beautiful Substrings](../../2501-3000/2767-partition-string-into-minimum-beautiful-substrings/)
- [1758. Minimum Changes To Make Alternating Binary String](../../1501-2000/1758-minimum-changes-to-make-alternating-binary-string/)
- [1864. Minimum Number of Swaps to Make the Binary String Alternating](../../1501-2000/1864-minimum-number-of-swaps-to-make-the-binary-string-alternating/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-cost-to-partition-a-binary-string/)
