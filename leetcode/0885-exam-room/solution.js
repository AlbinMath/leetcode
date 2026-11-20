var ExamRoom = function(n) {
    this.n = n;
    this.seats = [];
};
ExamRoom.prototype.seat = function() {
    if (this.seats.length === 0) {
        this.seats.push(0);
        return 0;
    }

    let maxDist = this.seats[0];
    let target = 0;
    for (let i = 0; i < this.seats.length - 1; i++) {
        const a = this.seats[i];
        const b = this.seats[i + 1];
        const dist = (b - a) >> 1;
        if (dist > maxDist) {
            maxDist = dist;
            target = a + dist;
        }
    }
    if ((this.n - 1) - this.seats[this.seats.length - 1] > maxDist) {
        target = this.n - 1;
    }
    
    let left = 0;
    let right = this.seats.length;
    while (left < right) {
        const mid = (left + right) >> 1;
        if (this.seats[mid] < target) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    
    this.seats.splice(left, 0, target);
    return target;
};
ExamRoom.prototype.leave = function(p) {
    let left = 0;
    let right = this.seats.length - 1;
    while (left <= right) {
        const mid = (left + right) >> 1;
        if (this.seats[mid] === p) {
            this.seats.splice(mid, 1);
            return;
        } else if (this.seats[mid] < p) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
};
