def validate_bst(root):

    def dfs(node, left, right):
        if not node: return True 

        if not (left < node.val < right):
            return False
        
        return dfs(node.left, left, node.val) and dfs(node.right, node.val, right)
    
    return dfs(root, float("-inf"), float("inf"))

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Tree: None
print(validate_bst(None))  # Expected output: True

# Tree:
#    1
print(validate_bst(TreeNode(1)))  # Expected output: True

# Tree:
#     2
#    / \
#   1   3
print(validate_bst(TreeNode(2, TreeNode(1), TreeNode(3))))  # Expected output: True

# Tree:
#     2
#    / \
#   1   3
print(validate_bst(TreeNode(2, TreeNode(1), TreeNode(3))))  # Expected output: True

# Tree:
#         10
#       /    \
#      5     20
#     / \   /  \
#    3   7 15  30
#           /
#          6  <-- Violation: 6 is less than 7 and should not be on the right subtree of 5.
print(validate_bst(TreeNode(10, TreeNode(5, TreeNode(3), TreeNode(7)), TreeNode(20, TreeNode(15, TreeNode(6)), TreeNode(30)))))  # Expected output: False
