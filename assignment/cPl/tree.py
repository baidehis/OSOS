def inorderTransversal(node): 
    return
inOrdertransversal(node.right)


def search(node,value):
    if node is None:
        return None
    
    if node.data == value:
        print(node.data)
        return node
    
    elif node.data == value:
        print(value)
        return node
    elif value < node.data:
        return search(node.left,value)
    else:
        return search(node.right,value)
    

def insert(node,data):
    if node is None:
        print(f"\ncreated new node with data(node)")
        return TreeNode(data)
    else:
     if data < node.data:
      node.left = insert(node.left,data)
     elif data > node.data:
      node.right = insert(node.right,data)
    retun node

#13, 7,3,8,14,15,19,18



root = TreeNode(7)
root = TreeNode(3)
root = TreeNode(8)
root = TreeNode(14)
root = TreeNode(15)
root = TreeNode(19)
root = TreeNode(18)


insert(root,10)
search(root,14)