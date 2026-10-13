
var BSTIterator = function(root) {
    this.stack = [];
    this.pushLeft(root);
};

// Push the entire left path onto the stack
BSTIterator.prototype.pushLeft = function(node) {
    while (node !== null) {
        this.stack.push(node);
        node = node.left;
    }
};

BSTIterator.prototype.next = function() {
    const node = this.stack.pop();

    // Visit the right subtree next
    if (node.right !== null) {
        this.pushLeft(node.right);
    }

    return node.val;
};

BSTIterator.prototype.hasNext = function() {
    return this.stack.length > 0;
};

