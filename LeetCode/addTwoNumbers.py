## https://leetcode.com/problems/add-two-numbers/submissions/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        head = res
        carry = 0
        while True :
            temp = l1.val + l2.val + carry
            l1=l1.next
            l2=l2.next
            res.val = temp%10
            carry = temp//10
            # print("{} | {}".format(res.val, carry))
            if l1 and l2:
                res.next = ListNode()
                res = res.next
            else:
                break
        while l1:
            res.next=ListNode()
            res = res.next
            temp = l1.val + carry
            res.val = temp%10
            # print("{} | {}".format(res.val, temp//10))
            carry = temp//10
            l1 = l1.next
        
        while l2:
            res.next=ListNode()
            res = res.next
            temp = l2.val + carry
            res.val = temp%10
            carry = temp//10
            l2 = l2.next
        
        if carry!=0:
            res.next = ListNode()
            res = res.next
            res.val = carry
            
        return head