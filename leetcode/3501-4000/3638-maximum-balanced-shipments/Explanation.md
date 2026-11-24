# LeetCode 3638: Maximum Balanced Shipments

**LeetCode Problem #3638 — Maximum Balanced Shipments**
Solve LeetCode Maximum Balanced Shipments using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Balanced Shipments |
| LeetCode | #3638 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array weight of length n , representing the weights of n parcels arranged in a straight line. A shipment is defined as a contiguous subarray of parcels. A shipment is considered balanced if the weight of the last parcel is **strictly less** than the maximum weight among all parcels in that shipment.

Select a set of non-overlapping , contiguous, balanced shipments such that each parcel appears in at most one shipment (parcels may remain unshipped).

Return the maximum possible number of balanced shipments that can be formed.

## Constraints
- 2 <= n <= 10^5
- 1 <= weight[i] <= 10^9

## Examples
### Example 1
- **Input:** `weight = [2,5,1,4,3]`
- **Output:** `2`
- **Explanation:** We can form the maximum of two balanced shipments as follows: 

 
 Shipment 1: `[2, 5, 1]`

 
 Maximum parcel weight = 5 
 Last parcel weight = 1, which is strictly less than 5. Thus, it's balanced. 
 
 
 Shipment 2: `[4, 3]`
 
 Maximum parcel weight = 4 
 Last parcel weight = 3, which is strictly less than 4. Thus, it's balanced. 
 
 
 

 It is impossible to partition the parcels to achieve more than two balanced shipments, so the answer is 2.

### Example 2
- **Input:** `weight = [4,4]`
- **Output:** `0`
- **Explanation:** No balanced shipment can be formed in this case: 

 
 A shipment `[4, 4]` has maximum weight 4 and the last parcel's weight is also 4, which is not strictly less. Thus, it's not balanced. 
 Single-parcel shipments `[4]` have the last parcel weight equal to the maximum parcel weight, thus not balanced. 
 

 As there is no way to form even one balanced shipment, the answer is 0.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Balanced Shipments**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `weight = [2,5,1,4,3]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** We can form the maximum of two balanced shipments as follows: 

 
 Shipment 1: `[2, 5, 1]`

 
 Maximum parcel weight = 5 
 Last parcel weight = 1, which is strictly less than 5. Thus, it's balanced. 
 
 
 Shipment 2: `[4, 3]`
 
 Maximum parcel weight = 4 
 Last parcel weight = 3, which is strictly less than 4. Thus, it's balanced. 
 
 
 

 It is impossible to partition the parcels to achieve more than two balanced shipments, so the answer is 2.

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
    def maxBalancedShipments(self, weight: List[int]) -> int:
        mx = 0
        count = 0
        for w in weight:
            if w < mx:
                count += 1
                mx = 0
            else:
                mx = w if w > mx else mx
        return count
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
- [2926. Maximum Balanced Subsequence Sum](../../2501-3000/2926-maximum-balanced-subsequence-sum/)
- [3755. Find Maximum Balanced XOR Subarray Length](../../3501-4000/3755-find-maximum-balanced-xor-subarray-length/)
- [53. Maximum Subarray](../../0001-0500/0053-maximum-subarray/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-balanced-shipments/)
