
var DinnerPlates = function(capacity) {
    this.capacity = capacity;
    this.stacks = [];
    this.heap = [];
    this.right = -1;
};

// Insert into min heap
DinnerPlates.prototype.heapPush = function(val) {
    const heap = this.heap;
    heap.push(val);

    let i = heap.length - 1;

    while (i > 0) {
        let p = Math.floor((i - 1) / 2);

        if (heap[p] <= heap[i]) break;

        [heap[p], heap[i]] = [heap[i], heap[p]];
        i = p;
    }
};

// Remove minimum from min heap
DinnerPlates.prototype.heapPop = function() {
    const heap = this.heap;
    const min = heap[0];
    const last = heap.pop();

    if (heap.length > 0) {
        heap[0] = last;
        let i = 0;

        while (true) {
            let smallest = i;
            let left = 2 * i + 1;
            let right = 2 * i + 2;

            if (left < heap.length &&
                heap[left] < heap[smallest]) {
                smallest = left;
            }

            if (right < heap.length &&
                heap[right] < heap[smallest]) {
                smallest = right;
            }

            if (smallest === i) break;

            [heap[i], heap[smallest]] =
                [heap[smallest], heap[i]];

            i = smallest;
        }
    }

    return min;
};

// Push value
DinnerPlates.prototype.push = function(val) {
    // Create a new stack if no available stack exists
    if (this.heap.length === 0) {
        const index = this.stacks.length;

        this.stacks.push([]);
        this.heapPush(index);
    }

    // Always use the leftmost available stack
    const index = this.heap[0];

    this.stacks[index].push(val);

    this.right = Math.max(this.right, index);

    // Remove from heap if stack becomes full
    if (this.stacks[index].length === this.capacity) {
        this.heapPop();
    }
};

// Pop from rightmost non-empty stack
DinnerPlates.prototype.pop = function() {
    while (
        this.right >= 0 &&
        this.stacks[this.right].length === 0
    ) {
        this.right--;
    }

    if (this.right < 0) return -1;

    return this.popAtStack(this.right);
};

// Pop from a specific stack
DinnerPlates.prototype.popAtStack = function(index) {
    if (
        index < 0 ||
        index >= this.stacks.length ||
        this.stacks[index].length === 0
    ) {
        return -1;
    }

    const stack = this.stacks[index];
    const wasFull = stack.length === this.capacity;

    const val = stack.pop();

    // Add index only if it was previously full
    if (wasFull) {
        this.heapPush(index);
    }

    // Update rightmost non-empty stack
    while (
        this.right >= 0 &&
        this.stacks[this.right].length === 0
    ) {
        this.right--;
    }

    return val;
};

