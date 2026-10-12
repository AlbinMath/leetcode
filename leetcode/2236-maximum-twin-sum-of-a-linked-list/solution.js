var pairSum = function(head) {
    let slow = head;
    let fast = head;

    // Find the middle of the linked list
    while (fast !== null && fast.next !== null) {
        slow = slow.next;
        fast = fast.next.next;
    }

    // Reverse the second half
    let prev = null;
    let curr = slow;

    while (curr !== null) {
        let next = curr.next;
        curr.next = prev;
        prev = curr;
        curr = next;
    }

    // Calculate the maximum twin sum
    let left = head;
    let right = prev;
    let maxSum = 0;

    while (right !== null) {
        maxSum = Math.max(maxSum, left.val + right.val);
        left = left.next;
        right = right.next;
    }

    return maxSum;
};
