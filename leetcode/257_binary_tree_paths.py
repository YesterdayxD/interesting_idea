# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def previous(node):
    print(node.val)
    if node.left != None:
        previous(node.left)
    if node.right != None:
        previous(node.right)


class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        previous(root)



if __name__ == '__main__':
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(5)
    a.left = b
    a.right = c
    b.right = d

    solu=Solution()
    solu.binaryTreePaths(a)
