# LeetCode 927: Three Equal Parts

**LeetCode Problem #927 — Three Equal Parts**
Solve LeetCode Three Equal Parts using Python and Linked List. This solution finds the optimal result using Pointer Traversal & Node Manipulation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Three Equal Parts |
| LeetCode | #927 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Pointer Traversal & Node Manipulation |
| Data Structure | Linked List |
| Pattern | Linked List |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array `arr` which consists of only zeros and ones, divide the array into **three non-empty parts** such that all of these parts represent the same binary value.

If it is possible, return any `[i, j]` with `i + 1 < j`, such that:

`arr[0], arr[1], ..., arr[i]` is the first part, 
 `arr[i + 1], arr[i + 2], ..., arr[j - 1]` is the second part, and 
 `arr[j], arr[j + 1], ..., arr[arr.length - 1]` is the third part. 
 All three parts have equal binary values.

If it is not possible, return `[-1, -1]`.

Note that the entire part is used when considering what binary value it represents. For example, `[1,1,0]` represents `6` in decimal, not `3`. Also, leading zeros **are allowed**, so `[0,1,1]` and `[1,1]` represent the same value.

## Constraints
- `3 <= arr.length <= 3 * 10^4`
- `arr[i]` is `0` or `1`

## Examples
### Example 1
- **Input:** `arr = [1,0,1,0,1]`
- **Output:** `[0,3]`

### Example 2
- **Input:** `arr = [1,1,0,1,1]`
- **Output:** `[-1,-1]`

### Example 3
- **Input:** `arr = [1,1,0,0,1]`
- **Output:** `[0,2]`

## Key Insight
Leverage **Linked List** with **Linked List** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Three Equal Parts**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `arr = [1,0,1,0,1]`.
2. **Processing Steps:** We apply **Pointer Traversal & Node Manipulation** using our **Linked List**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[0,3]`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Linked List.

## Pattern
**Linked List**

## Topics
- Linked List
- Two Pointers

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def threeEqualParts(self, arr: list[int]) -> list[int]:
        total_ones = sum(arr)
        
        if total_ones == 0:
            return [0, 2]
        if total_ones % 3 != 0:
            return [-1, -1]
            
        k = total_ones // 3
        p1 = p2 = p3 = -1
        ones_seen = 0
        for idx, bit in enumerate(arr):
            if bit == 1:
                ones_seen += 1
                if ones_seen == 1:
                    p1 = idx
                elif ones_seen == k + 1:
                    p2 = idx
                elif ones_seen == 2 * k + 1:
                    p3 = idx
                    break
        n = len(arr)
        while p3 < n:
            if arr[p1] != arr[p2] or arr[p2] != arr[p3]:
                return [-1, -1]
            p1 += 1
            p2 += 1
            p3 += 1
            
        return [p1 - 1, p2]
```

## Why This Works
By utilizing **Linked List**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1013. Partition Array Into Three Parts With Equal Sum](../../1001-1500/1013-partition-array-into-three-parts-with-equal-sum/)
- [416. Partition Equal Subset Sum](../../0001-0500/0416-partition-equal-subset-sum/)
- [453. Minimum Moves to Equal Array Elements](../../0001-0500/0453-minimum-moves-to-equal-array-elements/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/three-equal-parts/)
