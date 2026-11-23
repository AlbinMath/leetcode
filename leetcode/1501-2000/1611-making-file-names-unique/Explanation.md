# LeetCode 1487: Making File Names Unique

**LeetCode Problem #1487 — Making File Names Unique**
Solve LeetCode Making File Names Unique using Python and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Making File Names Unique |
| LeetCode | #1487 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an array of strings `names` of size `n`. You will create `n` folders in your file system **such that**, at the `i^th` minute, you will create a folder with the name `names[i]`.

Since two files **cannot** have the same name, if you enter a folder name that was previously used, the system will have a suffix addition to its name in the form of `(k)`, where, `k` is the **smallest positive integer** such that the obtained name remains unique.

Return *an array of strings of length *`n` where `ans[i]` is the actual name the system will assign to the `i^th` folder when you create it.

## Constraints
- `1 <= names.length <= 5 * 10^4`
- `1 <= names[i].length <= 20`
- `names[i]` consists of lowercase English letters, digits, and/or round brackets.

## Examples
### Example 1
- **Input:** `names = ["pes","fifa","gta","pes(2019)"]`
- **Output:** `["pes","fifa","gta","pes(2019)"]`
- **Explanation:** Let's see how the file system creates folder names:
"pes" --> not assigned before, remains "pes"
"fifa" --> not assigned before, remains "fifa"
"gta" --> not assigned before, remains "gta"
"pes(2019)" --> not assigned before, remains "pes(2019)"

### Example 2
- **Input:** `names = ["gta","gta(1)","gta","avalon"]`
- **Output:** `["gta","gta(1)","gta(2)","avalon"]`
- **Explanation:** Let's see how the file system creates folder names:
"gta" --> not assigned before, remains "gta"
"gta(1)" --> not assigned before, remains "gta(1)"
"gta" --> the name is reserved, system adds (k), since "gta(1)" is also reserved, systems put k = 2. it becomes "gta(2)"
"avalon" --> not assigned before, remains "avalon"

### Example 3
- **Input:** `names = ["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece"]`
- **Output:** `["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece(4)"]`
- **Explanation:** When the last folder is created, the smallest positive valid k is 4, and it becomes "onepiece(4)".

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Making File Names Unique**, we observe the problem requirements and utilize the **Binary Search** technique. By maintaining a **Sorted Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Sorted Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `names = ["pes","fifa","gta","pes(2019)"]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `["pes","fifa","gta","pes(2019)"]`.
4. **Verification:** Let's see how the file system creates folder names:
"pes" --> not assigned before, remains "pes"
"fifa" --> not assigned before, remains "fifa"
"gta" --> not assigned before, remains "gta"
"pes(2019)" --> not assigned before, remains "pes(2019)"

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Sorted Array.

## Pattern
**Binary Search**

## Topics
- Binary Search
- Divide and Conquer
- Search Space

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        used = set()
        next_k = {}
        res = []

        for name in names:
            if name not in used:
                used.add(name)
                res.append(name)
                continue

            k = next_k.get(name, 1)
            while f"{name}({k})" in used:
                k += 1
            new_name = f"{name}({k})"
            used.add(new_name)
            next_k[name] = k + 1
            res.append(new_name)

        return res
```

## Why This Works
By utilizing **Binary Search**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Applying standard binary search without accounting for array rotation or duplicates.
2. Off-by-one errors when updating boundary pointers (`left = mid + 1` vs `right = mid - 1`).
3. Integer overflow during midpoint calculation (use `mid = left + (right - left) // 2`).

## Interview Notes
- **Tests:** Logarithmic search space reduction, boundary handling, and invariant preservation.
- **Follow-up:** How does performance change if the array contains duplicate elements?

## Related Problems
- [194. Transpose File](../../0001-0500/0194-transpose-file/)
- [388. Longest Absolute File Path](../../0001-0500/0388-longest-absolute-file-path/)
- [609. Find Duplicate File in System](../../0501-1000/0609-find-duplicate-file-in-system/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/making-file-names-unique/)
