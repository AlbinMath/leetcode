# LeetCode 1207: Unique Number of Occurrences

**LeetCode Problem #1207 — Unique Number of Occurrences**
Solve LeetCode Unique Number of Occurrences using JavaScript, Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Unique Number of Occurrences |
| LeetCode | #1207 |
| Difficulty | Easy |
| Language | JavaScript, Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given an array of integers `arr`, return `true` *if the number of occurrences of each value in the array is **unique** or *`false`* otherwise*.

## Constraints
- `1 <= arr.length <= 1000`
- `-1000 <= arr[i] <= 1000`

## Examples
### Example 1
- **Input:** `arr = [1,2,2,1,1,3]`
- **Output:** `true`
- **Explanation:** The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

### Example 2
- **Input:** `arr = [1,2]`
- **Output:** `false`

### Example 3
- **Input:** `arr = [-3,0,1,-3,1,1,1,-3,10,0]`
- **Output:** `true`

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Unique Number of Occurrences**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `arr = [1,2,2,1,1,3]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

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
JavaScript, Python

## Source Code
- [solution.js](./solution.js)
- [solution.py](./solution.py)


### JavaScript
```javascript
var uniqueOccurrences = function(arr) {
    const freq = new Map();

    // Count occurrences of each number
    for (const num of arr) {
        freq.set(num, (freq.get(num) || 0) + 1);
    }

    // Store occurrence counts in a Set
    const counts = new Set(freq.values());

    // If sizes differ, some counts are repeated
    return counts.size === freq.size;
};
```

### Python
```python
from typing import List
from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = Counter(arr)
        return len(counts.values()) == len(set(counts.values()))
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
- [1481. Least Number of Unique Integers after K Removals](../../1501-2000/1604-least-number-of-unique-integers-after-k-removals/)
- [1593. Split a String Into the Max Number of Unique Substrings](../../1501-2000/1715-split-a-string-into-the-max-number-of-unique-substrings/)
- [1987. Number of Unique Good Subsequences](../../2001-2500/2115-number-of-unique-good-subsequences/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/unique-number-of-occurrences/)
