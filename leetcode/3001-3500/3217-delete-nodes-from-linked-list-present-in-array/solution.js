
var modifiedList = function(nums, head) {

    // Step 1: Store nums in a Set
    let set = new Set(nums);

    // Step 2: Create a dummy node
    let dummy = new ListNode(0);
    dummy.next = head;

    let current = dummy;

    // Step 3: Traverse and delete matching nodes
    while (current.next) {

        if (set.has(current.next.val)) {
            // Skip the node
            current.next = current.next.next;
        } else {
            current = current.next;
        }
    }

    return dummy.next;
};

