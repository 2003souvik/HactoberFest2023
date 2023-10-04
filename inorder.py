class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def inorder_traversal(root):
    if root:
        # Traverse the left subtree
        inorder_traversal(root.left)
        
        # Visit the current node
        print(root.val)
        
        # Traverse the right subtree
        inorder_traversal(root.right)

# Example usage:
# Create a sample binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Perform inorder traversal
print("Inorder Traversal:")
inorder_traversal(root)
