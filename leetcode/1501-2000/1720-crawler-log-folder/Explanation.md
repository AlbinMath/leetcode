# LeetCode 1598: Crawler Log Folder

**LeetCode Problem #1598 — Crawler Log Folder**
Solve LeetCode Crawler Log Folder using C++ and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Crawler Log Folder |
| LeetCode | #1598 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
The Leetcode file system keeps a log each time some user performs a *change folder* operation.

The operations are described below:

`"../"` : Move to the parent folder of the current folder. (If you are already in the main folder, **remain in the same folder**). 
 `"./"` : Remain in the same folder. 
 `"x/"` : Move to the child folder named `x` (This folder is **guaranteed to always exist**).

You are given a list of strings `logs` where `logs[i]` is the operation performed by the user at the `i^th` step.

The file system starts in the main folder, then the operations in `logs` are performed.

Return *the minimum number of operations needed to go back to the main folder after the change folder operations.*

## Constraints
- `1 <= logs.length <= 10^3`
- `2 <= logs[i].length <= 10`
- `logs[i]` contains lowercase English letters, digits, `'.'`, and `'/'`.
- `logs[i]` follows the format described in the statement.
- Folder names consist of lowercase English letters and digits.

## Examples
### Example 1
- **Input:** `logs = ["d1/","d2/","../","d21/","./"]`
- **Output:** `2`
- **Explanation:** Use this change folder operation "../" 2 times and go back to the main folder.

### Example 2
- **Input:** `logs = ["d1/","d2/","./","d3/","../","d31/"]`
- **Output:** `3`

### Example 3
- **Input:** `logs = ["d1/","../","../","../"]`
- **Output:** `0`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Crawler Log Folder**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `logs = ["d1/","d2/","../","d21/","./"]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** Use this change folder operation "../" 2 times and go back to the main folder.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)


```cpp
class Solution {
public:
    int minOperations(vector<string>& logs) {
        int depth = 0;

        for (string log : logs) {
            if (log == "../") {
                if (depth > 0) {
                    depth--;
                }
            }
            else if (log == "./") {
                continue;
            }
            else {
                depth++;
            }
        }

        return depth;
    }
};
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
- [937. Reorder Data in Log Files](../../0501-1000/0974-reorder-data-in-log-files/)
- [5. Longest Palindromic Substring](../../0001-0500/0005-longest-palindromic-substring/)
- [26. Remove Duplicates from Sorted Array](../../0001-0500/0026-remove-duplicates-from-sorted-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/crawler-log-folder/)
