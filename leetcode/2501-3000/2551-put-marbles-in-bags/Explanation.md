# LeetCode 2551: Put Marbles in Bags

**LeetCode Problem #2551 — Put Marbles in Bags**
Solve LeetCode Put Marbles in Bags using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Put Marbles in Bags |
| LeetCode | #2551 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You have `k` bags. You are given a **0-indexed** integer array `weights` where `weights[i]` is the weight of the `i^th` marble. You are also given the integer `k.`

Divide the marbles into the `k` bags according to the following rules:

No bag is empty. 
 If the `i^th` marble and `j^th` marble are in a bag, then all marbles with an index between the `i^th` and `j^th` indices should also be in that same bag. 
 If a bag consists of all the marbles with an index from `i` to `j` inclusively, then the cost of the bag is `weights[i] + weights[j]`.

The **score** after distributing the marbles is the sum of the costs of all the `k` bags.

Return *the **difference** between the **maximum** and **minimum** scores among marble distributions*.

## Constraints
- `1 <= k <= weights.length <= 10^5`
- `1 <= weights[i] <= 10^9`

## Examples
### Example 1
- **Input:** `weights = [1,3,5,1], k = 2`
- **Output:** `4`
- **Explanation:** The distribution [1],[3,5,1] results in the minimal score of (1+1) + (3+1) = 6. 
The distribution [1,3],[5,1], results in the maximal score of (1+3) + (5+1) = 10. 
Thus, we return their difference 10 - 6 = 4.

### Example 2
- **Input:** `weights = [1, 3], k = 2`
- **Output:** `0`
- **Explanation:** The only distribution possible is [1],[3]. 
Since both the maximal and minimal score are the same, we return 0.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Put Marbles in Bags**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `weights = [1,3,5,1], k = 2`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** The distribution [1],[3,5,1] results in the minimal score of (1+1) + (3+1) = 6. 
The distribution [1,3],[5,1], results in the maximal score of (1+3) + (5+1) = 10. 
Thus, we return their difference 10 - 6 = 4.

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
from typing import List

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        pairs = sorted(weights[i] + weights[i + 1] for i in range(len(weights) - 1))
        return sum(pairs[len(pairs) - (k - 1):]) - sum(pairs[:k - 1])
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
- [2279. Maximum Bags With Full Capacity of Rocks](../../2001-2500/2279-maximum-bags-with-full-capacity-of-rocks/)
- [3413. Maximum Coins From K Consecutive Bags](../../3001-3500/3413-maximum-coins-from-k-consecutive-bags/)
- [2766. Relocate Marbles](../../2501-3000/2766-relocate-marbles/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/put-marbles-in-bags/)
