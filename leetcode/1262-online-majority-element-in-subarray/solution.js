
var MajorityChecker = function(arr) {
    this.arr = arr;
    this.positions = new Map();

    // Store every value's sorted occurrence indices
    for (let i = 0; i < arr.length; i++) {
        if (!this.positions.has(arr[i])) {
            this.positions.set(arr[i], []);
        }
        this.positions.get(arr[i]).push(i);
    }
};

MajorityChecker.prototype.query = function(left, right, threshold) {
    const arr = this.arr;
    const positions = this.positions;

    // Randomly sample candidates and verify their frequencies
    for (let attempt = 0; attempt < 30; attempt++) {
        const index =
            left + Math.floor(Math.random() * (right - left + 1));

        const value = arr[index];
        const indices = positions.get(value);

        // First occurrence >= left
        let lo = 0;
        let hi = indices.length;

        while (lo < hi) {
            const mid = Math.floor((lo + hi) / 2);

            if (indices[mid] < left) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }

        const start = lo;

        // First occurrence > right
        lo = 0;
        hi = indices.length;

        while (lo < hi) {
            const mid = Math.floor((lo + hi) / 2);

            if (indices[mid] <= right) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }

        const end = lo;

        if (end - start >= threshold) {
            return value;
        }
    }

    return -1;
};

