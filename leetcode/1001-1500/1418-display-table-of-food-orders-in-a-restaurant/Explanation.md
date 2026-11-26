# LeetCode 1418: Display Table of Food Orders in a Restaurant

**LeetCode Problem #1418 — Display Table of Food Orders in a Restaurant**
Solve LeetCode Display Table of Food Orders in a Restaurant using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Display Table of Food Orders in a Restaurant |
| LeetCode | #1418 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given the array `orders`, which represents the orders that customers have done in a restaurant. More specifically `orders[i]=[customerName_i,tableNumber_i,foodItem_i]` where `customerName_i` is the name of the customer, `tableNumber_i` is the table customer sit at, and `foodItem_i` is the item customer orders.

*Return the restaurant's &ldquo;**display table**&rdquo;*. The &ldquo;**display table**&rdquo; is a table whose row entries denote how many of each food item each table ordered. The first column is the table number and the remaining columns correspond to each food item in alphabetical order. The first row should be a header whose first column is &ldquo;Table&rdquo;, followed by the names of the food items. Note that the customer names are not part of the table. Additionally, the rows should be sorted in numerically increasing order.

## Constraints
- `1 <= orders.length <= 5 * 10^4`
- `orders[i].length == 3`
- `1 <= customerName_i.length, foodItem_i.length <= 20`
- `customerName_i` and `foodItem_i` consist of lowercase and uppercase English letters and the space character.
- `tableNumber_i `is a valid integer between `1` and `500`.

## Examples
### Example 1
- **Input:** `orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]`
- **Output:** `[["Table","Beef Burrito","Ceviche","Fried Chicken","Water"],["3","0","2","1","0"],["5","0","1","0","1"],["10","1","0","0","0"]]`
- **Explanation:** The displaying table looks like:

### Example 2
- **Input:** `orders = [["James","12","Fried Chicken"],["Ratesh","12","Fried Chicken"],["Amadeus","12","Fried Chicken"],["Adam","1","Canadian Waffles"],["Brianna","1","Canadian Waffles"]]`
- **Output:** `[["Table","Canadian Waffles","Fried Chicken"],["1","2","0"],["12","0","3"]]`
- **Explanation:** For the table 1: Adam and Brianna order "Canadian Waffles".
For the table 12: James, Ratesh and Amadeus order "Fried Chicken".

### Example 3
- **Input:** `orders = [["Laura","2","Bean Burrito"],["Jhon","2","Beef Burrito"],["Melissa","2","Soda"]]`
- **Output:** `[["Table","Bean Burrito","Beef Burrito","Soda"],["2","1","1","1"]]`

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Display Table of Food Orders in a Restaurant**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[["Table","Beef Burrito","Ceviche","Fried Chicken","Water"],["3","0","2","1","0"],["5","0","1","0","1"],["10","1","0","0","0"]]`.
4. **Verification:** The displaying table looks like:

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
from collections import Counter, defaultdict

class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        foods = set()
        tables = defaultdict(Counter)

        for _, table, food in orders:
            foods.add(food)
            tables[int(table)][food] += 1

        menu = sorted(foods)
        res = [["Table"] + menu]

        for t in sorted(tables):
            res.append([str(t)] + [str(tables[t][f]) for f in menu])

        return res
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
- [1321. Restaurant Growth](../../1001-1500/1321-restaurant-growth/)
- [1174. Immediate Food Delivery II](../../1001-1500/1174-immediate-food-delivery-ii/)
- [2353. Design a Food Rating System](../../2001-2500/2353-design-a-food-rating-system/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/display-table-of-food-orders-in-a-restaurant/)
