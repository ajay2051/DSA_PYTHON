class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        """this function is used to insert data at beginning in linked list"""
        node = Node(data, self.head)  # In Node we are inserting data and next element will be head
        self.head = node

    def insert_at_end(self, data):
        """This function is used to insert data at end"""
        if self.head is None:  # It means linked list is empty
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:  # gets the last element in Node
            itr = itr.next
        itr.next = Node(data, None)

    def insert_values(self, data_list):
        """This function is used to insert list of values at end of linked list"""
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        """this function is used to calculate length of linked list"""
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_at(self, index, data):
        """Insert at given index"""
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Exception")
        if index == 0:
            return self.insert_at_beginning(data)
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def print(self):
        if self.head is None:
            print("Linked List is Empty")
            return

        itr = self.head
        linked_list_string = ""
        while itr:
            suffix = ""
            if itr.next:
                suffix = "----->"
            linked_list_string += str(itr.data) + suffix  # Append data in linked_list_string
            itr = itr.next
        print(linked_list_string)


if __name__ == "__main__":
    """Inserting data in linked list"""
    linked_list = LinkedList()
    linked_list.insert_at_beginning(5)
    linked_list.insert_at_beginning(10)
    linked_list.insert_at_beginning(15)
    linked_list.insert_at_end(25)
    linked_list.insert_at_end(30)
    linked_list.insert_values(["12", "45", "78"])
    linked_list.insert_at(2, 85)
    linked_list.print()
    linked_list.remove_at(1)
    linked_list.print()
    print(linked_list.get_length())
