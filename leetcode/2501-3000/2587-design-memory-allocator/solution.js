
var Allocator = function(n) {
    this.n = n;
    this.memory = new Int32Array(n);
    this.blocks = new Map();
};
Allocator.prototype.allocate = function(size, mID) {
    let freeRun = 0;
    
    for (let i = 0; i < this.n; i++) {
        if (this.memory[i] === 0) {
            freeRun++;
            if (freeRun === size) {
                const start = i - size + 1;
                this.memory.fill(mID, start, i + 1);
                if (!this.blocks.has(mID)) {
                    this.blocks.set(mID, []);
                }
                this.blocks.get(mID).push([start, size]);
                return start;
            }
        } else {
            freeRun = 0;
        }
    }
    
    return -1;
};
Allocator.prototype.freeMemory = function(mID) {
    const ranges = this.blocks.get(mID);
    if (!ranges) return 0;
    
    let freed = 0;
    for (const [start, size] of ranges) {
        this.memory.fill(0, start, start + size);
        freed += size;
    }
    
    this.blocks.delete(mID);
    return freed;
};
