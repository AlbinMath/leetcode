
var sortList = function(head) {
    if (head === null || head.next === null) {
        return head;
    }

    // Find the middle and split the list
    let slow = head;
    let fast = head;
    let prev = null;

    while (fast !== null && fast.next !== null) {
        prev = slow;
        slow = slow.next;
        fast = fast.next.next;
    }

    // Break the list into two halves
    prev.next = null;

    const left = sortList(head);
    const right = sortList(slow);

    // Merge the sorted halves
    return merge(left, right);
};

function merge(left, right) {
    const dummy = new ListNode(0);
    let tail = dummy;

    while (left !== null && right !== null) {
        if (left.val <= right.val) {
            tail.next = left;
            left = left.next;
        } else {
            tail.next = right;
            right = right.next;
        }

        tail = tail.next;
    }

    tail.next = left !== null ? left : right;

    return dummy.next;
}

