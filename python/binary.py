class BinaryTree:
    def __init__(self):
        self.root = None
    
    def __str__(self):
        return self.root.__str__()

    def insert(self, value):
        if self.root:
            self.root.insert(Node(value)) 
        else:
            self.root = Node(value)

    def find(self, target):
        return self.root.find(target)

    def in_order(self):
        # return self.root.in_order()
        for node in self.root.in_order():
            yield node

    def pre_order(self):
        return self.root.pre_order()

    def post_order(self):
        return self.root.post_order()


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, node):
        if node.value < self.value:
            if self.left:
                self.left.insert(node)
            else:
                self.left = node
        elif node.value > self.value:
            if self.right:
                self.right.insert(node)
            else:
                self.right = node

    def find(self, target):
        if self.value == target:
            return True
        
        if self.value > target and self.left:
            return self.left.find(target)

        if self.value < target and self.right:
            return self.right.find(target)

        return False

    def in_order(self):
        if self.left:
            for lc in self.left.in_order():
                yield lc
        
        yield self

        if self.right:
            for rc in self.right.in_order():
                yield rc
        
    def pre_order(self):
        yield self

        if self.left:
            for lc in self.left.pre_order():
                yield lc

        if self.right:
            for rc in self.right.pre_order():
                yield rc
        
    def post_order(self):
        if self.right:
            for rc in self.right.post_order():
                yield rc

        yield self

        if self.left:
            for lc in self.left.post_order():
                yield lc


    def __str__(self):
        output = ""
        # traverse in-order
        for node in self.in_order():
            output = output + str(node.value) + ", "

        return output


tree = BinaryTree()
tree.insert(5)
from random import randrange
for i in range(100):
    tree.insert(randrange(0, 50))


if __name__ == '__main__':
    print("In Order")
    print(tree)