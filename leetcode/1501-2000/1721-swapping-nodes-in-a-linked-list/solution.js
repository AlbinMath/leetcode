
var swapNodes = function(head, k) {
    let first = head;

    // Step 1: Find kth node from beginning
    for (let i = 1; i < k; i++) {
        first = first.next;
    }

    // Save kth node from beginning
    let node1 = first;

    // Step 2: Find kth node from end
    let second = head;
    let current = first;

    while (current.next) {
        current = current.next;
        second = second.next;
    }

    // Step 3: Swap values
    let temp = node1.val;
    node1.val = second.val;
    second.val = temp;

    return head;
};

