# LeetCode 496: Next Greater Element I

**LeetCode Problem #496 — Next Greater Element I**
Solve LeetCode Next Greater Element I using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Next Greater Element I |
| LeetCode | #496 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
The **next greater element** of some element `x` in an array is the **first greater** element that is **to the right** of `x` in the same array.

You are given two **distinct 0-indexed** integer arrays `nums1` and `nums2`, where `nums1` is a subset of `nums2`.

For each `0 <= i < nums1.length`, find the index `j` such that `nums1[i] == nums2[j]` and determine the **next greater element** of `nums2[j]` in `nums2`. If there is no next greater element, then the answer for this query is `-1`.

Return *an array *`ans`* of length *`nums1.length`* such that *`ans[i]`* is the **next greater element** as described above.*

## Constraints
- `1 <= nums1.length <= nums2.length <= 1000`
- `0 <= nums1[i], nums2[i] <= 10^4`
- All integers in `nums1` and `nums2` are **unique**.
- All the integers of `nums1` also appear in `nums2`.

## Examples
### Example 1
- **Input:** `nums1 = [4,1,2], nums2 = [1,3,4,2]`
- **Output:** `[-1,3,-1]`
- **Explanation:** The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3, 4 ,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [ 1 ,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4, 2 ]. There is no next greater element, so the answer is -1.

### Example 2
- **Input:** `nums1 = [2,4], nums2 = [1,2,3,4]`
- **Output:** `[3,-1]`
- **Explanation:** The next greater element for each value of nums1 is as follows:
- 2 is underlined in nums2 = [1, 2 ,3,4]. The next greater element is 3.
- 4 is underlined in nums2 = [1,2,3, 4 ]. There is no next greater element, so the answer is -1.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Next Greater Element I**, we observe the problem requirements and utilize the **Monotonic Stack** technique. By maintaining a **Stack**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Stack** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums1 = [4,1,2], nums2 = [1,3,4,2]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[-1,3,-1]`.
4. **Verification:** The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3, 4 ,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [ 1 ,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4, 2 ]. There is no next greater element, so the answer is -1.

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
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        next_greater = {}

        for num in nums2:
            while stack and num > stack[-1]:
                smaller = stack.pop()
                next_greater[smaller] = num

            stack.append(num)

        # Elements remaining in the stack have no greater element
        while stack:
            next_greater[stack.pop()] = -1

        return [next_greater[num] for num in nums1]
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
- [503. Next Greater Element II](../../0501-1000/0503-next-greater-element-ii/)
- [556. Next Greater Element III](../../0501-1000/0556-next-greater-element-iii/)
- [2454. Next Greater Element IV](../../2001-2500/2454-next-greater-element-iv/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/next-greater-element-i/)
