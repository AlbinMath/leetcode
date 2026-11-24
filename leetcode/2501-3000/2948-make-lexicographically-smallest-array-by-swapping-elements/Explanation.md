# LeetCode 2948: Make Lexicographically Smallest Array by Swapping Elements

**LeetCode Problem #2948 — Make Lexicographically Smallest Array by Swapping Elements**
Solve LeetCode Make Lexicographically Smallest Array by Swapping Elements using C++ and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Make Lexicographically Smallest Array by Swapping Elements |
| LeetCode | #2948 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a **0-indexed** array of **positive** integers `nums` and a **positive** integer `limit`.

In one operation, you can choose any two indices `i` and `j` and swap `nums[i]` and `nums[j]` **if** `|nums[i] - nums[j]| <= limit`.

Return *the **lexicographically smallest array** that can be obtained by performing the operation any number of times*.

An array `a` is lexicographically smaller than an array `b` if in the first position where `a` and `b` differ, array `a` has an element that is less than the corresponding element in `b`. For example, the array `[2,10,3]` is lexicographically smaller than the array `[10,2,3]` because they differ at index `0` and `2 < 10`.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`
- `1 <= limit <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [1,5,3,9,8], limit = 2`
- **Output:** `[1,3,5,8,9]`
- **Explanation:** Apply the operation 2 times:
- Swap nums[1] with nums[2]. The array becomes [1,3,5,9,8]
- Swap nums[3] with nums[4]. The array becomes [1,3,5,8,9]
We cannot obtain a lexicographically smaller array by applying any more operations.
Note that it may be possible to get the same result by doing different operations.

### Example 2
- **Input:** `nums = [1,7,6,18,2,1], limit = 3`
- **Output:** `[1,6,7,18,1,2]`
- **Explanation:** Apply the operation 3 times:
- Swap nums[1] with nums[2]. The array becomes [1,6,7,18,2,1]
- Swap nums[0] with nums[4]. The array becomes [2,6,7,18,1,1]
- Swap nums[0] with nums[5]. The array becomes [1,6,7,18,1,2]
We cannot obtain a lexicographically smaller array by applying any more operations.

### Example 3
- **Input:** `nums = [1,7,28,19,10], limit = 3`
- **Output:** `[1,7,28,19,10]`
- **Explanation:** [1,7,28,19,10] is the lexicographically smallest array we can obtain because we cannot apply the operation on any two indices.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Make Lexicographically Smallest Array by Swapping Elements**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,5,3,9,8], limit = 2`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,3,5,8,9]`.
4. **Verification:** Apply the operation 2 times:
- Swap nums[1] with nums[2]. The array becomes [1,3,5,9,8]
- Swap nums[3] with nums[4]. The array becomes [1,3,5,8,9]
We cannot obtain a lexicographically smaller array by applying any more operations.
Note that it may be possible to get the same result by doing different operations.

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
    vector<int> lexicographicallySmallestArray(vector<int>& nums, int limit) {
        int n = nums.size();

        // Store {value, original index}
        vector<pair<int, int>> arr;

        for (int i = 0; i < n; i++) {
            arr.push_back({nums[i], i});
        }

        // Sort by value
        sort(arr.begin(), arr.end());

        vector<int> ans(n);

        int i = 0;

        while (i < n) {
            int j = i;

            // Find the connected group
            while (j + 1 < n &&
                   arr[j + 1].first - arr[j].first <= limit) {
                j++;
            }

            // Get original indices of this group
            vector<int> indices;

            for (int k = i; k <= j; k++) {
                indices.push_back(arr[k].second);
            }

            // Sort original indices
            sort(indices.begin(), indices.end());

            // Values are already sorted
            // Assign smallest values to smallest indices
            for (int k = 0; k < (int)indices.size(); k++) {
                ans[indices[k]] = arr[i + k].first;
            }

            i = j + 1;
        }

        return ans;
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
- [1887. Reduction Operations to Make the Array Elements Equal](../../1501-2000/1887-reduction-operations-to-make-the-array-elements-equal/)
- [2602. Minimum Operations to Make All Array Elements Equal](../../2501-3000/2602-minimum-operations-to-make-all-array-elements-equal/)
- [2654. Minimum Number of Operations to Make All Array Elements Equal to 1](../../2501-3000/2654-minimum-number-of-operations-to-make-all-array-elements-equal-to-1/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/)
