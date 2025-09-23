class TreeNode:
    def __init__(self , val):
        self.val = val
        self.left = None
        self.right = None
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.val , end=" ")
            self.inorder(root.right)
    def preorder(self, root):
        if root:
            print(root.val , end=" ")
            self.preorder(root.left)
            self.preorder(root.right)
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.val , end=" ")

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right= TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
print("\nThe Inorder Traversal is: ")
root.inorder(root)
print("\nThe Preorder Traversal is: ")
root.preorder(root)
print("\nThe Postorder Traversal is: ")
root.postorder(root)
print("\n")

