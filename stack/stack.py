"""A stack implementation."""


class Stack(object):
    """A stack class implementing adding, peeking items."""

    def __init__(self):
        """Initialize a stack with empty list."""
        self.stack = []

    def isEmpty(self):
        """Check if the list is empty."""
        return self.stack == []

    def add(self, item):
        """Add an item to the stack."""
        self.stack.append(item)

    def remove(self):
        """Remove the top item from the stack."""
        self.stack.pop()

    def peek(self):
        """Show the item at the top of the stack."""
        return self.stack[len(self.stack) - 1]

    def size(self):
        """Return the size of the stack."""
        return len(self.stack)


if __name__ == '__main__':
    stack = Stack()
    print "Stack is empty {}".format(stack.isEmpty())
    stack.add(456)
    stack.add(617)
    stack.add(868)
    stack.add(452)
    print "Size of stack {}".format(stack.size())
    print "Stack is empty {}".format(stack.isEmpty())
    print "Top of the stack is {}".format(stack.peek())
    print "Removing {} from the top".format(stack.peek())
    stack.remove()
    print "Size of stack {}".format(stack.size())
