
var removeNthFromEnd = function(head, n) {
    const dummy = new ListNode(0);
    dummy.next = head;

    let fast = dummy;
    let slow = dummy;

    // Move fast n + 1 steps ahead
    for (let i = 0; i <= n; i++) {
        fast = fast.next;
    }

    // Move both pointers until fast reaches the end
    while (fast !== null) {
        fast = fast.next;
        slow = slow.next;
    }

    // Remove the nth node from the end
    slow.next = slow.next.next;

    return dummy.next;
};

