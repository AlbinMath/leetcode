# LeetCode 1436: Destination City

**LeetCode Problem #1436 — Destination City**
Solve LeetCode Destination City using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Destination City |
| LeetCode | #1436 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given the array `paths`, where `paths[i] = [cityA_i, cityB_i]` means there exists a direct path going from `cityA_i` to `cityB_i`. *Return the destination city, that is, the city without any path outgoing to another city.*

It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.

## Constraints
- `1 <= paths.length <= 100`
- `paths[i].length == 2`
- `1 <= cityA_i.length, cityB_i.length <= 10`
- `cityA_i != cityB_i`
- All strings consist of lowercase and uppercase English letters and the space character.

## Examples
### Example 1
- **Input:** `paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]`
- **Output:** `"Sao Paulo"`
- **Explanation:** Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".

### Example 2
- **Input:** `paths = [["B","C"],["D","B"],["C","A"]]`
- **Output:** `"A"`
- **Explanation:** All possible trips are: 
"D" -> "B" -> "C" -> "A". 
"B" -> "C" -> "A". 
"C" -> "A". 
"A". 
Clearly the destination city is "A".

### Example 3
- **Input:** `paths = [["A","Z"]]`
- **Output:** `"Z"`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Destination City**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"Sao Paulo"`.
4. **Verification:** Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".

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
    def destCity(self, paths: list[list[str]]) -> str:
        starting_cities = {path[0] for path in paths}

        for start, destination in paths:
            if destination not in starting_cities:
                return destination
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
- [807. Max Increase to Keep City Skyline](../../0501-1000/0825-max-increase-to-keep-city-skyline/)
- [1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance](../../1001-1500/1456-find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/)
- [1466. Reorder Routes to Make All Paths Lead to the City Zero](../../1501-2000/1576-reorder-routes-to-make-all-paths-lead-to-the-city-zero/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/destination-city/)
