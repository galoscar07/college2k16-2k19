class TreeNode(object):

    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    def is_left_child(self):
        return self.parent and self.parent.left == self

    def is_right_child(self):
        return self.parent and self.parent.right == self

    def is_leaf(self):
        return not (self.right or self.left)

    def has_any_children(self):
        return self.right or self.left

    def has_both_children(self):
        return self.right and self.left

    def has_one_child(self):
        return self.has_any_children() and not self.has_both_children()

    def replace_node_data(self, key, val, left, right):
        self.key = key
        self.val = val
        self.left = left
        self.right = right
        if self.left:
            self.left.parent = self
        if self.right:
            self.right.parent = self

    def __iter__(self):
        if self is None:
            return

        if self.left:
            # `in` calls `__iter__` so is recursive
            for elem in self.left:
                yield elem

        yield (self.key, self.val)

        if self.right:
            # recurse again
            for elem in self.right:
                yield elem

    def find_successor(self):
        if self.right:
            return self.right.find_min()

        if self.parent is None:
            return None

        if self.is_left_child():
            return self.parent

        self.parent.right = None
        successor = self.parent.find_successor()
        self.parent.right = self
        return successor

    def find_min(self):
        current = self
        while current.left:
            current = current.left
        return current

    def splice_out(self):
        if self.is_leaf():
            if self.is_left_child():
                self.parent.left = None
            else:
                self.parent.right = None

        else:
            promoted_node = self.left or self.right

            if self.is_left_child():
                self.parent.left = promoted_node
            else:
                self.parent.right = promoted_node
            promoted_node.parent = self.parent


class BinarySearchTree(object):
    TreeNodeClass = TreeNode

    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        if self.root is None:
            return
        return self.root.__iter__()

    def get_key_value_dict(self):
        data = {}
        if self.__iter__() is None:
            return data
        for elem in self.__iter__():
            key, value = elem
            data[key] = value
        return data

    def set_pair_key_value(self, key, value):
        if self.root:
            self._put(key, value, self.root)
        else:
            self.root = self.TreeNodeClass(key, value)
        self.size = self.size + 1

    def get_keys(self):
        return self.get_key_value_dict().keys()

    def get_values(self):
        return self.get_key_value_dict().values()

    def get(self, key):
        for keys, value in self.get_key_value_dict().items():
            if key == keys:
                return value
        return None

    def __setitem__(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = self.TreeNodeClass(key, val)
        self.size = self.size + 1

    def _put(self, key, val, node):
        if key < node.key:
            if node.left:
                self._put(key, val, node.left)
            else:
                node.left = self.TreeNodeClass(key, val, parent=node)
        else:
            if node.right:
                self._put(key, val, node.right)
            else:
                node.right = self.TreeNodeClass(key, val, parent=node)

