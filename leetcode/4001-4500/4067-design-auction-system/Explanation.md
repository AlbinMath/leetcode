# LeetCode 3815: Design Auction System

**LeetCode Problem #3815 — Design Auction System**
Solve LeetCode Design Auction System using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Design Auction System |
| LeetCode | #3815 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are asked to design an auction system that manages bids from multiple users in real time.

Each bid is associated with a `userId`, an `itemId`, and a `bidAmount`.

Implement the `AuctionSystem` class:​​​​​​​

`AuctionSystem()`: Initializes the `AuctionSystem` object. 
 `void addBid(int userId, int itemId, int bidAmount)`: Adds a new bid for `itemId` by `userId` with `bidAmount`. If the same `userId` **already** has a bid on `itemId`, **replace** it with the new `bidAmount`. 
 `void updateBid(int userId, int itemId, int newAmount)`: Updates the existing bid of `userId` for `itemId` to `newAmount`. It is **guaranteed** that this bid *exists*. 
 `void removeBid(int userId, int itemId)`: Removes the bid of `userId` for `itemId`. It is **guaranteed** that this bid *exists*. 
 `int getHighestBidder(int itemId)`: Returns the `userId` of the **highest** bidder for `itemId`. If multiple users have the **same highest** `bidAmount`, return the user with the **highest** `userId`. If no bids exist for the item, return -1.

## Constraints
- `1 <= userId, itemId <= 5 * 10^4`
- `1 <= bidAmount, newAmount <= 10^9`
- At most `5 * 10^4` total calls to `addBid`, `updateBid`, `removeBid`, and `getHighestBidder`.
- The input is generated such that for `updateBid` and `removeBid`, the bid from the given `userId` for the given `itemId` will be valid.

## Examples
### Example 1
- **Input:** `["AuctionSystem", "addBid", "addBid", "getHighestBidder", "updateBid", "getHighestBidder", "removeBid", "getHighestBidder", "getHighestBidder"] 
[[], [1, 7, 5], [2, 7, 6], [7], [1, 7, 8], [7], [2, 7], [7], [3]]`
- **Output:** `[null, null, null, 2, null, 1, null, 1, -1]`
- **Explanation:** AuctionSystem auctionSystem = new AuctionSystem(); // Initialize the Auction system 
auctionSystem.addBid(1, 7, 5); // User 1 bids 5 on item 7 
auctionSystem.addBid(2, 7, 6); // User 2 bids 6 on item 7 
auctionSystem.getHighestBidder(7); // return 2 as User 2 has the highest bid 
auctionSystem.updateBid(1, 7, 8); // User 1 updates bid to 8 on item 7 
auctionSystem.getHighestBidder(7); // return 1 as User 1 now has the highest bid 
auctionSystem.removeBid(2, 7); // Remove User 2's bid on item 7 
auctionSystem.getHighestBidder(7); // return 1 as User 1 is the current highest bidder 
auctionSystem.getHighestBidder(3); // return -1 as no bids exist for item 3

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Design Auction System**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `["AuctionSystem", "addBid", "addBid", "getHighestBidder", "updateBid", "getHighestBidder", "removeBid", "getHighestBidder", "getHighestBidder"] 
[[], [1, 7, 5], [2, 7, 6], [7], [1, 7, 8], [7], [2, 7], [7], [3]]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[null, null, null, 2, null, 1, null, 1, -1]`.
4. **Verification:** AuctionSystem auctionSystem = new AuctionSystem(); // Initialize the Auction system 
auctionSystem.addBid(1, 7, 5); // User 1 bids 5 on item 7 
auctionSystem.addBid(2, 7, 6); // User 2 bids 6 on item 7 
auctionSystem.getHighestBidder(7); // return 2 as User 2 has the highest bid 
auctionSystem.updateBid(1, 7, 8); // User 1 updates bid to 8 on item 7 
auctionSystem.getHighestBidder(7); // return 1 as User 1 now has the highest bid 
auctionSystem.removeBid(2, 7); // Remove User 2's bid on item 7 
auctionSystem.getHighestBidder(7); // return 1 as User 1 is the current highest bidder 
auctionSystem.getHighestBidder(3); // return -1 as no bids exist for item 3

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
class BidMaxHeap {
    constructor() {
        this.data = [];
    }
    size() {
        return this.data.length;
    }
    peek() {
        return this.data[0];
    }
    _higherPriority(a, b) {
        if (a[0] !== b[0]) return a[0] > b[0];
        return a[1] > b[1];
    }
    push(val) {
        this.data.push(val);
        let i = this.data.length - 1;
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (this._higherPriority(this.data[p], this.data[i])) break;
            [this.data[p], this.data[i]] = [this.data[i], this.data[p]];
            i = p;
        }
    }
    pop() {
        const top = this.data[0];
        const last = this.data.pop();
        if (this.data.length > 0) {
            this.data[0] = last;
            let i = 0;
            const n = this.data.length;
            while (true) {
                let best = i;
                const l = (i << 1) + 1;
                const r = (i << 1) + 2;
                if (l < n && this._higherPriority(this.data[l], this.data[best])) best = l;
                if (r < n && this._higherPriority(this.data[r], this.data[best])) best = r;
                if (best === i) break;
                [this.data[i], this.data[best]] = [this.data[best], this.data[i]];
                i = best;
            }
        }
        return top;
    }
}

var AuctionSystem = function() {
    this.bids = new Map();
    this.itemHeaps = new Map();
};
AuctionSystem.prototype.addBid = function(userId, itemId, bidAmount) {
    this.bids.set(`${itemId}:${userId}`, bidAmount);
    if (!this.itemHeaps.has(itemId)) {
        this.itemHeaps.set(itemId, new BidMaxHeap());
    }
    this.itemHeaps.get(itemId).push([bidAmount, userId]);
};
AuctionSystem.prototype.updateBid = function(userId, itemId, newAmount) {
    this.bids.set(`${itemId}:${userId}`, newAmount);
    this.itemHeaps.get(itemId).push([newAmount, userId]);
};
AuctionSystem.prototype.removeBid = function(userId, itemId) {
    this.bids.delete(`${itemId}:${userId}`);
};
AuctionSystem.prototype.getHighestBidder = function(itemId) {
    const heap = this.itemHeaps.get(itemId);
    if (!heap) return -1;
    
    while (heap.size() > 0) {
        const [amount, userId] = heap.peek();
        if (this.bids.get(`${itemId}:${userId}`) === amount) {
            return userId;
        }
        heap.pop();
    }
    
    return -1;
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
- [1396. Design Underground System](../../1501-2000/1512-design-underground-system/)
- [1603. Design Parking System](../../1501-2000/1708-design-parking-system/)
- [1912. Design Movie Rental System](../../2001-2500/2023-design-movie-rental-system/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/design-auction-system/)
