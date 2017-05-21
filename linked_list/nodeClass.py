"""An implentation of the node."""


class Node(object):
    """A node initialized with a head and data."""

    def __init__(self, data):
        """Initialize node with data."""
        self.next = None
        self.data = data

    def getData(self):
        """Get the data."""
        return self.data

    def getNext(self):
        """Get the next node."""
        return self.next

    def setData(self, newdata):
        """Assign new data."""
        self.data = newdata

    def setNext(self, newnext):
        """Set the next node."""
        self.next = newnext
