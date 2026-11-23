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
    function getIntersectionNode($headA, $headB) {
        $pA = $headA;
        $pB = $headB;

        while ($pA !== $pB) {
            // Move to next node, or switch to headB
            if ($pA === null) {
                $pA = $headB;
            } else {
                $pA = $pA->next;
            }

            // Move to next node, or switch to headA
            if ($pB === null) {
                $pB = $headA;
            } else {
                $pB = $pB->next;
            }
        }

        return $pA;
    }
}
