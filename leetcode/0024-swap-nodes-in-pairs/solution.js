
var swapPairs = function(head) {
    const dummy = new ListNode(0);
    dummy.next = head;

    let prev = dummy;

    while (prev.next !== null && prev.next.next !== null) {
        let first = prev.next;
        let second = first.next;

        // Swap the two nodes
        first.next = second.next;
        second.next = first;
        prev.next = second;

        // Move to the next pair
        prev = first;
    }

    return dummy.next;
};

