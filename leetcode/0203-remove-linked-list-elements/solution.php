/**
 * Definition for a singly-linked list.
 * class ListNode {
 *     public $val = 0;
 *     public $next = null;
 *     function __construct($val = 0, $next = null) {
 *         $this->val = $val;
 *         $this->next = $next;
 *     }
 * }
 */

class Solution {
    function removeElements($head, $val) {
        // Dummy node handles deletion of the head
        $dummy = new ListNode(0);
        $dummy->next = $head;

        $current = $dummy;

        while ($current->next !== null) {
            if ($current->next->val == $val) {
                // Remove the next node
                $current->next = $current->next->next;
            } else {
                $current = $current->next;
            }
        }

        return $dummy->next;
    }
}
