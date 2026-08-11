# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/
# Difficulty: Easy
# Topic: Linked Lists
#
# Problem:
#   Given the head of a singly linked list, reverse the list and return the new head.
#
# Example:
#   Input:  1 -> 2 -> 3 -> 4 -> 5
#   Output: 5 -> 4 -> 3 -> 2 -> 1
#
# Approach: Iterative — walk with two pointers (prev, curr), flip each .next link.
# Time:  O(n)
# Space: O(1)

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next_node = curr.next  # save next before overwriting
            curr.next = prev       # flip the link
            prev = curr
            curr = next_node
        return prev


# ---------------------------------------------------------------------------
# Interview talking point
# ---------------------------------------------------------------------------
# "I use two pointers — prev starts at None (the new tail's null terminator),
#  curr walks the list. Each iteration I flip curr.next to prev, then advance
#  both. When curr is None we've passed every node; prev is the new head.
#  O(n) time, O(1) space — no extra data structures needed."
#
# Bonus: recursive version (O(n) space on call stack)
#   def reverseList(self, head):
#       if not head or not head.next:
#           return head
#       new_head = self.reverseList(head.next)
#       head.next.next = head
#       head.next = None
#       return new_head
# ---------------------------------------------------------------------------


# Quick smoke test
def build(vals):
    dummy = ListNode(0)
    cur = dummy
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


if __name__ == "__main__":
    s = Solution()
    print(to_list(s.reverseList(build([1, 2, 3, 4, 5]))))  # [5, 4, 3, 2, 1]
    print(to_list(s.reverseList(build([1, 2]))))            # [2, 1]
    print(to_list(s.reverseList(build([]))))                # []
