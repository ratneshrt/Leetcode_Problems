class TreeNode:
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None

def isSameTree(p,q):
    def DFS(node1,node2):
        if node1 == None and node2 == None:
            return True
        elif node1 == None or node2 == None:
            return False
        elif node1.val != node2.val:
            return False
        return DFS(node1.left, node2.left) and DFS(node1.right, node2.right)
    return DFS(p,q)