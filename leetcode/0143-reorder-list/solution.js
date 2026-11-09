
var reorderList = function(head) {
    if (!head || !head.next) return;

    // Step 1: Find the middle of the linked list
    let slow = head;
    let fast = head;

    while (fast.next && fast.next.next) {
        slow = slow.next;
        fast = fast.next.next;
    }

    // Step 2: Reverse the second half
    let second = slow.next;
    slow.next = null;

    let prev = null;

    while (second) {
        let nextNode = second.next;
        second.next = prev;
        prev = second;
        second = nextNode;
    }

    // Step 3: Merge the two halves alternately
    let first = head;
    second = prev;

    while (second) {
        let temp1 = first.next;
        let temp2 = second.next;

        first.next = second;
        second.next = temp1;

        first = temp1;
        second = temp2;
    }
};

