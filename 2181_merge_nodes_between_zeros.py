# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head.next
        current_node = ListNode(val=0)
        head = current_node
        while current != None:
            if current.val != 0:
                current_node.val += current.val
                current = current.next
            else:
                if current.next == None:
                    break
                new_node = ListNode(val=0)
                current_node.next = new_node
                current_node = new_node
                current = current.next
        
        return head




