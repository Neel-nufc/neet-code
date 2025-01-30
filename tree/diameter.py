def diameter(root):
    res = 0

    def dfs(node):
        if not node:
            return 0
        
        left = dfs(node.left)
        right = dfs(node.right)

        nonlocal res 
        res = max(res, left+right)

        return 1 + max(left,right)
    dfs(root)
    return res

# Test case: Single node tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1)
print(diameter(root))  # Expected output: 0

# Test case: Empty tree
root = None
print(diameter(root))  # Expected output: 0

# Test case: Perfect binary tree
#        1
#       / \
#      2   3
#     / \ / \
#    4  5 6  7
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print(diameter(root))  # Expected output: 4 (path 4 -> 2 -> 1 -> 3 -> 7)

# Test case: Unbalanced tree
#         1
#        /
#       2
#      /
#     3
#    /
#   4
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.left.left = TreeNode(4)

print(diameter(root))  # Expected output: 3 (path 4 -> 3 -> 2 -> 1)
