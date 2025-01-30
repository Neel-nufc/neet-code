# Definition for a binary tree node

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sub_tree(s,t):
    if not t:
        return True
    if not s:
        return False
    
    def is_same(s,t):
        if not s and not t:
            return True
        
        if s and t and s.val == t.val:
            return is_same(s.left, t.left) and is_same(s.right,t.right)
        
        return False
    
    if is_same(s,t):
        return True
    
    return sub_tree(s.left,t) or sub_tree(s.right, t)

# Constructing main tree 's'
#        3
#       / \
#      4   5
#     / \
#    1   2

s = TreeNode(3)
s.left = TreeNode(4)
s.right = TreeNode(5)
s.left.left = TreeNode(1)
s.left.right = TreeNode(2)



# Constructing subtree 't'
#      4
#     / \
#    1   2

t = TreeNode(4)
t.left = TreeNode(1)
t.right = TreeNode(3)


# Test the function

print(sub_tree(s, t))