# LeetCode 1357: Apply Discount Every n Orders

**LeetCode Problem #1357 — Apply Discount Every n Orders**
Solve LeetCode Apply Discount Every n Orders using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Apply Discount Every n Orders |
| LeetCode | #1357 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
There is a supermarket that is frequented by many customers. The products sold at the supermarket are represented as two parallel integer arrays `products` and `prices`, where the `i^th` product has an ID of `products[i]` and a price of `prices[i]`.

When a customer is paying, their bill is represented as two parallel integer arrays `product` and `amount`, where the `j^th` product they purchased has an ID of `product[j]`, and `amount[j]` is how much of the product they bought. Their subtotal is calculated as the sum of each `amount[j] * (price of the j^th product)`.

The supermarket decided to have a sale. Every `n^th` customer paying for their groceries will be given a **percentage discount**. The discount amount is given by `discount`, where they will be given `discount` percent off their subtotal. More formally, if their subtotal is `bill`, then they would actually pay `bill * ((100 - discount) / 100)`.

Implement the `Cashier` class:

`Cashier(int n, int discount, int[] products, int[] prices)` Initializes the object with `n`, the `discount`, and the `products` and their `prices`. 
 `double getBill(int[] product, int[] amount)` Returns the final total of the bill with the discount applied (if any). Answers within `10^-5` of the actual value will be accepted.

## Constraints
- `1 <= n <= 10^4`
- `0 <= discount <= 100`
- `1 <= products.length <= 200`
- `prices.length == products.length`
- `1 <= products[i] <= 200`
- `1 <= prices[i] <= 1000`
- The elements in `products` are **unique**.
- `1 <= product.length <= products.length`
- `amount.length == product.length`
- `product[j]` exists in `products`.
- `1 <= amount[j] <= 1000`
- The elements of `product` are **unique**.
- At most `1000` calls will be made to `getBill`.
- Answers within `10^-5` of the actual value will be accepted.

## Examples
### Example 1
- **Input:** `["Cashier","getBill","getBill","getBill","getBill","getBill","getBill","getBill"]
[[3,50,[1,2,3,4,5,6,7],[100,200,300,400,300,200,100]],[[1,2],[1,2]],[[3,7],[10,10]],[[1,2,3,4,5,6,7],[1,1,1,1,1,1,1]],[[4],[10]],[[7,3],[10,10]],[[7,5,3,1,6,4,2],[10,10,10,9,9,9,7]],[[2,3,5],[5,3,2]]]`
- **Output:** `[null,500.0,4000.0,800.0,4000.0,4000.0,7350.0,2500.0]`
- **Explanation:** Cashier cashier = new Cashier(3,50,[1,2,3,4,5,6,7],[100,200,300,400,300,200,100]);
cashier.getBill([1,2],[1,2]); // return 500.0. 1^st customer, no discount.
 // bill = 1 * 100 + 2 * 200 = 500.
cashier.getBill([3,7],[10,10]); // return 4000.0. 2^nd customer, no discount.
 // bill = 10 * 300 + 10 * 100 = 4000.
cashier.getBill([1,2,3,4,5,6,7],[1,1,1,1,1,1,1]); // return 800.0. 3^rd customer, 50% discount.
 // Original bill = 1600
 // Actual bill = 1600 * ((100 - 50) / 100) = 800.
cashier.getBill([4],[10]); // return 4000.0. 4^th customer, no discount.
cashier.getBill([7,3],[10,10]); // return 4000.0. 5^th customer, no discount.
cashier.getBill([7,5,3,1,6,4,2],[10,10,10,9,9,9,7]); // return 7350.0. 6^th customer, 50% discount.
 // Original bill = 14700, but with
 // Actual bill = 14700 * ((100 - 50) / 100) = 7350.
cashier.getBill([2,3,5],[5,3,2]); // return 2500.0. 7^th customer, no discount.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Apply Discount Every n Orders**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `["Cashier","getBill","getBill","getBill","getBill","getBill","getBill","getBill"]
[[3,50,[1,2,3,4,5,6,7],[100,200,300,400,300,200,100]],[[1,2],[1,2]],[[3,7],[10,10]],[[1,2,3,4,5,6,7],[1,1,1,1,1,1,1]],[[4],[10]],[[7,3],[10,10]],[[7,5,3,1,6,4,2],[10,10,10,9,9,9,7]],[[2,3,5],[5,3,2]]]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[null,500.0,4000.0,800.0,4000.0,4000.0,7350.0,2500.0]`.
4. **Verification:** Cashier cashier = new Cashier(3,50,[1,2,3,4,5,6,7],[100,200,300,400,300,200,100]);
cashier.getBill([1,2],[1,2]); // return 500.0. 1^st customer, no discount.
 // bill = 1 * 100 + 2 * 200 = 500.
cashier.getBill([3,7],[10,10]); // return 4000.0. 2^nd customer, no discount.
 // bill = 10 * 300 + 10 * 100 = 4000.
cashier.getBill([1,2,3,4,5,6,7],[1,1,1,1,1,1,1]); // return 800.0. 3^rd customer, 50% discount.
 // Original bill = 1600
 // Actual bill = 1600 * ((100 - 50) / 100) = 800.
cashier.getBill([4],[10]); // return 4000.0. 4^th customer, no discount.
cashier.getBill([7,3],[10,10]); // return 4000.0. 5^th customer, no discount.
cashier.getBill([7,5,3,1,6,4,2],[10,10,10,9,9,9,7]); // return 7350.0. 6^th customer, 50% discount.
 // Original bill = 14700, but with
 // Actual bill = 14700 * ((100 - 50) / 100) = 7350.
cashier.getBill([2,3,5],[5,3,2]); // return 2500.0. 7^th customer, no discount.

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
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var Cashier = function(n, discount, products, prices) {
    this.n = n;
    this.discountFactor = (100 - discount) / 100;
    this.priceMap = new Map();
    this.customerCount = 0;
    
    for (let i = 0; i < products.length; i++) {
        this.priceMap.set(products[i], prices[i]);
    }
};
Cashier.prototype.getBill = function(product, amount) {
    this.customerCount++;
    
    let subtotal = 0;
    for (let i = 0; i < product.length; i++) {
        subtotal += this.priceMap.get(product[i]) * amount[i];
    }
    
    if (this.customerCount % this.n === 0) {
        return subtotal * this.discountFactor;
    }
    
    return subtotal;
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
- [2858. Minimum Edge Reversals So Every Node Is Reachable](../../2501-3000/2858-minimum-edge-reversals-so-every-node-is-reachable/)
- [3305. Count of Substrings Containing Every Vowel and K Consonants I](../../3001-3500/3305-count-of-substrings-containing-every-vowel-and-k-consonants-i/)
- [3306. Count of Substrings Containing Every Vowel and K Consonants II](../../3001-3500/3306-count-of-substrings-containing-every-vowel-and-k-consonants-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/apply-discount-every-n-orders/)
