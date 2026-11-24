var Router = function (memoryLimit) {
    this.limit = memoryLimit;
    this.queue = [];            // [source, destination, timestamp]
    this.qHead = 0;
    this.seen = new Set();
    this.byDest = new Map();    // dest -> { ts: [], head: 0 }
};

Router.prototype._remove = function () {
    const p = this.queue[this.qHead];
    this.queue[this.qHead++] = null; // free memory
    this.seen.delete(p[0] + "," + p[1] + "," + p[2]);
    this.byDest.get(p[1]).head++;
    return p;
};

/**
 * @param {number} source
 * @param {number} destination
 * @param {number} timestamp
 * @return {boolean}
 */
Router.prototype.addPacket = function (source, destination, timestamp) {
    const key = source + "," + destination + "," + timestamp;
    if (this.seen.has(key)) return false;

    if (this.queue.length - this.qHead === this.limit) this._remove();

    this.seen.add(key);
    this.queue.push([source, destination, timestamp]);
    let d = this.byDest.get(destination);
    if (!d) {
        d = { ts: [], head: 0 };
        this.byDest.set(destination, d);
    }
    d.ts.push(timestamp);
    return true;
};

/**
 * @return {number[]}
 */
Router.prototype.forwardPacket = function () {
    if (this.qHead === this.queue.length) return [];
    return this._remove();
};

/**
 * @param {number} destination
 * @param {number} startTime
 * @param {number} endTime
 * @return {number}
 */
Router.prototype.getCount = function (destination, startTime, endTime) {
    const d = this.byDest.get(destination);
    if (!d) return 0;
    const ts = d.ts;

    // first index in [head, len) with ts[idx] >= target
    const lowerBound = (target) => {
        let lo = d.head, hi = ts.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (ts[mid] < target) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    };

    return lowerBound(endTime + 1) - lowerBound(startTime);
};
