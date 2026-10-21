
var hasCycle = function(head) {
    let slow = head;
    let fast = head;

    while (fast !== null && fast.next !== null) {
        slow = slow.next;           // Move one step
        fast = fast.next.next;      // Move two steps

        if (slow === fast) {
            return true;
        }
    }

    return false;
};

