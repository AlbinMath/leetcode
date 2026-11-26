# LeetCode 781: Rabbits in Forest

**LeetCode Problem #781 — Rabbits in Forest**
Solve LeetCode Rabbits in Forest using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Rabbits in Forest |
| LeetCode | #781 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There is a forest with an unknown number of rabbits. We asked n rabbits **"How many other rabbits have the same color as you?"** and collected the answers in an integer array `answers` where `answers[i]` is the answer of the `i^th` rabbit.

Given the array `answers`, return *the minimum number of rabbits that could be in the forest*.

## Constraints
- `1 <= answers.length <= 1000`
- `0 <= answers[i] < 1000`

## Examples
### Example 1
- **Input:** `answers = [1,1,2]`
- **Output:** `5`
- **Explanation:** The two rabbits that answered "1" could both be the same color, say red.
The rabbit that answered "2" can't be red or the answers would be inconsistent.
Say the rabbit that answered "2" was blue.
Then there should be 2 other blue rabbits in the forest that didn't answer into the array.
The smallest possible number of rabbits in the forest is therefore 5: 3 that answered plus 2 that didn't.

### Example 2
- **Input:** `answers = [10,10,10]`
- **Output:** `11`

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Rabbits in Forest**, we observe the problem requirements and utilize the **Bit Manipulation** technique. By maintaining a **Integer Bitmask**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Integer Bitmask** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `answers = [1,1,2]`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.
4. **Verification:** The two rabbits that answered "1" could both be the same color, say red.
The rabbit that answered "2" can't be red or the answers would be inconsistent.
Say the rabbit that answered "2" was blue.
Then there should be 2 other blue rabbits in the forest that didn't answer into the array.
The smallest possible number of rabbits in the forest is therefore 5: 3 that answered plus 2 that didn't.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Integer Bitmask.

## Pattern
**Bit Manipulation**

## Topics
- Bit Manipulation
- Bitwise Math

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from collections import Counter
from typing import List

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counts = Counter(answers)
        total_rabbits = 0
        
        for ans, count in counts.items():
            group_size = ans + 1
            num_groups = (count + ans) // group_size
            total_rabbits += num_groups * group_size
            
        return total_rabbits
```

## Why This Works
By utilizing **Bit Manipulation**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1110. Delete Nodes And Return Forest](../../1001-1500/1110-delete-nodes-and-return-forest/)
- [8. String to Integer (atoi)](../../0001-0500/0008-string-to-integer-atoi/)
- [89. Gray Code](../../0001-0500/0089-gray-code/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/rabbits-in-forest/)
