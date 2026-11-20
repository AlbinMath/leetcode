var SeatManager = function(n) {
    this.marker = 1;
    this.heap = [];
};
SeatManager.prototype.reserve = function() {
    if (this.heap.length > 0) {
        return this._pop();
    }
    return this.marker++;
};
SeatManager.prototype.unreserve = function(seatNumber) {
    this._push(seatNumber);
};

SeatManager.prototype._push = function(val) {
    this.heap.push(val);
    let i = this.heap.length - 1;
    while (i > 0) {
        const parent = (i - 1) >> 1;
        if (this.heap[parent] <= this.heap[i]) break;
        [this.heap[parent], this.heap[i]] = [this.heap[i], this.heap[parent]];
        i = parent;
    }
};

SeatManager.prototype._pop = function() {
    const top = this.heap[0];
    const last = this.heap.pop();
    if (this.heap.length > 0) {
        this.heap[0] = last;
        let i = 0;
        const len = this.heap.length;
        while (true) {
            let smallest = i;
            const left = (i << 1) + 1;
            const right = (i << 1) + 2;
            if (left < len && this.heap[left] < this.heap[smallest]) smallest = left;
            if (right < len && this.heap[right] < this.heap[smallest]) smallest = right;
            if (smallest === i) break;
            [this.heap[i], this.heap[smallest]] = [this.heap[smallest], this.heap[i]];
            i = smallest;
        }
    }
    return top;
};
