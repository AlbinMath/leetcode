var SmallestInfiniteSet = function() {
    this.current = 1;
    this.addedBack = new Set();
};

SmallestInfiniteSet.prototype.popSmallest = function() {
    if (this.addedBack.size > 0) {
        let smallest = Infinity;

        for (const num of this.addedBack) {
            smallest = Math.min(smallest, num);
        }

        this.addedBack.delete(smallest);
        return smallest;
    }

    return this.current++;
};

SmallestInfiniteSet.prototype.addBack = function(num) {
    if (num < this.current) {
        this.addedBack.add(num);
    }
};
