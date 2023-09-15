from typing import Optional


class BinarySearchTreeNode:
    def __init__(self, data: int):
        self.data = data
        self.right: Optional["BinarySearchTreeNode"] = None
        self.left: Optional["BinarySearchTreeNode"] = None

    def add_child(self, data: int) -> Optional["BinarySearchTreeNode"]:
        if self.data == data:
            return
        if data < self.data:
            if self.left is None:
                self.left = BinarySearchTreeNode(data)  # create sub left tree
            else:
                self.left.add_child(data)
        else:
            if self.right is None:
                self.right = BinarySearchTreeNode(data)  # create sub right tree
            else:
                self.right.add_child(data)

    def in_order_traversal(self):

        elements = []
        # visit left tree
        if self.left:
            elements += self.left.in_order_traversal()
        elements.append(self.data)
        # visit right tree
        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    def search(self, value):
        if self.data == value:
            return True
        if value < self.data:
            if self.left is None:
                return False
            else:
                return self.left.search(value)
        if value > self.data:
            if self.right is None:
                return False
            else:
                return self.right.search(value)

    def delete(self, value):
        if value < self.data:
            if self.left:
                self.left.delete(value)
        elif value > self.data:
            if self.right:
                self.right.delete(value)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            min_value = self.right.find_min()
            self.data = min_value
            self.right = self.right.delete(min_value)
        return self

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()


def build_tree(elements):
    print("Building Tree: ", elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root


if __name__ == "__main__":
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    countries = ['Nepal', "India", "Pakistan"]
    country_tree = build_tree(countries)
    print(country_tree.search("India"))
    print(country_tree.search("UK"))
    number_tree = build_tree(numbers)
    number_tree.delete(20)
    print(number_tree.in_order_traversal())
    print(number_tree.search(18))
    print(number_tree.search(124589))
