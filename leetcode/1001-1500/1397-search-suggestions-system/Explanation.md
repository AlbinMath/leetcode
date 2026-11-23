# LeetCode 1268: Search Suggestions System

**LeetCode Problem #1268 — Search Suggestions System**
Solve LeetCode Search Suggestions System using JavaScript and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Search Suggestions System |
| LeetCode | #1268 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an array of strings `products` and a string `searchWord`.

Design a system that suggests at most three product names from `products` after each character of `searchWord` is typed. Suggested products should have common prefix with `searchWord`. If there are more than three products with a common prefix return the three lexicographically minimums products.

Return *a list of lists of the suggested products after each character of *`searchWord`* is typed*.

## Constraints
- `1 <= products.length <= 1000`
- `1 <= products[i].length <= 3000`
- `1 <= sum(products[i].length) <= 2 * 10^4`
- All the strings of `products` are **unique**.
- `products[i]` consists of lowercase English letters.
- `1 <= searchWord.length <= 1000`
- `searchWord` consists of lowercase English letters.

## Examples
### Example 1
- **Input:** `products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"`
- **Output:** `[["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]`
- **Explanation:** products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"].
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"].
After typing mou, mous and mouse the system suggests ["mouse","mousepad"].

### Example 2
- **Input:** `products = ["havana"], searchWord = "havana"`
- **Output:** `[["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]`
- **Explanation:** The only word "havana" will be always suggested while typing the search word.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Search Suggestions System**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]`.
4. **Verification:** products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"].
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"].
After typing mou, mous and mouse the system suggests ["mouse","mousepad"].

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for DP Table / Array.

## Pattern
**Dynamic Programming**

## Topics
- Dynamic Programming
- Memoization
- State Transition

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var suggestedProducts = function(products, searchWord) {
    products.sort();

    const result = [];
    let prefix = "";

    for (const char of searchWord) {
        prefix += char;

        const suggestions = [];

        for (const product of products) {
            if (product.startsWith(prefix)) {
                suggestions.push(product);
            }

            if (suggestions.length === 3) {
                break;
            }
        }

        result.push(suggestions);
    }

    return result;
};
```

## Why This Works
By utilizing **Dynamic Programming**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Incorrect base case initialization.
2. Flawed state transition equation.
3. Storing unnecessary state leading to Memory Limit Exceeded (MLE).

## Interview Notes
- **Tests:** Subproblem decomposition, state transition logic, and space optimization.
- **Follow-up:** Can space complexity be reduced from $O(n^2)$ to $O(n)$ or $O(1)$?

## Related Problems
- [609. Find Duplicate File in System](../../0501-1000/0609-find-duplicate-file-in-system/)
- [1396. Design Underground System](../../1501-2000/1512-design-underground-system/)
- [1603. Design Parking System](../../1501-2000/1708-design-parking-system/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/search-suggestions-system/)
