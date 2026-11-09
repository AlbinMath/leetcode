
var doubleIt = function(head) {

    function reverse(node) {
        let prev = null;
        let current = node;

        while (current) {
            let nextNode = current.next;
            current.next = prev;
            prev = current;
            current = nextNode;
        }

        return prev;
    }

    // Reverse the linked list
    head = reverse(head);

    let current = head;
    let carry = 0;

    // Double each digit
    while (current) {
        let sum = current.val * 2 + carry;

        current.val = sum % 10;
        carry = Math.floor(sum / 10);

        if (!current.next && carry > 0) {
            current.next = new ListNode(carry);
            break; // Important: don't process the new node again
        }

        current = current.next;
    }

    // Reverse back
    return reverse(head);
};

