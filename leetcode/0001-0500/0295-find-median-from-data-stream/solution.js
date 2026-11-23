
var MedianFinder = function() {
    this.lower = []; // Max heap: smaller half
    this.upper = []; // Min heap: larger half
};

// Max heap insertion
MedianFinder.prototype.pushLower = function(num) {
    const heap = this.lower;
    heap.push(num);

    let i = heap.length - 1;

    while (i > 0) {
        const parent = Math.floor((i - 1) / 2);

        if (heap[parent] >= heap[i]) break;

        [heap[parent], heap[i]] = [heap[i], heap[parent]];
        i = parent;
    }
};

// Min heap insertion
MedianFinder.prototype.pushUpper = function(num) {
    const heap = this.upper;
    heap.push(num);

    let i = heap.length - 1;

    while (i > 0) {
        const parent = Math.floor((i - 1) / 2);

        if (heap[parent] <= heap[i]) break;

        [heap[parent], heap[i]] = [heap[i], heap[parent]];
        i = parent;
    }
};

// Remove the maximum from the max heap
MedianFinder.prototype.popLower = function() {
    const heap = this.lower;
    const top = heap[0];
    const last = heap.pop();

    if (heap.length > 0) {
        heap[0] = last;
        let i = 0;

        while (true) {
            let largest = i;
            const left = 2 * i + 1;
            const right = 2 * i + 2;

            if (
                left < heap.length &&
                heap[left] > heap[largest]
            ) largest = left;

            if (
                right < heap.length &&
                heap[right] > heap[largest]
            ) largest = right;

            if (largest === i) break;

            [heap[i], heap[largest]] =
                [heap[largest], heap[i]];

            i = largest;
        }
    }

    return top;
};

// Remove the minimum from the min heap
MedianFinder.prototype.popUpper = function() {
    const heap = this.upper;
    const top = heap[0];
    const last = heap.pop();

    if (heap.length > 0) {
        heap[0] = last;
        let i = 0;

        while (true) {
            let smallest = i;
            const left = 2 * i + 1;
            const right = 2 * i + 2;

            if (
                left < heap.length &&
                heap[left] < heap[smallest]
            ) smallest = left;

            if (
                right < heap.length &&
                heap[right] < heap[smallest]
            ) smallest = right;

            if (smallest === i) break;

            [heap[i], heap[smallest]] =
                [heap[smallest], heap[i]];

            i = smallest;
        }
    }

    return top;
};

MedianFinder.prototype.addNum = function(num) {
    if (
        this.lower.length === 0 ||
        num <= this.lower[0]
    ) {
        this.pushLower(num);
    } else {
        this.pushUpper(num);
    }

    // Balance the heaps
    if (this.lower.length > this.upper.length + 1) {
        this.pushUpper(this.popLower());
    } else if (this.upper.length > this.lower.length + 1) {
        this.pushLower(this.popUpper());
    }
};

MedianFinder.prototype.findMedian = function() {
    if (this.lower.length > this.upper.length) {
        return this.lower[0];
    }

    if (this.upper.length > this.lower.length) {
        return this.upper[0];
    }

    return (this.lower[0] + this.upper[0]) / 2;
};

