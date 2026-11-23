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
    function reverseList($head) {
        $prev = null;
        $current = $head;

        while ($current !== null) {
            // Save the next node
            $next = $current->next;

            // Reverse the link
            $current->next = $prev;

            // Move prev forward
            $prev = $current;

            // Move current forward
            $current = $next;
        }

        return $prev;
    }
}

