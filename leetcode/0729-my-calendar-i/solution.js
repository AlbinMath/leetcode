var MyCalendar = function() {
    this.calendar = [];
};

MyCalendar.prototype.book = function(startTime, endTime) {
    let left = 0;
    let right = this.calendar.length;
    while (left < right) {
        const mid = (left + right) >> 1;
        if (this.calendar[mid][0] < startTime) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    if (left > 0 && this.calendar[left - 1][1] > startTime) {
        return false;
    }
    if (left < this.calendar.length && this.calendar[left][0] < endTime) {
        return false;
    }
    
    this.calendar.splice(left, 0, [startTime, endTime]);
    return true;
};
