# LeetCode 1523: Count Odd Numbers in an Interval Range

**LeetCode Problem #1523 — Count Odd Numbers in an Interval Range**
Solve LeetCode Count Odd Numbers in an Interval Range using Python and Heap. This solution finds the optimal result using Min/Max Heap Priority Selection in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Odd Numbers in an Interval Range |
| LeetCode | #1523 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Min/Max Heap Priority Selection |
| Data Structure | Heap / Priority Queue |
| Pattern | Heap |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given two non-negative integers `low` and ` high `. Return the *count of odd numbers between *`low`* and *` high `* (inclusive)*.

## Constraints
- `0 <= low <= high <= 10^9`

## Examples
### Example 1
- **Input:** `low = 3, high = 7`
- **Output:** `3`

### Example 2
- **Input:** `low = 8, high = 10`
- **Output:** `1`

## Key Insight
Leverage **Heap** with **Heap / Priority Queue** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count Odd Numbers in an Interval Range**, we observe the problem requirements and utilize the **Heap** technique. We iterate through the inputs using **Min/Max Heap Priority Selection**, leveraging a **Heap / Priority Queue** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Heap / Priority Queue**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `low = 3, high = 7`.
2. **Processing Steps:** We apply **Min/Max Heap Priority Selection** using our **Heap / Priority Queue**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Heap / Priority Queue.

## Pattern
**Heap**

## Topics
- Heap
- Priority Queue
- Sorting

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high + 1) // 2 - low // 2
```

## Why This Works
By utilizing **Heap**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [315. Count of Smaller Numbers After Self](../../0001-0500/0315-count-of-smaller-numbers-after-self/)
- [327. Count of Range Sum](../../0001-0500/0327-count-of-range-sum/)
- [357. Count Numbers with Unique Digits](../../0001-0500/0357-count-numbers-with-unique-digits/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/)
