class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class CustomList:
    def __init__(self):
        self.head = None
        self.length = 0

    def __repr__(self):
        nodes = '[ '
        curr = self.head
        while curr:
            nodes += (str(curr.value) + ' -> ')
            curr = curr.next
        nodes += ' ]'
        return str(nodes)

    def __iter__(self):
        self.num = 0
        curr = self.head
        while curr:
            yield curr
            curr = curr.next

    def __getitem__(self, index):
        if index >= self.length:
            raise IndexError('List index is out of range =)')
        count = 0
        for item in self:
            if index == count:
                return item
            count += 1
            continue

    def __setitem__(self, index, value):
        if index >= self.length:
            raise IndexError('List index is out of range =)')
        count = 0
        for item in self:
            if index == count:
                item.value = value
            count += 1
            continue

    def add(self, value):
        """
        Insert a new element at the end of the list.
        Each call of this method increments self.length property by 1.
        """
        self.length = 1
        if not self.head:
            self.head = Node(value)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
            self.length += 1
        curr.next = Node(value)
        self.length += 1

    def find(self, key):
        """
        Search for the first element with value matching the key.
        Return the Node object or print message that value is not found
        """
        curr = self.head
        try:
            while curr.value != key:
                curr = curr.next
            return curr
        except AttributeError:
            print('The value not found')

    def remove_by_value(self, key):
        """
        Remove the first occurence of the key in the list.
        Each call of this method decrements self.length property by 1.
        """
        curr = self.head
        prev = None
        while curr and curr.value != key:
            prev = curr
            curr = curr.next
        if prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None
            self.length -= 1

    def remove_by_index(self, index):
        """
        Remove the element using its index.
        Each call of this method decrements self.length property by 1.
        """
        if index >= self.length:
            raise IndexError('List index is out of range =)')
        curr = self.head
        prev = None
        count = 0
        while curr and count != index:
            prev = curr
            curr = curr.next
            count += 1
        if prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None
            self.length -= 1

    def clear(self):
        """
        Remove all elements from the list. The result is empty list.
        Sets self.length property as 0.
        """
        for item in self:
            self.remove_by_value(item.value)
        self.length = 0
