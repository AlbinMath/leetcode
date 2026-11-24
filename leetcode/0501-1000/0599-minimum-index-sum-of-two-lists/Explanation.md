# LeetCode 599: Minimum Index Sum of Two Lists

**LeetCode Problem #599 — Minimum Index Sum of Two Lists**
Solve LeetCode Minimum Index Sum of Two Lists using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Index Sum of Two Lists |
| LeetCode | #599 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given two arrays of strings `list1` and `list2`, find the **common strings with the least index sum**.

A **common string** is a string that appeared in both `list1` and `list2`.

A **common string with the least index sum** is a common string such that if it appeared at `list1[i]` and `list2[j]` then `i + j` should be the minimum value among all the other **common strings**.

Return *all the **common strings with the least index sum***. Return the answer in **any order**.

## Constraints
- `1 <= list1.length, list2.length <= 1000`
- `1 <= list1[i].length, list2[i].length <= 30`
- `list1[i]` and `list2[i]` consist of spaces `' '` and English letters.
- All the strings of `list1` are **unique**.
- All the strings of `list2` are **unique**.
- There is at least a common string between `list1` and `list2`.

## Examples
### Example 1
- **Input:** `list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]`
- **Output:** `["Shogun"]`
- **Explanation:** The only common string is "Shogun".

### Example 2
- **Input:** `list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]`
- **Output:** `["Shogun"]`
- **Explanation:** The common string with the least index sum is "Shogun" with index sum = (0 + 1) = 1.

### Example 3
- **Input:** `list1 = ["happy","sad","good"], list2 = ["sad","happy","good"]`
- **Output:** `["sad","happy"]`
- **Explanation:** There are three common strings:
"happy" with index sum = (0 + 1) = 1.
"sad" with index sum = (1 + 0) = 1.
"good" with index sum = (2 + 2) = 4.
The strings with the least index sum are "sad" and "happy".

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Minimum Index Sum of Two Lists**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `["Shogun"]`.
4. **Verification:** The only common string is "Shogun".

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
class Solution:
    def findRestaurant(self, list1, list2):
        index_map = {}

        for i in range(len(list1)):
            index_map[list1[i]] = i

        result = []
        min_sum = float('inf')

        for j in range(len(list2)):
            if list2[j] in index_map:
                current_sum = index_map[list2[j]] + j

                if current_sum < min_sum:
                    min_sum = current_sum
                    result = [list2[j]]

                elif current_sum == min_sum:
                    result.append(list2[j])

        return result
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
- [712. Minimum ASCII Delete Sum for Two Strings](../../0501-1000/0712-minimum-ascii-delete-sum-for-two-strings/)
- [1879. Minimum XOR Sum of Two Arrays](../../1501-2000/1879-minimum-xor-sum-of-two-arrays/)
- [3550. Smallest Index With Digit Sum Equal to Index](../../3501-4000/3550-smallest-index-with-digit-sum-equal-to-index/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-index-sum-of-two-lists/)
