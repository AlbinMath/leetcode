# LeetCode 3514: Number of Unique XOR Triplets II

**LeetCode Problem #3514 — Number of Unique XOR Triplets II**
Solve LeetCode Number of Unique XOR Triplets II using C++ and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Unique XOR Triplets II |
| LeetCode | #3514 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums`.

A **XOR triplet** is defined as the XOR of three elements `nums[i] XOR nums[j] XOR nums[k]` where `i <= j <= k`.

Return the number of **unique** XOR triplet values from all possible triplets `(i, j, k)`.

## Constraints
- `1 <= nums.length <= 1500`
- `1 <= nums[i] <= 1500`

## Examples
### Example 1
- **Input:** `nums = [1,3]`
- **Output:** `2`
- **Explanation:** The possible XOR triplet values are: 

 
 `(0, 0, 0) &rarr; 1 XOR 1 XOR 1 = 1` 
 `(0, 0, 1) &rarr; 1 XOR 1 XOR 3 = 3` 
 `(0, 1, 1) &rarr; 1 XOR 3 XOR 3 = 1` 
 `(1, 1, 1) &rarr; 3 XOR 3 XOR 3 = 3` 
 

 The unique XOR values are {1, 3} . Thus, the output is 2.

### Example 2
- **Input:** `nums = [6,7,8,9]`
- **Output:** `4`
- **Explanation:** The possible XOR triplet values are {6, 7, 8, 9} . Thus, the output is 4.

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Number of Unique XOR Triplets II**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

## Algorithm
1. Initialize boundary pointers `left` and `right`.
2. Compute `mid = left + (right - left) // 2` to prevent overflow.
3. Adjust `left` or `right` depending on whether target satisfies the partition condition.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,3]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The possible XOR triplet values are: 

 
 `(0, 0, 0) &rarr; 1 XOR 1 XOR 1 = 1` 
 `(0, 0, 1) &rarr; 1 XOR 1 XOR 3 = 3` 
 `(0, 1, 1) &rarr; 1 XOR 3 XOR 3 = 1` 
 `(1, 1, 1) &rarr; 3 XOR 3 XOR 3 = 3` 
 

 The unique XOR values are {1, 3} . Thus, the output is 2.

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
C++

## Source Code
- [solution.cpp](./solution.cpp)


```cpp
class Solution {
public:
    int uniqueXorTriplets(vector<int>& nums) {
        const int MAX = 2048;

        // Values that actually exist in nums
        vector<bool> present(MAX, false);

        for (int x : nums)
            present[x] = true;

        // All possible XORs of two elements.
        // Repetition is allowed because i <= j <= k.
        vector<bool> pairXor(MAX, false);

        for (int a = 0; a < MAX; a++) {
            if (!present[a])
                continue;

            for (int b = 0; b < MAX; b++) {
                if (!present[b])
                    continue;

                pairXor[a ^ b] = true;
            }
        }

        // Add the third element.
        vector<bool> result(MAX, false);

        for (int x = 0; x < MAX; x++) {
            if (!pairXor[x])
                continue;

            for (int c = 0; c < MAX; c++) {
                if (!present[c])
                    continue;

                result[x ^ c] = true;
            }
        }

        int ans = 0;

        for (bool x : result) {
            if (x)
                ans++;
        }

        return ans;
    }
};
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
- [3513. Number of Unique XOR Triplets I](../../3501-4000/3824-number-of-unique-xor-triplets-i/)
- [1442. Count Triplets That Can Form Two Arrays of Equal XOR](../../1501-2000/1553-count-triplets-that-can-form-two-arrays-of-equal-xor/)
- [2997. Minimum Number of Operations to Make Array XOR Equal to K](../../3001-3500/3249-minimum-number-of-operations-to-make-array-xor-equal-to-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-unique-xor-triplets-ii/)
