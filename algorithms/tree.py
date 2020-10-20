#
#
# Ok but what are binary trees
#



#
#
#

class BinaryTree:

    def __init__(self, key = None):
        """
        Binary Tree data type class implemented to enable
        insertion, deletion, and sort on a binary tree.
        """

        if key is None:
            self.root = None
        else:
            self.root = Node(key)

        return

    def set_root(self, key):
        """

        """

        if not (self.root is None):
            print("Cannot set root. Root already exists!")
            return

        self.root = Node(key)
        return

class Node:

    def __init__(self, key : int,
                       data : dict = {}
                 ):
        """
        An individual node in a binary tree. Described by
        an integer identifier and optional dictionary
        of data.

        Parameters:
        -----------
        key   :  (int)  Unique identifier
        data  :  (Optional, dict) Optional data dictionary
        """
        self.left  = None
        self.right = None
        self.key   = key   # id identifier
        self.data  = data

        return


def test_binary_tree():
    """
    Builds an example binary tree following along with the example in
    geeksforgeeks.org
    """

    # create root
    bt            = BinaryTree()
    bt.set_root(1)

    bt.root.left  = Node(2)
    bt.root.right = Node(3)

    # more:
    bt.root.left.left = Node(4)

    '''4 becomes left child of 2
               1
           /       \
          2          3
        /   \       /  \
       4    None  None  None
      /  \
    None None'''
