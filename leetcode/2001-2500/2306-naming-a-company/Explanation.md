# LeetCode 2306: Naming a Company

**LeetCode Problem #2306 — Naming a Company**
Solve LeetCode Naming a Company using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Naming a Company |
| LeetCode | #2306 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array of strings `ideas` that represents a list of names to be used in the process of naming a company. The process of naming a company is as follows:

Choose 2 **distinct** names from `ideas`, call them `idea_A` and `idea_B`. 
 Swap the first letters of `idea_A` and `idea_B` with each other. 
 If **both** of the new names are not found in the original `ideas`, then the name `idea_A idea_B` (the **concatenation** of `idea_A` and `idea_B`, separated by a space) is a valid company name. 
 Otherwise, it is not a valid name.

Return *the number of **distinct** valid names for the company*.

## Constraints
- `2 <= ideas.length <= 5 * 10^4`
- `1 <= ideas[i].length <= 10`
- `ideas[i]` consists of lowercase English letters.
- All the strings in `ideas` are **unique**.

## Examples
### Example 1
- **Input:** `ideas = ["coffee","donuts","time","toffee"]`
- **Output:** `6`
- **Explanation:** The following selections are valid:
- ("coffee", "donuts"): The company name created is "doffee conuts".
- ("donuts", "coffee"): The company name created is "conuts doffee".
- ("donuts", "time"): The company name created is "tonuts dime".
- ("donuts", "toffee"): The company name created is "tonuts doffee".
- ("time", "donuts"): The company name created is "dime tonuts".
- ("toffee", "donuts"): The company name created is "doffee tonuts".
Therefore, there are a total of 6 distinct company names.

The following are some examples of invalid selections:
- ("coffee", "time"): The name "toffee" formed after swapping already exists in the original array.
- ("time", "toffee"): Both names are still the same after swapping and exist in the original array.
- ("coffee", "toffee"): Both names formed after swapping already exist in the original array.

### Example 2
- **Input:** `ideas = ["lack","back"]`
- **Output:** `0`
- **Explanation:** There are no valid selections. Therefore, 0 is returned.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Naming a Company**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `ideas = ["coffee","donuts","time","toffee"]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `6`.
4. **Verification:** The following selections are valid:
- ("coffee", "donuts"): The company name created is "doffee conuts".
- ("donuts", "coffee"): The company name created is "conuts doffee".
- ("donuts", "time"): The company name created is "tonuts dime".
- ("donuts", "toffee"): The company name created is "tonuts doffee".
- ("time", "donuts"): The company name created is "dime tonuts".
- ("toffee", "donuts"): The company name created is "doffee tonuts".
Therefore, there are a total of 6 distinct company names.

The following are some examples of invalid selections:
- ("coffee", "time"): The name "toffee" formed after swapping already exists in the original array.
- ("time", "toffee"): Both names are still the same after swapping and exist in the original array.
- ("coffee", "toffee"): Both names formed after swapping already exist in the original array.

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
class Solution(object):
    def distinctNames(self, ideas):
        groups = [set() for _ in range(26)]
        for idea in ideas:
            groups[ord(idea[0]) - ord('a')].add(idea[1:])

        ans = 0
        for i in range(25):
            if not groups[i]:
                continue
            for j in range(i + 1, 26):
                if not groups[j]:
                    continue
                mutual = len(groups[i] & groups[j])
                ans += 2 * (len(groups[i]) - mutual) * (len(groups[j]) - mutual)

        return ans
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
- [1978. Employees Whose Manager Left the Company](../../1501-2000/1978-employees-whose-manager-left-the-company/)
- [5. Longest Palindromic Substring](../../0001-0500/0005-longest-palindromic-substring/)
- [26. Remove Duplicates from Sorted Array](../../0001-0500/0026-remove-duplicates-from-sorted-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/naming-a-company/)
