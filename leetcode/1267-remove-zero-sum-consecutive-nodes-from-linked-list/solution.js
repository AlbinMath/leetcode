
var removeZeroSumSublists = function(head) {
    // Dummy node handles cases where the head must be removed
    let dummy = new ListNode(0);
    dummy.next = head;

    let map = new Map();
    let sum = 0;
    let current = dummy;

    // First pass: store the last node for each prefix sum
    while (current) {
        sum += current.val;
        map.set(sum, current);
        current = current.next;
    }

    // Second pass: skip zero-sum sequences
    sum = 0;
    current = dummy;

    while (current) {
        sum += current.val;
        current.next = map.get(sum).next;
        current = current.next;
    }

    return dummy.next;
};

