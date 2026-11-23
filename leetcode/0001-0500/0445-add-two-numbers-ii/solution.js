
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    const stack1 = [];
    const stack2 = [];

    while (l1) {
        stack1.push(l1.val);
        l1 = l1.next;
    }

    while (l2) {
        stack2.push(l2.val);
        l2 = l2.next;
    }

    let carry = 0;
    let result = null;

    while (stack1.length > 0 || stack2.length > 0 || carry > 0) {
        let sum = carry;

        if (stack1.length > 0) {
            sum += stack1.pop();
        }

        if (stack2.length > 0) {
            sum += stack2.pop();
        }

        carry = Math.floor(sum / 10);

        const node = new ListNode(sum % 10);
        node.next = result;
        result = node;
    }

    return result;
};

