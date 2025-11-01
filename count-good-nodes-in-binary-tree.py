class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values):
    """Helper to build a binary tree from level-order list."""
    if not values:
        return None
    nodes = [None if v is None else TreeNode(v) for v in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_val):
            if not node:
                return 0
            count = 1 if node.val >= max_val else 0
            max_val = max(max_val, node.val)
            left = dfs(node.left, max_val)
            right = dfs(node.right, max_val)
            return count + left + right

        return dfs(root, float('-inf'))


# ---- Test ----
if __name__ == "__main__":
    root = build_tree([3, 1, 4, 3, None, 1, 5])
    s = Solution()
    print("Count of good nodes:", s.goodNodes(root))
