# LeetCode 1748: Sum of Unique Elements

**LeetCode Problem #1748 — Sum of Unique Elements**
Solve LeetCode Sum of Unique Elements using C++ and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sum of Unique Elements |
| LeetCode | #1748 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums`. The unique elements of an array are the elements that appear **exactly once** in the array.

Return *the **sum** of all the unique elements of *`nums`.

## Constraints
- `1 <= nums.length <= 100`
- `1 <= nums[i] <= 100`

## Examples
### Example 1
- **Input:** `nums = [1,2,3,2]`
- **Output:** `4`
- **Explanation:** The unique elements are [1,3], and the sum is 4.

### Example 2
- **Input:** `nums = [1,1,1,1,1]`
- **Output:** `0`
- **Explanation:** There are no unique elements, and the sum is 0.

### Example 3
- **Input:** `nums = [1,2,3,4,5]`
- **Output:** `15`
- **Explanation:** The unique elements are [1,2,3,4,5], and the sum is 15.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Sum of Unique Elements**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3,2]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** The unique elements are [1,3], and the sum is 4.

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
C++

## Source Code
- [solution.cpp](./solution.cpp)


```cpp
class Solution {
public:
    int sumOfUnique(vector<int>& nums) {
        int freq[101] = {0};

        // Count the frequency of each number
        for (int num : nums) {
            freq[num]++;
        }

        int sum = 0;

        // Add elements that appear exactly once
        for (int num : nums) {
            if (freq[num] == 1) {
                sum += num;
            }
        }

        return sum;
    }
};
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
- [2841. Maximum Sum of Almost Unique Subarray](../../2501-3000/2841-maximum-sum-of-almost-unique-subarray/)
- [2778. Sum of Squares of Special Elements ](../../2501-3000/2778-sum-of-squares-of-special-elements/)
- [3165. Maximum Sum of Subsequence With Non-adjacent Elements](../../3001-3500/3165-maximum-sum-of-subsequence-with-non-adjacent-elements/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sum-of-unique-elements/)
