# LeetCode 49: Group Anagrams

**LeetCode Problem #49 — Group Anagrams**
Solve LeetCode Group Anagrams using JavaScript, Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Group Anagrams |
| LeetCode | #49 |
| Difficulty | Medium |
| Language | JavaScript, Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given an array of strings `strs`, group the anagrams together. You can return the answer in **any order**.

## Constraints
- `1 <= strs.length <= 10^4`
- `0 <= strs[i].length <= 100`
- `strs[i]` consists of lowercase English letters.

## Examples
### Example 1
- **Input:** `strs = ["eat","tea","tan","ate","nat","bat"]`
- **Output:** `[["bat"],["nat","tan"],["ate","eat","tea"]]`
- **Explanation:** There is no string in strs that can be rearranged to form `"bat"`. 
 The strings `"nat"` and `"tan"` are anagrams as they can be rearranged to form each other. 
 The strings `"ate"`, `"eat"`, and `"tea"` are anagrams as they can be rearranged to form each other.

### Example 2
- **Input:** `strs = [""]`
- **Output:** `[[""]]`

### Example 3
- **Input:** `strs = ["a"]`
- **Output:** `[["a"]]`

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Group Anagrams**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `strs = ["eat","tea","tan","ate","nat","bat"]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[["bat"],["nat","tan"],["ate","eat","tea"]]`.
4. **Verification:** There is no string in strs that can be rearranged to form `"bat"`. 
 The strings `"nat"` and `"tan"` are anagrams as they can be rearranged to form each other. 
 The strings `"ate"`, `"eat"`, and `"tea"` are anagrams as they can be rearranged to form each other.

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
var groupAnagrams = function(strs) {
    const map = new Map();

    for (const str of strs) {
        // Sort letters to create a common key
        const key = str.split('').sort().join('');

        if (!map.has(key)) {
            map.set(key, []);
        }

        map.get(key).push(str);
    }

    return Array.from(map.values());
};
```

### Python
```python
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        d = defaultdict(list)
        for s in strs:
            d[''.join(sorted(s))].append(s)
        return list(d.values())
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
- [25. Reverse Nodes in k-Group](../../0001-0500/0025-reverse-nodes-in-k-group/)
- [1282. Group the People Given the Group Size They Belong To](../../1001-1500/1282-group-the-people-given-the-group-size-they-belong-to/)
- [1399. Count Largest Group](../../1001-1500/1399-count-largest-group/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/group-anagrams/)
