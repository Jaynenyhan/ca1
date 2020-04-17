#!/usr/bin/env python3

# Priority Queue
class PQ(object):

    # d = dict where we store nodes, n = count of total nodes
    def __init__(self):
        self.d = {}
        self.n = 0

    # is empty
    def is_empty(self):
        return self.size() == 0

    # return size
    def size(self):
        return self.n

    # swap nodes i and j
    def swap(self, i, j):
        self.d[i], self.d[j] = self.d[j], self.d[i]

    # insert node
    def insert(self, node):
        self.n += 1
        self.d[self.n] = node
        # swim new node at index n to find correct pos
        self.swim(self.n)

    # node swims up the heap to correct pos
    def swim(self, node):
        # while not at root node and parent is smaller than child
        # node//2 == parent
        while node > 1 and self.d[node // 2] < self.d[node]:
            self.swap(node, node // 2)
            node = node // 2

    # return bigger of nodes i and j
    def bigger(self, i, j):
        try:
            return max([i, j], key=self.d.__getitem__)
        except KeyError:
            return i

    # return max node
    def getMax(self):
        return self.d[1]

    # remove max node
    def delMax(self):
        node = self.d[1]
        # move root to end
        self.swap(1, self.n)
        # delete it
        del(self.d[self.n])
        # decrease node count
        self.n -= 1
        # sink the root node to find correct pos
        self.sink(1)
        return node

    # node sinks down the heap to the correct pos
    def sink(self, node):
        # while there is a child
        while node * 2 <= self.n:
            # j = left child, j + 1 = right child
            j = node * 2
            # select bigger child
            big = self.bigger(j, j + 1)
            # if node is bigger than the biggest child, we're done
            if self.d[node] >= self.d[big]:
                break
            # else, swap with biggest child
            self.swap(node, big)
            # change node index to the new pos
            node = big
