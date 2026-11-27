# LeetCode 3606: Coupon Code Validator

**LeetCode Problem #3606 — Coupon Code Validator**
Solve LeetCode Coupon Code Validator using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Coupon Code Validator |
| LeetCode | #3606 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given three arrays of length `n` that describe the properties of `n` coupons: `code`, `businessLine`, and `isActive`. The `i^th `coupon has:

`code[i]`: a **string** representing the coupon identifier. 
 `businessLine[i]`: a **string** denoting the business category of the coupon. 
 `isActive[i]`: a **boolean** indicating whether the coupon is currently active.

A coupon is considered **valid** if all of the following conditions hold:

`code[i]` is non-empty and consists only of alphanumeric characters (a-z, A-Z, 0-9) and underscores (`_`). 
 `businessLine[i]` is one of the following four categories: `"electronics"`, `"grocery"`, `"pharmacy"`, `"restaurant"`. 
 `isActive[i]` is **true**.

Return an array of the **codes** of all valid coupons, **sorted** first by their **businessLine** in the order: `"electronics"`, `"grocery"`, `"pharmacy", "restaurant"`, and then by **code** in lexicographical (ascending) order within each category.

## Constraints
- `n == code.length == businessLine.length == isActive.length`
- `1 <= n <= 100`
- `0 <= code[i].length, businessLine[i].length <= 100`
- `code[i]` and `businessLine[i]` consist of printable ASCII characters.
- `isActive[i]` is either `true` or `false`.

## Examples
### Example 1
- **Input:** `code = ["SAVE20","","PHARMA5","SAVE@20"], businessLine = ["restaurant","grocery","pharmacy","restaurant"], isActive = [true,true,true,true]`
- **Output:** `["PHARMA5","SAVE20"]`
- **Explanation:** First coupon is valid. 
 Second coupon has empty code (invalid). 
 Third coupon is valid. 
 Fourth coupon has special character `@` (invalid).

### Example 2
- **Input:** `code = ["GROCERY15","ELECTRONICS_50","DISCOUNT10"], businessLine = ["grocery","electronics","invalid"], isActive = [false,true,true]`
- **Output:** `["ELECTRONICS_50"]`
- **Explanation:** First coupon is inactive (invalid). 
 Second coupon is valid. 
 Third coupon has invalid business line (invalid).

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Coupon Code Validator**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `code = ["SAVE20","","PHARMA5","SAVE@20"], businessLine = ["restaurant","grocery","pharmacy","restaurant"], isActive = [true,true,true,true]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `["PHARMA5","SAVE20"]`.
4. **Verification:** First coupon is valid. 
 Second coupon has empty code (invalid). 
 Third coupon is valid. 
 Fourth coupon has special character `@` (invalid).

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var validateCoupons = function(code, businessLine, isActive) {
    const priority = {
        electronics: 0,
        grocery: 1,
        pharmacy: 2,
        restaurant: 3
    };
    const validCoupons = [];
    for (let i = 0; i < code.length; i++) {
        if (
            code[i].length > 0 &&
            /^[a-zA-Z0-9_]+$/.test(code[i]) &&
            priority[businessLine[i]] !== undefined &&
            isActive[i] === true
        ) {
            validCoupons.push([
                businessLine[i],
                code[i]
            ]);
        }
    }
    validCoupons.sort((a, b) => {
        if (priority[a[0]] !== priority[b[0]]) {
            return priority[a[0]] - priority[b[0]];
        }
        if (a[1] < b[1]) return -1;
        if (a[1] > b[1]) return 1;

        return 0;
    });
    return validCoupons.map(coupon => coupon[1]);
};
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
- [89. Gray Code](../../0001-0500/0089-gray-code/)
- [804. Unique Morse Code Words](../../0501-1000/0804-unique-morse-code-words/)
- [591. Tag Validator](../../0501-1000/0591-tag-validator/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/coupon-code-validator/)
