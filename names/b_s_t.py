# sys.path.append('../queue_and_stack')
# from dll_queue import Queue
# from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # compare to current node
        # if no node
            # make new node (left or right) 
        # if smaller, go left
        if value < self.value:
            if self.left is None:
                # insert tree node
                self.left = BinarySearchTree(value)
            else:
                # continue to left
                self.left.insert(value)
        # if bigger, go right
        elif value >= self.value:
            if self.right is None:
                # insert tree node
                self.right = BinarySearchTree(value)
            else:
                # continue right
                self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # compare to current node
        # if smaller, go left
        if target < self.value:
            # if smaller, but can't go left, return false
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        # if bigger, go right
        if target > self.value:
            # if bigger, but can't go right, return false
            if self.right is None:
                return False
            else:
                return self.right.contains(target)
        # if equal, return true
        if target == self.value:
            return True

    # Return the maximum value found in the tree
    def get_max(self):
        # traverse to the right until right equals None
        # return self.value
        while self.right is not None:
            self = self.right
        
        return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # perform cb on self.value
        cb(self.value)
        # if can go left, go left
        if self.left is not None:
            self.left.for_each(cb)
        # if can go right, go right
        if self.right is not None:
            self.right.for_each(cb)


    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # go left first
        if node.left is not None:
            node.in_order_print(node.left)
        
        print(node.value)

        if node.right is not None:
            node.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    # def bft_print(self, node):
        # create queue
        # storage = Queue()
        # push current value onto queue
        # storage.enqueue(node)
        # while queue is not empty

        # while storage.len() != 0:
            # pop node off queue
            # curr_node = storage.dequeue()
            # print node
            # print(curr_node.value)
            # push its children if we can
            # if curr_node.left:
                # storage.enqueue(curr_node.left)
            # if curr_node.right:
                # storage.enqueue(curr_node.right)
            

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    # def dft_print(self, node):
        # create node_stack
        # storage = Stack()
        # push current value onto stack
        # storage.push(node)
        # while items on stack
        # # while storage.len() != 0:
            # print the value and pop it off
            # curr_node = storage.pop()
            # print(curr_node.value)
            # push left value of current node if we can
            # if curr_node.left:
                # storage.push(curr_node.left)
            # push right value of current node if we can
            # if curr_node.right:
                # storage.push(curr_node.right)
            
            

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    # def pre_order_dft(self, node):
        # print node
        # print(node.value)
        # go left
        # if node.left is not None:
            # node.pre_order_dft(node.left)
        # go right
        # if node.right is not None:
            # node.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    # def post_order_dft(self, node):
        # go left
        # if node.left is not None:
            # node.post_order_dft(node.left)
        # go right
        # if node.right is not None:
            # node.post_order_dft(node.right)
        # print node
        # print(node.value)

# bst = BinarySearchTree(5)

# bst.insert(3)
# bst.insert(7)
# bst.insert(2)
# bst.insert(6)
# bst.insert(4)

# bst.pre_order_dft(bst)
# bst.post_order_dft(bst)