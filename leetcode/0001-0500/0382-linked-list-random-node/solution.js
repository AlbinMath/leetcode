
var Solution = function(head) {
    this.head = head;
};

Solution.prototype.getRandom = function() {
    let current = this.head;
    let result = 0;
    let count = 0;

    while (current) {
        count++;

        // Select current node with probability 1/count
        if (Math.floor(Math.random() * count) === 0) {
            result = current.val;
        }

        current = current.next;
    }

    return result;
};

