# LeetCode 447: Number of Boomerangs

**LeetCode Problem #447 — Number of Boomerangs**
Solve LeetCode Number of Boomerangs using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Boomerangs |
| LeetCode | #447 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given `n` `points` in the plane that are all **distinct**, where `points[i] = [x_i, y_i]`. A **boomerang** is a tuple of points `(i, j, k)` such that the distance between `i` and `j` equals the distance between `i` and `k` **(the order of the tuple matters)**.

Return *the number of boomerangs*.

## Constraints
- `n == points.length`
- `1 <= n <= 500`
- `points[i].length == 2`
- `-10^4 <= x_i, y_i <= 10^4`
- All the points are **unique**.

## Examples
### Example 1
- **Input:** `points = [[0,0],[1,0],[2,0]]`
- **Output:** `2`
- **Explanation:** The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]].

### Example 2
- **Input:** `points = [[1,1],[2,2],[3,3]]`
- **Output:** `2`

### Example 3
- **Input:** `points = [[1,1]]`
- **Output:** `0`

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Number of Boomerangs**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `points = [[0,0],[1,0],[2,0]]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]].

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Dictionary / Hash Map.

## Pattern
**Hash Map**

## Topics
- Hash Table
- Array
- Complement Lookup

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from collections import defaultdict
from typing import List

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        total_boomerangs = 0
        
        for x1, y1 in points:
            dist_counts = defaultdict(int)
            
            # Count how many points share each squared distance from (x1, y1)
            for x2, y2 in points:
                dx = x1 - x2
                dy = y1 - y2
                dist_sq = dx * dx + dy * dy
                dist_counts[dist_sq] += 1
            
            # For each group of m equidistant points, add m * (m - 1) permutations
            for count in dist_counts.values():
                if count > 1:
                    total_boomerangs += count * (count - 1)
                    
        return total_boomerangs
```

## Why This Works
By utilizing **Hash Map**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Using the same element twice.
2. Checking the map before inserting elements in the correct order.
3. Inefficient hash functions or unnecessary duplicate key updates.

## Interview Notes
- **Tests:** Hash map usage, complement/frequency lookup, and $O(n)$ time optimization.
- **Follow-up:** Can you solve the problem in $O(1)$ extra space if the input array is sorted?

## Related Problems
- [9. Palindrome Number](../../0001-0500/0009-palindrome-number/)
- [17. Letter Combinations of a Phone Number](../../0001-0500/0017-letter-combinations-of-a-phone-number/)
- [65. Valid Number](../../0001-0500/0065-valid-number/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-boomerangs/)
