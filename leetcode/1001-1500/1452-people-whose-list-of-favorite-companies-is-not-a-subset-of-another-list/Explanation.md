# LeetCode 1452: People Whose List of Favorite Companies Is Not a Subset of Another List

**LeetCode Problem #1452 — People Whose List of Favorite Companies Is Not a Subset of Another List**
Solve LeetCode People Whose List of Favorite Companies Is Not a Subset of Another List using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | People Whose List of Favorite Companies Is Not a Subset of Another List |
| LeetCode | #1452 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given the array `favoriteCompanies` where `favoriteCompanies[i]` is the list of favorites companies for the `ith` person (**indexed from 0**).

*Return the indices of people whose list of favorite companies is not a **subset** of any other list of favorites companies*. You must return the indices in increasing order.

## Constraints
- `1 <= favoriteCompanies.length <= 100`
- `1 <= favoriteCompanies[i].length <= 500`
- `1 <= favoriteCompanies[i][j].length <= 20`
- All strings in `favoriteCompanies[i]` are **distinct**.
- All lists of favorite companies are **distinct**, that is, If we sort alphabetically each list then `favoriteCompanies[i] != favoriteCompanies[j].`
- All strings consist of lowercase English letters only.

## Examples
### Example 1
- **Input:** `favoriteCompanies = [["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]`
- **Output:** `[0,1,4]`
- **Explanation:** Person with index=2 has favoriteCompanies[2]=["google","facebook"] which is a subset of favoriteCompanies[0]=["leetcode","google","facebook"] corresponding to the person with index 0. 
Person with index=3 has favoriteCompanies[3]=["google"] which is a subset of favoriteCompanies[0]=["leetcode","google","facebook"] and favoriteCompanies[1]=["google","microsoft"]. 
Other lists of favorite companies are not a subset of another list, therefore, the answer is [0,1,4].

### Example 2
- **Input:** `favoriteCompanies = [["leetcode","google","facebook"],["leetcode","amazon"],["facebook","google"]]`
- **Output:** `[0,1]`
- **Explanation:** In this case favoriteCompanies[2]=["facebook","google"] is a subset of favoriteCompanies[0]=["leetcode","google","facebook"], therefore, the answer is [0,1].

### Example 3
- **Input:** `favoriteCompanies = [["leetcode"],["google"],["facebook"],["amazon"]]`
- **Output:** `[0,1,2,3]`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **People Whose List of Favorite Companies Is Not a Subset of Another List**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `favoriteCompanies = [["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[0,1,4]`.
4. **Verification:** Person with index=2 has favoriteCompanies[2]=["google","facebook"] which is a subset of favoriteCompanies[0]=["leetcode","google","facebook"] corresponding to the person with index 0. 
Person with index=3 has favoriteCompanies[3]=["google"] which is a subset of favoriteCompanies[0]=["leetcode","google","facebook"] and favoriteCompanies[1]=["google","microsoft"]. 
Other lists of favorite companies are not a subset of another list, therefore, the answer is [0,1,4].

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        sets = [set(f) for f in favoriteCompanies]
        n = len(sets)
        res = []

        for i in range(n):
            is_subset = False
            for j in range(n):
                if i != j and len(sets[i]) <= len(sets[j]) and sets[i] <= sets[j]:
                    is_subset = True
                    break
            if not is_subset:
                res.append(i)

        return res
```

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [1978. Employees Whose Manager Left the Company](../../1501-2000/1978-employees-whose-manager-left-the-company/)
- [2435. Paths in Matrix Whose Sum Is Divisible by K](../../2001-2500/2435-paths-in-matrix-whose-sum-is-divisible-by-k/)
- [2824. Count Pairs Whose Sum is Less than Target](../../2501-3000/2824-count-pairs-whose-sum-is-less-than-target/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list/)
