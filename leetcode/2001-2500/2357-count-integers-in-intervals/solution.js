var CountIntervals = function() {
    this.intervals = [];
    this.total = 0;
};
CountIntervals.prototype.add = function(left, right) {
    let lo = 0;
    let hi = this.intervals.length;
    while (lo < hi) {
        const mid = (lo + hi) >> 1;
        if (this.intervals[mid][1] < left - 1) {
            lo = mid + 1;
        } else {
            hi = mid;
        }
    }
    
    let end = lo;
    while (end < this.intervals.length && this.intervals[end][0] <= right + 1) {
        const [l, r] = this.intervals[end];
        if (l < left) left = l;
        if (r > right) right = r;
        this.total -= (r - l + 1);
        end++;
    }
    
    this.intervals.splice(lo, end - lo, [left, right]);
    this.total += (right - left + 1);
};
CountIntervals.prototype.count = function() {
    return this.total;
};
