class Node(object):
    def __init__(self, value):
        self.right = None
        self.left = None
        self.value = value
        
    def is_leaf(self):
        return self.right == self.left == None


class BinarySearchTree(object):
    def __init__(self):
        self.root = None
        self.len = 0
        self.__repr__ == self.__str__

    def __len__(self):
        return self.len

    def __repr__(self):
        return "BST: %s" % ", ".join([str(v) for v in self.values()])

    def is_empty(self):
        return self.root == None

    def insert(self, val):
        """ inserts the value val in the tree """
        if self.len == 0:
            node = Node(val)
            self.root = node
            self.len += 1
            return
        node = self.root
        while (node != None):
            parent = node
            if node.value <= val:
                node = node.right
            elif node.value > val:
                node = node.left
        if parent.value > val:
            parent.left = Node(val)
            self.len += 1
            return
        parent.right = Node(val)
        self.len += 1
        return


    def remove(self, k):
        """ remove the value and the key k """
        node = self.root
        while node != None:
            if node.value < k:
                parent = node
                node = node.right
            elif node.value > k:
                parent = node
                node = node.left
            else:
                break
        if not node:
            raise IndexError("%s not in tree" % k)
        n = node
        if node.is_leaf():
            # if node is a leaf
            if parent.left == node:
                parent.left = None
            else:
                parent.right = None
            del node
            return n.value
        elif node.left and node.right:
            # node has 2 children, find the successor
            s = node.right
            p = node
            while s.left != None:
                p = s
                s = p.left
            old_value = node.value
            node.value = s.value
            if not s.is_leaf():
                p.left = s.right
            else:
                if p.value > old_value:
                    p.right = None
                else:
                    p.left = None
            del s
            return old_value
        else:
            # node has 1 child
            if node.left:
                if node.value > parent.value:
                    parent.right = node.left
                else:
                    parent.left = node.left
            else:
                if node.value > parent.value:
                    parent.right = node.right
                else:
                    parent.left = node.right
            del node
            return n.value

    def search(self, k):
        """ returns the node associated with the key k """
        node = self.root
        while node != None:
            if node.value < k:
                node = node.right
            elif node.value > k:
                node = node.left
            else:
                return node
        return None

    def extreme_node(self, side):
        """ returns extreme side node - left for minimum, right for maximum """
        node = self.root
        while node != None:
            parent = node
            if side == "left":
                node = node.left
            elif side == "right":
                node = node.right
        return parent.value

    def minimum(self):
        """ returns the value associated with the minimum key """
        return self.extreme_node("left")
    
    def maximum(self):
        """ returns the value associated with the maximum key """
        return self.extreme_node("right")

    def values(self, reverse=False):
        """ returns an inorder traversal of the binary tree """
        if self.len == 0: return []
        values = []
        self.inorder(self.root, values)
        if reverse:
            return values[::-1]
        return values

    def inorder(self, root, values):
        if root != None:
            self.inorder(root.left, values)
            values.append(root.value)
            self.inorder(root.right, values)
            
if __name__ == "__main__":
    tree = BinarySearchTree()
    nodes = [18, 25, 12, 25, 28, 29, 15, 4, 1, 3, 13, 17, 14]
    for n in nodes:
        tree.insert(n)
