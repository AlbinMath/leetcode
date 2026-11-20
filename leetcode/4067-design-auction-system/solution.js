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
