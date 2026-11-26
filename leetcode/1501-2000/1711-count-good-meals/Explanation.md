# LeetCode 1711: Count Good Meals

**LeetCode Problem #1711 — Count Good Meals**
Solve LeetCode Count Good Meals using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Good Meals |
| LeetCode | #1711 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
A **good meal** is a meal that contains **exactly two different food items** with a sum of deliciousness equal to a power of two.

You can pick **any** two different foods to make a good meal.

Given an array of integers `deliciousness` where `deliciousness[i]` is the deliciousness of the `i^​​​​​​th​​​​`​​​​ item of food, return *the number of different **good meals** you can make from this list modulo* `10^9 + 7`.

Note that items with different indices are considered different even if they have the same deliciousness value.

## Constraints
- `1 <= deliciousness.length <= 10^5`
- `0 <= deliciousness[i] <= 2^20`

## Examples
### Example 1
- **Input:** `deliciousness = [1,3,5,7,9]`
- **Output:** `4`
- **Explanation:** The good meals are (1,3), (1,7), (3,5) and, (7,9).
Their respective sums are 4, 8, 8, and 16, all of which are powers of 2.

### Example 2
- **Input:** `deliciousness = [1,1,1,3,3,3,7]`
- **Output:** `15`
- **Explanation:** The good meals are (1,1) with 3 ways, (1,3) with 9 ways, and (1,7) with 3 ways.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count Good Meals**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `deliciousness = [1,3,5,7,9]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** The good meals are (1,3), (1,7), (3,5) and, (7,9).
Their respective sums are 4, 8, 8, and 16, all of which are powers of 2.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from collections import defaultdict
from typing import List

class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        MOD = 10**9 + 7
        # Max possible sum is 2^20 + 2^20 = 2^21
        powers_of_two = [1 << i for i in range(22)]
        
        seen = defaultdict(int)
        total_meals = 0
        
        for x in deliciousness:
            for power in powers_of_two:
                target = power - x
                if target in seen:
                    total_meals = (total_meals + seen[target]) % MOD
            seen[x] += 1
            
        return total_meals
```

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1448. Count Good Nodes in Binary Tree](../../1001-1500/1448-count-good-nodes-in-binary-tree/)
- [1534. Count Good Triplets](../../1501-2000/1534-count-good-triplets/)
- [1922. Count Good Numbers](../../1501-2000/1922-count-good-numbers/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-good-meals/)
