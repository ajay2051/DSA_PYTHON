# Folder Structure in OS in one of the example of tree.

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        spaces = " " * self.get_level() * 3
        prefix = spaces + "|---" if self.parent else ""
        print(prefix + self.data)
        for child in self.children:
            child.print_tree()

    def add_child(self, child):
        child.parent = self
        self.children.append(child)


def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("ThinkPad"))

    phone = TreeNode("Cell Phone")
    phone.add_child(TreeNode("iphone"))
    phone.add_child(TreeNode("Pixel"))
    phone.add_child(TreeNode("Samsung"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Philips"))
    tv.add_child(TreeNode("LG"))
    tv.add_child(TreeNode("Panasonic"))

    root.add_child(laptop)
    root.add_child(phone)
    root.add_child(tv)

    root.get_level()
    root.print_tree()


if __name__ == "__main__":
    build_product_tree()
