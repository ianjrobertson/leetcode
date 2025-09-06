# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        # Okay, so the idea here is that we need to go through the linked list, and then remove the elements that are present in the List. 
        # We want to remove them in a single pass
        # We need to stitch back the list when we remove something. 

        # I like the idea of turning nums into a dict, then we can check if node.val exists in it. 

        # do we need to store whatever the current head is? 
        # When does the head change? Just if the head gets removed? 
        nums_set = set(nums)
        curr = head
        prev = None
        while curr != None:
            if curr.val in nums_set:
                temp = curr
                curr = self.remove(prev, curr)
                if temp == head:
                    head = curr
            else:
                prev = curr
                curr = curr.next
        
        return head


    def remove(self, prev: Optional[ListNode], node: Optional[ListNode]):
        if prev != None:
            prev.next = node.next
            node.next = None
            return prev.next
        else:
            next_node = node.next
            node.next = None
            return next_node
