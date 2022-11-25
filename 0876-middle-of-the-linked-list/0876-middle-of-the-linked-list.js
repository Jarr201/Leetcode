/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var middleNode = function(head) {
    let count = 0
    
    const bigHead = new ListNode(null)
    bigHead.next = head
    let head1 = bigHead
    let head2 = bigHead
    
    while (head1.next !== null) {
        count++
        head1 = head1.next
    }
    
    console.log(count)
    if (count % 2 == 0) {
        count++
    }
    
    i = 0
    while (i < count/2) {
        head2 = head2.next
        i++
    }
    return(head2)
};