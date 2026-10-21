
var reverseKGroup = function(head, k) {
    const dummy = new ListNode(0);
    dummy.next = head;

    let groupPrev = dummy;

    while (true) {
        // Find the kth node in the current group
        let kth = groupPrev;

        for (let i = 0; i < k; i++) {
            kth = kth.next;
            if (kth === null) {
                return dummy.next;
            }
        }

        // Save the node after this group
        let groupNext = kth.next;

        // Reverse the current group
        let prev = groupNext;
        let curr = groupPrev.next;

        while (curr !== groupNext) {
            let nextNode = curr.next;
            curr.next = prev;
            prev = curr;
            curr = nextNode;
        }

        // Connect the reversed group to the previous part
        let oldGroupStart = groupPrev.next;
        groupPrev.next = kth;
        groupPrev = oldGroupStart;
    }
};

