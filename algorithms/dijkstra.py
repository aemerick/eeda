"""
A very rough implementation of Dijkstras shortest path
algorithm just for practice sake:


1) Create a set (sptSet) keeping track of vertices in shortest path tree
2) Assign distance values to all vertices in input graph. Initialize as INF.
   Assign source as 0
3) While sptSet doesn't include all vertices:
   a) Pick a vertex "u" NOT in sptSet AND has a minimum distance value
   b) Add "u" to sptSet
   c) Update distance value of all adjacent vertices if "u". To update, iterate
      through all adjacent vertices. FOr every adj ("v") if sum of distance value
      of "u" (from source) and weight of edge u-v is < ditance value of "v",
      update distance value of "v". (ahh ok ... works cause all init to INF)

"""

import sys
import copy

_MAX_INT = sys.maxsize

class Graph():

    def __init__(self, num_vertices):

        self.num_vertices = num_vertices
        self.adj = [[0 for column in range(self.num_vertices)] for row in range(self.num_vertices)]

        return


    def minDistance(self, dist, sptSet):
        """
        Find the vertex of
        """

        mindist   = _MAX_INT
        min_index = None

        for v in range(self.num_vertices):

            if (dist[v] < mindist) and (sptSet[v] == False):
                mindist   = dist[v]
                min_index = v

        if min_index is None:
            print("Cannot find minimum distance. Something is wrong.")
            raise RuntimeError

        return min_index


def dijkstra(G, source, return_paths = False):
    """
    An implementation of the dijkstra shortest path algorithm that
    finds the shortest paths from source to all nodes.

    Implemented in O(V^2)!
    """


    dist         = [_MAX_INT] * G.num_vertices # initialized distance array
    dist[source] = 0
    sptSet       = [False] * G.num_vertices

    paths        = None
    if return_paths:
        paths = [[] for x in range(G.num_vertices)]

    #
    # the shortest path matrix
    #

    while not all(sptSet):

        # Pick the minimum distance vertex from the set
        # of vertices NOT currently processed.
        # in the first iteration, this returns the source
        # (step a of alg loop)
        u = G.minDistance(dist, sptSet)

        # (step b of alg loop) set the spt set to true
        sptSet[u] = True

        # Now loop through the dista value of all adjacent vertices
        # from u. If the current known distance is > the new distance,
        # update current distance with the new distance
        # (step c of alg loop)
        for v in range(G.num_vertices):
            if (G.adj[u][v] > 0) and (not sptSet[v]) and\
               (dist[v] > dist[u] + G.adj[u][v]):

                dist[v]  = dist[u] + G.adj[u][v]

                if return_paths:
                    paths[v].extend(paths[u] + [v])

    if not (all(sptSet)):
        print("All vertices not in sptSet")
        print(sptSet)
        raise RuntimeError

    if return_paths:
        print(paths)
        for u in range(G.num_vertices):
            if len(paths[u]) == 0:
                paths[u].append(u)
            elif paths[u][-1] != u:
                paths[u].append(u)

            if paths[u][0] != source:
                paths[u].insert(0,source)

        print(paths)
        """
        for u in range(G.num_vertices):
            pathsincomplete = True
            count = 0
            while pathsincomplete and count < 2:
                pathsincomplete = False

                for i in range(1,len(paths[u])):
                    v,w = paths[u][i], paths[u][i-1]
                    print(paths)
                    if G.adj[v][w] == 0:
                        paths[u] = paths[u][:i] +\
                                   (paths[w][1:-1])+\
                                   paths[u][i:]
                        pathsincomplete = True
                count = count + 1
        """
        return dist, paths
    else:
        return dist


def printsolution(G, source, dist, paths = None):

    if paths is None:
        print("Dijkstra solution from source %i"%(source))
        print("Vertex \t Distance from Source")
        for n in range(G.num_vertices):
            print(n, "\t", dist[n])
    else:
        print("Dijkstra solution from source %i"%(source))
        print("Vertex \t Distance \tPath")
        for n in range(G.num_vertices):
            print(n, "\t", dist[n], "\t\t", end="")

            for v in paths[n]:
                print(v,end="\t")

            print("\n")

    return

def test():
    """
    A test graph
    """

    G     = Graph(9)
    G.adj = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
        ];

    source = 0
    dist   = dijkstra(G, source)
    printsolution(G, source, dist)

    print("----------------- with path -------------------")

    source = 0
    dist, path = dijkstra(G, source, return_paths=True)
    printsolution(G, source, dist, path)

    return

if __name__ == "__main__":

    test()
