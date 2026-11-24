
var Skiplist = function() {
    this.MAX_LEVEL = 16;
    this.P = 0.5;

    this.head = new SkipNode(-1, this.MAX_LEVEL);
    this.level = 1;
};

// Skiplist node
var SkipNode = function(val, level) {
    this.val = val;
    this.forward = new Array(level).fill(null);
};

// Generate random level
Skiplist.prototype.randomLevel = function() {
    let level = 1;

    while (
        Math.random() < this.P &&
        level < this.MAX_LEVEL
    ) {
        level++;
    }

    return level;
};

// Search
Skiplist.prototype.search = function(target) {
    let current = this.head;

    for (let i = this.level - 1; i >= 0; i--) {
        while (
            current.forward[i] &&
            current.forward[i].val < target
        ) {
            current = current.forward[i];
        }
    }

    current = current.forward[0];

    return current !== null && current.val === target;
};

// Add
Skiplist.prototype.add = function(num) {
    let update = new Array(this.MAX_LEVEL);
    let current = this.head;

    // Find insertion positions
    for (let i = this.level - 1; i >= 0; i--) {
        while (
            current.forward[i] &&
            current.forward[i].val < num
        ) {
            current = current.forward[i];
        }

        update[i] = current;
    }

    // Generate random level
    let newLevel = this.randomLevel();

    if (newLevel > this.level) {
        for (let i = this.level; i < newLevel; i++) {
            update[i] = this.head;
        }

        this.level = newLevel;
    }

    // Create and insert node
    let node = new SkipNode(num, newLevel);

    for (let i = 0; i < newLevel; i++) {
        node.forward[i] = update[i].forward[i];
        update[i].forward[i] = node;
    }
};

// Erase
Skiplist.prototype.erase = function(num) {
    let update = new Array(this.MAX_LEVEL);
    let current = this.head;

    // Find node and its predecessors
    for (let i = this.level - 1; i >= 0; i--) {
        while (
            current.forward[i] &&
            current.forward[i].val < num
        ) {
            current = current.forward[i];
        }

        update[i] = current;
    }

    current = current.forward[0];

    if (!current || current.val !== num) {
        return false;
    }

    // Remove node from every level where it exists
    for (let i = 0; i < this.level; i++) {
        if (update[i].forward[i] === current) {
            update[i].forward[i] = current.forward[i];
        }
    }

    // Reduce empty top levels
    while (
        this.level > 1 &&
        this.head.forward[this.level - 1] === null
    ) {
        this.level--;
    }

    return true;
};

