def find_depth(root):
    
    def dfs(node):
        if not node:
            return 0
        
        left = dfs(node.left)
        right = dfs(node.right)

        return 1 + max(left,right)
    return dfs(root)

# Test case: Single node tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

print(find_depth(None))  # Expected output: 0
print(find_depth(TreeNode(1)))  # Expected output: 1
# Tree:
#     1
#    / \
#   2   3
#  /
# 4
print(find_depth(TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))))  # Expected output: 3
# Tree:
#         1
#       /   \
#      2     3
#     / \   / \
#    4   5 6   7
print(find_depth(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))))  # Expected output: 3
# Tree:
#     1
#      \
#       2
#        \
#         3
print(find_depth(TreeNode(1, None, TreeNode(2, None, TreeNode(3)))))  # Expected output: 3
# Tree:
#     1
#    /
#   2
#  /
# 3
print(find_depth(TreeNode(1, TreeNode(2, TreeNode(3)))))  # Expected output: 3
# Tree:
#         1
#       /   \
#      2     3
#     / \   / \
#    4   5 6   7
#               \
#                8
print(find_depth(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7, None, TreeNode(8))))))  # Expected output: 4
