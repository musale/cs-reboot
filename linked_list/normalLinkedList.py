"""A normal unordered linked list."""
from nodeClass import Node


class UnOrderedLinkedList(object):
    """An  unordered linked list class."""

    def __init__(self):
        """Initialize."""
        self.head = None

    def isEmpty(self):
        """Check if the first node is None."""
        return self.head is None

    def add(self, item):
        """Add an item to the linked list."""
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        """Get the size of the list."""
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.getNext()
        return count

    def search(self, item):
        """Search the linked list for an item."""
        current = self.head
        found = False
        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        """Remove an item from the list."""
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())


if __name__ == '__main__':
    myList = UnOrderedLinkedList()
    myList.add(90)
    myList.add(34)
    myList.add(67)
    print "Data list size {}".format(myList.size())
    print "find 34 {}".format(myList.search(34))
    print "find 35 {}".format(myList.search(35))
    print "Remove 34 {}".format(myList.remove(34))
    print "Data list size {}".format(myList.size())
