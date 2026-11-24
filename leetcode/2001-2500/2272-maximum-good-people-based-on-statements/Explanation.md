# LeetCode 2151: Maximum Good People Based on Statements

**LeetCode Problem #2151 — Maximum Good People Based on Statements**
Solve LeetCode Maximum Good People Based on Statements using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Good People Based on Statements |
| LeetCode | #2151 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
There are two types of persons:

The **good person**: The person who always tells the truth. 
 The **bad person**: The person who might tell the truth and might lie.

You are given a **0-indexed** 2D integer array `statements` of size `n x n` that represents the statements made by `n` people about each other. More specifically, `statements[i][j]` could be one of the following:

`0` which represents a statement made by person `i` that person `j` is a **bad** person. 
 `1` which represents a statement made by person `i` that person `j` is a **good** person. 
 `2` represents that **no statement** is made by person `i` about person `j`.

Additionally, no person ever makes a statement about themselves. Formally, we have that `statements[i][i] = 2` for all `0 <= i < n`.

Return *the **maximum** number of people who can be **good** based on the statements made by the *`n`* people*.

## Constraints
- `n == statements.length == statements[i].length`
- `2 <= n <= 15`
- `statements[i][j]` is either `0`, `1`, or `2`.
- `statements[i][i] == 2`

## Examples
### Example 1
- **Input:** `statements = [[2,1,2],[1,2,2],[2,0,2]]`
- **Output:** `2`
- **Explanation:** Each person makes a single statement.
- Person 0 states that person 1 is good.
- Person 1 states that person 0 is good.
- Person 2 states that person 1 is bad.
Let's take person 2 as the key.
- Assuming that person 2 is a good person:
 - Based on the statement made by person 2, person 1 is a bad person.
 - Now we know for sure that person 1 is bad and person 2 is good.
 - Based on the statement made by person 1, and since person 1 is bad, they could be:
 - telling the truth. There will be a contradiction in this case and this assumption is invalid.
 - lying. In this case, person 0 is also a bad person and lied in their statement.
 -

### Example 2
- **Input:** `statements = [[2,0],[0,2]]`
- **Output:** `1`
- **Explanation:** Each person makes a single statement.
- Person 0 states that person 1 is bad.
- Person 1 states that person 0 is bad.
Let's take person 0 as the key.
- Assuming that person 0 is a good person:
 - Based on the statement made by person 0, person 1 is a bad person and was lying.
 -

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Good People Based on Statements**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `statements = [[2,1,2],[1,2,2],[2,0,2]]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** Each person makes a single statement.
- Person 0 states that person 1 is good.
- Person 1 states that person 0 is good.
- Person 2 states that person 1 is bad.
Let's take person 2 as the key.
- Assuming that person 2 is a good person:
 - Based on the statement made by person 2, person 1 is a bad person.
 - Now we know for sure that person 1 is bad and person 2 is good.
 - Based on the statement made by person 1, and since person 1 is bad, they could be:
 - telling the truth. There will be a contradiction in this case and this assumption is invalid.
 - lying. In this case, person 0 is also a bad person and lied in their statement.
 -

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
from typing import List

class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        n = len(statements)

        # For each person: bits they claim are good, and bits they claim are bad
        says_good = [0] * n
        says_bad = [0] * n
        for i in range(n):
            for j in range(n):
                if statements[i][j] == 1:
                    says_good[i] |= 1 << j
                elif statements[i][j] == 0:
                    says_bad[i] |= 1 << j

        best = 0
        for mask in range(1 << n):
            cnt = mask.bit_count()
            if cnt <= best:
                continue
            ok = True
            for i in range(n):
                if mask >> i & 1:
                    # good person i: all "good" claims must be in mask,
                    # all "bad" claims must be outside mask
                    if says_good[i] & ~mask or says_bad[i] & mask:
                        ok = False
                        break
            if ok:
                best = cnt
        return best
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
- [1793. Maximum Score of a Good Subarray](../../1501-2000/1918-maximum-score-of-a-good-subarray/)
- [3575. Maximum Good Subtree Score](../../3501-4000/3875-maximum-good-subtree-score/)
- [483. Smallest Good Base](../../0001-0500/0483-smallest-good-base/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-good-people-based-on-statements/)
