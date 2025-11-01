# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root, target):
        # if tree is empty
        if root is None:
            return False

        # if we reach a leaf node, check if the remaining target == node value
        if not root.left and not root.right:
            return target == root.val

        # subtract current node's value from target
        target -= root.val

        # check if either left or right subtree has a valid path
        left = self.hasPathSum(root.left, target)
        right = self.hasPathSum(root.right, target)

        if left or right:
            return True


if __name__ == "__main__":
    # Build sample tree:
    #       5
    #      / \
    #     4   8
    #    /   / \
    #   11  13  4
    #  / \       \
    # 7   2       1
    #
    # target = 22 → True (path 5→4→11→2)

    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)

    target = 22

    sol = Solution()
    print(sol.hasPathSum(root, target))  # Expected output: True
