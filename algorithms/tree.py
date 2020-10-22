#
#
# Ok but what are binary trees
#



#
#
#

"""

Binary Tree Notes:

  - Maximum number of nodes on level l is 2^l (root : l = 0)
  - Height is defined as the maximum number of nodes on a root-leaf path
  - max nodes is 2^h -1 (taking root height as 1, leaf as 0)
  - Min height : log_2(n+1)
  - Min levels : log_2(L) + 1 (L = num leaves)


  - Full Binary Tree: every node has 0 or 2 children
  - Complete : All levels are filled except last. Last level is left justified.
  - Perfect : Complete on all levels.

  - Balanced: Height is O(log n)
"""


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

    def insert(self, key):
        """

        """

        if (self.root is None):
            self.root = Node(key)
            return

        q = []
        q.append(self.root)

        while(len(q)):
            temp = q[0]
            q.pop(0)

            if (not temp.left):
                


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
    bt.root.left.left  = Node(4)
    bt.root.left.right = Node(5)

    bt.root.left.left.left  = Node(6)
    bt.root.left.left.right = Node(7)

    '''4 becomes left child of 2
               1
           /       \
          2          3
        /   \       /  \
       4     5  None  None
      /  \
     6   7
    / \  / \
None None None None'''

    return bt
