# LeetCode 3842: Toggle Light Bulbs

**LeetCode Problem #3842 — Toggle Light Bulbs**
Solve LeetCode Toggle Light Bulbs using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Toggle Light Bulbs |
| LeetCode | #3842 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array `bulbs` of integers between 1 and 100.

There are 100 light bulbs numbered from 1 to 100. All of them are switched off initially.

For each element `bulbs[i]` in the array `bulbs`:

If the `bulbs[i]^th` light bulb is currently off, switch it on. 
 Otherwise, switch it off.

Return the list of integers denoting the light bulbs that are on in the end, **sorted** in **ascending** order. If no bulb is on, return an empty list.

## Constraints
- `1 <= bulbs.length <= 100`
- `1 <= bulbs[i] <= 100`

## Examples
### Example 1
- **Input:** `bulbs = [10,30,20,10]`
- **Output:** `[20,30]`
- **Explanation:** The `bulbs[0] = 10^th` light bulb is currently off. We switch it on. 
 The `bulbs[1] = 30^th` light bulb is currently off. We switch it on. 
 The `bulbs[2] = 20^th` light bulb is currently off. We switch it on. 
 The `bulbs[3] = 10^th` light bulb is currently on. We switch it off. 
 In the end, the 20^th and the 30^th light bulbs are on.

### Example 2
- **Input:** `bulbs = [100,100]`
- **Output:** `[]`
- **Explanation:** The `bulbs[0] = 100^th` light bulb is currently off. We switch it on. 
 The `bulbs[1] = 100^th` light bulb is currently on. We switch it off. 
 In the end, no light bulb is on.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Toggle Light Bulbs**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `bulbs = [10,30,20,10]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[20,30]`.
4. **Verification:** The `bulbs[0] = 10^th` light bulb is currently off. We switch it on. 
 The `bulbs[1] = 30^th` light bulb is currently off. We switch it on. 
 The `bulbs[2] = 20^th` light bulb is currently off. We switch it on. 
 The `bulbs[3] = 10^th` light bulb is currently on. We switch it off. 
 In the end, the 20^th and the 30^th light bulbs are on.

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
class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        on = set()
        for b in bulbs:
            on ^= {b}
        return sorted(on)
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
- [5. Longest Palindromic Substring](../../0001-0500/0005-longest-palindromic-substring/)
- [26. Remove Duplicates from Sorted Array](../../0001-0500/0026-remove-duplicates-from-sorted-array/)
- [27. Remove Element](../../0001-0500/0027-remove-element/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/toggle-light-bulbs/)
