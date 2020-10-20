#
#
# Ok but what are binary trees
#



class Node:

    def __init__(self, key : int,
                       data : dict = {}
                 ):
        self.left  = None
        self.right = None
        self.key   = key   # id identifier
        self.data  = data

        return
