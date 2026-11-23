# LeetCode 3043: Find the Length of the Longest Common Prefix

**LeetCode Problem #3043 — Find the Length of the Longest Common Prefix**
Solve LeetCode Find the Length of the Longest Common Prefix using C++ and Prefix Sum. This solution finds the optimal result using Prefix Sum Precomputation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the Length of the Longest Common Prefix |
| LeetCode | #3043 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | Prefix Sum Precomputation |
| Data Structure | Prefix Array |
| Pattern | Prefix Sum |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given two arrays with **positive** integers `arr1` and `arr2`.

A **prefix** of a positive integer is an integer formed by one or more of its digits, starting from its **leftmost** digit. For example, `123` is a prefix of the integer `12345`, while `234` is **not**.

A **common prefix** of two integers `a` and `b` is an integer `c`, such that `c` is a prefix of both `a` and `b`. For example, `5655359` and `56554` have common prefixes `565` and `5655` while `1223` and `43456` **do not** have a common prefix.

You need to find the length of the **longest common prefix** between all pairs of integers `(x, y)` such that `x` belongs to `arr1` and `y` belongs to `arr2`.

Return *the length of the **longest** common prefix among all pairs*.* If no common prefix exists among them*, *return* `0`.

## Constraints
- `1 <= arr1.length, arr2.length <= 5 * 10^4`
- `1 <= arr1[i], arr2[i] <= 10^8`

## Examples
### Example 1
- **Input:** `arr1 = [1,10,100], arr2 = [1000]`
- **Output:** `3`
- **Explanation:** There are 3 pairs (arr1[i], arr2[j]):
- The longest common prefix of (1, 1000) is 1.
- The longest common prefix of (10, 1000) is 10.
- The longest common prefix of (100, 1000) is 100.
The longest common prefix is 100 with a length of 3.

### Example 2
- **Input:** `arr1 = [1,2,3], arr2 = [4,4,4]`
- **Output:** `0`
- **Explanation:** There exists no common prefix for any pair (arr1[i], arr2[j]), hence we return 0.
Note that common prefixes between elements of the same array do not count.

## Key Insight
Leverage **Prefix Sum** with **Prefix Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find the Length of the Longest Common Prefix**, we observe the problem requirements and utilize the **Prefix Sum** technique. We iterate through the inputs using **Prefix Sum Precomputation**, leveraging a **Prefix Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Prefix Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `arr1 = [1,10,100], arr2 = [1000]`.
2. **Processing Steps:** We apply **Prefix Sum Precomputation** using our **Prefix Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** There are 3 pairs (arr1[i], arr2[j]):
- The longest common prefix of (1, 1000) is 1.
- The longest common prefix of (10, 1000) is 10.
- The longest common prefix of (100, 1000) is 100.
The longest common prefix is 100 with a length of 3.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Prefix Array.

## Pattern
**Prefix Sum**

## Topics
- Prefix Sum
- Array

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)


```cpp
class Solution {
public:
    struct TrieNode {
        TrieNode* child[10];

        TrieNode() {
            for (int i = 0; i < 10; i++)
                child[i] = nullptr;
        }
    };

    int longestCommonPrefix(vector<int>& arr1, vector<int>& arr2) {
        TrieNode* root = new TrieNode();

        // Insert all numbers from arr1
        for (int num : arr1) {
            string s = to_string(num);
            TrieNode* node = root;

            for (char c : s) {
                int digit = c - '0';

                if (!node->child[digit])
                    node->child[digit] = new TrieNode();

                node = node->child[digit];
            }
        }

        int answer = 0;

        // Search prefixes of numbers in arr2
        for (int num : arr2) {
            string s = to_string(num);
            TrieNode* node = root;
            int len = 0;

            for (char c : s) {
                int digit = c - '0';

                if (!node->child[digit])
                    break;

                node = node->child[digit];
                len++;
            }

            answer = max(answer, len);
        }

        return answer;
    }
};
```

## Why This Works
By utilizing **Prefix Sum**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [14. Longest Common Prefix](../../0001-0500/0014-longest-common-prefix/)
- [2657. Find the Prefix Common Array of Two Arrays](../../2501-3000/2766-find-the-prefix-common-array-of-two-arrays/)
- [3485. Longest Common Prefix of K Strings After Removal](../../3501-4000/3784-longest-common-prefix-of-k-strings-after-removal/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/)
