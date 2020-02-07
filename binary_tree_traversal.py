# 전위 순회를 구현합니다.
def preorder(node):
  if node:
    print(node.data, end=' ')
    preorder(node.left)
    preorder(node.right)

# 중위 순회를 구현합니다.
def inorder(node):
  if node:
    inorder(node.left)
    print(node.data, end=' ')
    inorder(node.right)

# 후위 순회를 구현합니다.
def postorder(node):
  if node:
    postorder(node.left)
    postorder(node.right)
    print(node.data, end=' ')