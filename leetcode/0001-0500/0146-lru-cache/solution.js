
var LRUCache = function(capacity) {
    this.capacity = capacity;
    this.cache = new Map();

    this.head = { key: 0, value: 0, prev: null, next: null };
    this.tail = { key: 0, value: 0, prev: null, next: null };

    this.head.next = this.tail;
    this.tail.prev = this.head;
};

// Remove a node from the list
LRUCache.prototype.remove = function(node) {
    node.prev.next = node.next;
    node.next.prev = node.prev;
};

// Insert a node right after the head (most recently used)
LRUCache.prototype.insertFront = function(node) {
    node.next = this.head.next;
    node.prev = this.head;

    this.head.next.prev = node;
    this.head.next = node;
};

// Move an existing node to the front
LRUCache.prototype.moveToFront = function(node) {
    this.remove(node);
    this.insertFront(node);
};

LRUCache.prototype.get = function(key) {
    if (!this.cache.has(key)) {
        return -1;
    }

    const node = this.cache.get(key);
    this.moveToFront(node);

    return node.value;
};

LRUCache.prototype.put = function(key, value) {
    if (this.cache.has(key)) {
        const node = this.cache.get(key);
        node.value = value;
        this.moveToFront(node);
        return;
    }

    const node = {
        key,
        value,
        prev: null,
        next: null
    };

    this.cache.set(key, node);
    this.insertFront(node);

    if (this.cache.size > this.capacity) {
        const lru = this.tail.prev;

        this.remove(lru);
        this.cache.delete(lru.key);
    }
};

