from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # if storage.length is not capacity
            # add to tail
            # self.current = storage.head
        if self.storage.length != self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.head
        # else
            # replace current node with item
            # self.current = self.current.next
        else:
            next_node = self.storage.head
            prev_node = self.storage.tail
            while next_node is not prev_node or next_node is not prev_node.prev:
                if next_node == self.current:
                    next_node.value = item
                    if self.current.next is None:
                        self.current = self.storage.head
                    else:
                        self.current = self.current.next
                    return

                if prev_node == self.current:
                    prev_node.value = item
                    if self.current.next is None:
                        self.current = self.storage.head
                    else:
                        self.current = self.current.next
                    return

                next_node = next_node.next
                prev_node = prev_node.prev


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        current = self.storage.head

        while current is not None:
            list_buffer_contents.append(current.value)
            current = current.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
