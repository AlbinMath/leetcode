var SnapshotArray = function(length) {
    this.snapId = 0;
    this.history = Array.from({ length }, () => [[0, 0]]);
};

SnapshotArray.prototype.set = function(index, val) {
    const records = this.history[index];

    if (records[records.length - 1][0] === this.snapId) {
        records[records.length - 1][1] = val;
    } else {
        records.push([this.snapId, val]);
    }
};

SnapshotArray.prototype.snap = function() {
    return this.snapId++;
};

SnapshotArray.prototype.get = function(index, snap_id) {
    const records = this.history[index];
    let left = 0;
    let right = records.length - 1;
    let result = 0;

    while (left <= right) {
        const mid = Math.floor((left + right) / 2);

        if (records[mid][0] <= snap_id) {
            result = records[mid][1];
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    return result;
};
