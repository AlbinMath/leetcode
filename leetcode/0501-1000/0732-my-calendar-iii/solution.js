var MyCalendarThree = function() {
    this.diff = new Map();
};
MyCalendarThree.prototype.book = function(startTime, endTime) {
    this.diff.set(startTime, (this.diff.get(startTime) || 0) + 1);
    this.diff.set(endTime, (this.diff.get(endTime) || 0) - 1);
    const times = Array.from(this.diff.keys()).sort((a, b) => a - b);
    
    let active = 0;
    let maxK = 0;
    for (const time of times) {
        active += this.diff.get(time);
        if (active > maxK) {
            maxK = active;
        }
    }
    
    return maxK;
};
