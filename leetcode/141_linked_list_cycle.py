# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool                                    
        """
        p = head
        q = head
        while head:
            # print(head.val)
            if q.next != None and q.next.next != None:
                p = p.next
                q = q.next.next
            else:
                return False
            if p != q:
                head = head.next
            else:
                return True
        return False


if __name__ == '__main__':
    a = ListNode(3)
    b = ListNode(2)
    c = ListNode(0)
    d = ListNode(-4)
    a.next = b
    b.next = c
    c.next = d
    d.next = b

    sulo = Solution()
    print(sulo.hasCycle(a))
