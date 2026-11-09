
var MyLinkedList = function() {
    this.head = null;
    this.size = 0;
};

// Node structure
var ListNode = function(val) {
    this.val = val;
    this.next = null;
};

// Get value at index
MyLinkedList.prototype.get = function(index) {
    if (index < 0 || index >= this.size) {
        return -1;
    }

    let current = this.head;

    for (let i = 0; i < index; i++) {
        current = current.next;
    }

    return current.val;
};

// Add node at head
MyLinkedList.prototype.addAtHead = function(val) {
    let node = new ListNode(val);

    node.next = this.head;
    this.head = node;

    this.size++;
};

// Add node at tail
MyLinkedList.prototype.addAtTail = function(val) {
    let node = new ListNode(val);

    if (!this.head) {
        this.head = node;
    } else {
        let current = this.head;

        while (current.next) {
            current = current.next;
        }

        current.next = node;
    }

    this.size++;
};

// Add node at given index
MyLinkedList.prototype.addAtIndex = function(index, val) {
    if (index < 0) {
        index = 0;
    }

    if (index > this.size) {
        return;
    }

    if (index === 0) {
        this.addAtHead(val);
        return;
    }

    let current = this.head;

    for (let i = 0; i < index - 1; i++) {
        current = current.next;
    }

    let node = new ListNode(val);

    node.next = current.next;
    current.next = node;

    this.size++;
};

// Delete node at given index
MyLinkedList.prototype.deleteAtIndex = function(index) {
    if (index < 0 || index >= this.size) {
        return;
    }

    if (index === 0) {
        this.head = this.head.next;
    } else {
        let current = this.head;

        for (let i = 0; i < index - 1; i++) {
            current = current.next;
        }

        current.next = current.next.next;
    }

    this.size--;
};

