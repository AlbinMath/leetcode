
var insertGreatestCommonDivisors = function(head) {

    // Calculate GCD using Euclidean Algorithm
    function gcd(a, b) {
        while (b !== 0) {
            let temp = b;
            b = a % b;
            a = temp;
        }

        return a;
    }

    let current = head;

    // Traverse the linked list
    while (current && current.next) {

        // Calculate GCD of adjacent nodes
        let value = gcd(current.val, current.next.val);

        // Create new node
        let node = new ListNode(value);

        // Insert new node between current and next
        node.next = current.next;
        current.next = node;

        // Move to the next original node
        current = node.next;
    }

    return head;
};

