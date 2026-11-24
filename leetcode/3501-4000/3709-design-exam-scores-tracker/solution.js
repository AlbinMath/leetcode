var ExamTracker = function() {
    this.times = [];
    this.prefix = [0];
};
ExamTracker.prototype.record = function(time, score) {
    this.times.push(time);
    this.prefix.push(this.prefix[this.prefix.length - 1] + score);
};
ExamTracker.prototype.totalScore = function(startTime, endTime) {
    let lo = 0;
    let hi = this.times.length;
    while (lo < hi) {
        const mid = (lo + hi) >> 1;
        if (this.times[mid] < startTime) {
            lo = mid + 1;
        } else {
            hi = mid;
        }
    }
    const left = lo;
    lo = left;
    hi = this.times.length;
    while (lo < hi) {
        const mid = (lo + hi) >> 1;
        if (this.times[mid] <= endTime) {
            lo = mid + 1;
        } else {
            hi = mid;
        }
    }
    const right = lo;

    return this.prefix[right] - this.prefix[left];
};
