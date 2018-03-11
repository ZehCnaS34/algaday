class AVLNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.update_weight()

    def update_weight(self):
        if self.left:
            self.left.update_weight()
        if self.right:
            self.right.update_weight()
            
        left_weight = self.left.weight if self.left else -1
        right_weight = self.right.weight if self.right else -1
        self.weight = 1 + max(left_weight, right_weight)

    def insert(self, node):
        if self.value < node.value:
            if self.right:
                self.right.insert(node)
            else:
                self.right = node
        elif self.value > node.value:
            if self.left:
                self.left.insert(node)
            else:
                self.left = node
        
        self.update_weight()

    def rotate_left(self):
        if not self.right:
            return

        new_root = self.right
        self.right = new_root.left if new_root.left else None
        new_root.left = self

        new_root.update_weight()
        return new_root

    def rotate_right(self):
        if not self.right:
            return
        
        new_root = self.left
        self.left = new_root.right if new_root.right else None
        new_root.right = self

    def pre_order(self):
        yield self
        if self.left:
            for node in self.left.in_order():
                yield node
        if self.right:
            for node in self.right.in_order():
                yield node

    def in_order(self):
        if self.left:
            for node in self.left.in_order():
                yield node
        yield self
        if self.right:
            for node in self.right.in_order():
                yield node

    def pre_pair(self):
        def gen():
            yield str(self.value)
            yield "("
            if self.left:
                for node in self.left.pre_pair():
                    yield node
            if self.right:
                for node in self.right.pre_pair():
                    yield node
            yield ")"

        return ''.join(gen())
    
    def __str__(self):
        return ', '.join(str(i.value) + ":" + str(i.weight) for i in self.in_order())


if __name__ == '__main__':
    n = AVLNode(3)
    n.insert(AVLNode(4))
    n.insert(AVLNode(5))