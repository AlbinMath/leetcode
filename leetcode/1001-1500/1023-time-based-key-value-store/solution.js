var TimeMap = function() {
    this.store = new Map();
};

TimeMap.prototype.set = function(key, value, timestamp) {
    if (!this.store.has(key)) {
        this.store.set(key, []);
    }

    this.store.get(key).push([timestamp, value]);
};

TimeMap.prototype.get = function(key, timestamp) {
    if (!this.store.has(key)) {
        return "";
    }

    const values = this.store.get(key);
    let left = 0;
    let right = values.length - 1;
    let result = "";

    while (left <= right) {
        const mid = Math.floor((left + right) / 2);

        if (values[mid][0] <= timestamp) {
            result = values[mid][1];
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    return result;
};
