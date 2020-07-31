"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

from collections import deque


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:  # if current value equal to target then return true
            return True
        if target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        else:
            if not self.right:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree

    # def get_max(self):
    #     current = self
    #     while current.right is not None:
    #         current = current.right

    #     return current.value
    def get_max(self):
        # current = self

        while self.right is not None:
            return self.right.get_max()

        return self.value
    # Call the function `fn` on the value of each node

    def for_each(self, fn):
        # call the anonymous func on self.valur
        fn(self.value)

        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    def iterative_depth_first_for_each(self, fn):
        # DFT: LIFO
        # we'll use a stack
        stack = []
        stack.append(self)

        # so long as our stack has nodes in it
        # there's more nodes to traverse
        while len(stack) > 0:
            current = stack.pop()
            # right to left order
            # add the current niode's right child first
            if current.right:
                stack.append(current.right)
            # add the current niode's left child
            if current.left:
                stack.append(current.left)
            # call the anonymous func.
            fn(current.value)

    def iterative_breadth_first_for_each(self, fn):
        from collections import deque
        # BFT: FIFO
        # we'll use a queue
        #
        queue = deque()
        queue.append(self)
        while len(queue) > 0:
            current = queue.popleft()

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

            fn(current.value)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self):
        if not self:
            return
        # left -> root -> right
        if self.left:
            self.left.in_order_print()

        print(self.value)

        if self.right:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self):

        # 1. define deque
        # 2. add self to deque
        # 3. iterate: while there are items in the deque
        # 4. dequeue/pop from deque, point to result, and print
        # 5. add left and right children to deque
        qq = deque()
        qq.append(self)
        while len(qq) > 0:
            current = qq.popleft()
            print(current.value)

            if current.left:
                qq.append(current.left)

            if current.right:
                qq.append(current.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self):

        s = []
        s.append(self)

        while len(s) > 0:
            current = s.pop()
            print(current.value)
            if current.left:
                s.append(current.left)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass


"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
print("post order")
bst.post_order_dft()
