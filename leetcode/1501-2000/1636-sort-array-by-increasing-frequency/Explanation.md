# LeetCode 1636: Sort Array by Increasing Frequency

**LeetCode Problem #1636 — Sort Array by Increasing Frequency**
Solve LeetCode Sort Array by Increasing Frequency using C++ and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sort Array by Increasing Frequency |
| LeetCode | #1636 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given an array of integers `nums`, sort the array in **increasing** order based on the frequency of the values. If multiple values have the same frequency, sort them in **decreasing** order.

Return the *sorted array*.

## Constraints
- `1 <= nums.length <= 100`
- `-100 <= nums[i] <= 100`

## Examples
### Example 1
- **Input:** `nums = [1,1,2,2,2,3]`
- **Output:** `[3,1,1,2,2,2]`
- **Explanation:** '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.

### Example 2
- **Input:** `nums = [2,3,1,3,2]`
- **Output:** `[1,3,3,2,2]`
- **Explanation:** '2' and '3' both have a frequency of 2, so they are sorted in decreasing order.

### Example 3
- **Input:** `nums = [-1,1,-6,4,5,-6,1,4,1]`
- **Output:** `[5,-1,4,4,-6,-6,1,1,1]`

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Sort Array by Increasing Frequency**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,1,2,2,2,3]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[3,1,1,2,2,2]`.
4. **Verification:** '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.

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
    vector<int> frequencySort(vector<int>& nums) {
        unordered_map<int, int> freq;

        // Count the frequency of each number
        for (int num : nums) {
            freq[num]++;
        }

        // Sort by frequency, then by decreasing value
        sort(nums.begin(), nums.end(), [&](int a, int b) {
            if (freq[a] != freq[b]) {
                return freq[a] < freq[b];
            }
            return a > b;
        });

        return nums;
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
- [905. Sort Array By Parity](../../0501-1000/0905-sort-array-by-parity/)
- [912. Sort an Array](../../0501-1000/0912-sort-an-array/)
- [922. Sort Array By Parity II](../../0501-1000/0922-sort-array-by-parity-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sort-array-by-increasing-frequency/)
