
var reverseBetween = function(head, left, right) {
    const dummy = new ListNode(0);
    dummy.next = head;

    let prev = dummy;

    // Move to the node just before position left
    for (let i = 1; i < left; i++) {
        prev = prev.next;
    }

    // Start reversing the sublist
    let curr = prev.next;

    for (let i = 0; i < right - left; i++) {
        const next = curr.next;

        curr.next = next.next;
        next.next = prev.next;
        prev.next = next;
    }

    return dummy.next;
};

