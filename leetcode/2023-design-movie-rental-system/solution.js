class CustomMinHeap {
    constructor(compare) {
        this.data = [];
        this.compare = compare;
    }
    size() {
        return this.data.length;
    }
    push(val) {
        this.data.push(val);
        let i = this.data.length - 1;
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (this.compare(this.data[p], this.data[i]) <= 0) break;
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
                if (l < n && this.compare(this.data[l], this.data[best]) < 0) best = l;
                if (r < n && this.compare(this.data[r], this.data[best]) < 0) best = r;
                if (best === i) break;
                [this.data[i], this.data[best]] = [this.data[best], this.data[i]];
                i = best;
            }
        }
        return top;
    }
}

var MovieRentingSystem = function(n, entries) {
    this.prices = new Map();
    this.unrented = new Map();
    this.rentedSet = new Set();
    
    // Order by price ASC, then shop ASC, then movie ASC
    this.rentedHeap = new CustomMinHeap((a, b) => 
        a[0] !== b[0] ? a[0] - b[0] : (a[1] !== b[1] ? a[1] - b[1] : a[2] - b[2])
    );
    
    for (const [shop, movie, price] of entries) {
        this.prices.set(`${shop}:${movie}`, price);
        if (!this.unrented.has(movie)) {
            // Order by price ASC, then shop ASC
            this.unrented.set(movie, new CustomMinHeap((a, b) => 
                a[0] !== b[0] ? a[0] - b[0] : a[1] - b[1]
            ));
        }
        this.unrented.get(movie).push([price, shop]);
    }
};

MovieRentingSystem.prototype.search = function(movie) {
    const heap = this.unrented.get(movie);
    if (!heap) return [];
    
    const res = [];
    const restored = [];
    
    while (heap.size() > 0 && res.length < 5) {
        const [price, shop] = heap.pop();
        const key = `${shop}:${movie}`;
        if (this.rentedSet.has(key)) continue;
        
        const prev = restored[restored.length - 1];
        if (prev && prev[0] === price && prev[1] === shop) continue;
        
        res.push(shop);
        restored.push([price, shop]);
    }
    
    for (const item of restored) {
        heap.push(item);
    }
    return res;
};

MovieRentingSystem.prototype.rent = function(shop, movie) {
    const key = `${shop}:${movie}`;
    const price = this.prices.get(key);
    this.rentedSet.add(key);
    this.rentedHeap.push([price, shop, movie]);
};
MovieRentingSystem.prototype.drop = function(shop, movie) {
    const key = `${shop}:${movie}`;
    const price = this.prices.get(key);
    this.rentedSet.delete(key);
    this.unrented.get(movie).push([price, shop]);
};

MovieRentingSystem.prototype.report = function() {
    const res = [];
    const restored = [];
    
    while (this.rentedHeap.size() > 0 && res.length < 5) {
        const [price, shop, movie] = this.rentedHeap.pop();
        const key = `${shop}:${movie}`;
        if (!this.rentedSet.has(key)) continue;
        
        const prev = restored[restored.length - 1];
        if (prev && prev[0] === price && prev[1] === shop && prev[2] === movie) continue;
        
        res.push([shop, movie]);
        restored.push([price, shop, movie]);
    }
    
    for (const item of restored) {
        this.rentedHeap.push(item);
    }
    return res;
};
