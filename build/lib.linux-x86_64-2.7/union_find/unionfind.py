class UnionFind(object):
    """ Disjoint Set data structure supporting union and find operations used
    for Kruskal's MST algorithm 
    Methods - 
        insert(a, b) -> inserts 2 items in the sets
        get_leader(a) -> returns the leader(representative) corresponding to item a
        make_union(leadera, leaderb) -> unions two sets with leadera and leaderb
        in O(nlogn) time where n the number of elements in the data structure
        count_keys() -> returns the number of groups in the data structure
    """

    def __init__(self):
        self.leader = {}
        self.group = {}
        self.__repr__ = self.__str__

    def __str__(self):
        return str(self.group)

    def get_sets(self):
        """ returns a list of all the sets in the data structure"""
        return [i[1] for i in self.group.items()]

    def insert(self, a, b=None):
        """ takes a hash of object and inserts it in the
        data structure """

        leadera = self.get_leader(a)
        leaderb = self.get_leader(b)

        if not b:
            # only one item is inserted
            if a not in self.leader:
                # a is not already in any set
                self.leader[a] = a
                self.group[a] = set([a])
                return 

        if leadera is not None:
            if leaderb is not None:
                if leadera == leaderb: return # Do nothing
                self.make_union(leadera, leaderb)
            else:
                # leaderb is none
                self.group[leadera].add(b)
                self.leader[b] = leadera
        else:
            if leaderb is not None:
                # leadera is none
                self.group[leaderb].add(a)
                self.leader[a] = leaderb
            else:
                self.leader[a] = self.leader[b] = a
                self.group[a] = set([a, b])

    def get_leader(self, a):
        return self.leader.get(a)

    def count_groups(self):
        """ returns a count of the number of groups/sets in the
        data structure"""
        return len(self.group)

    def make_union(self, leadera, leaderb):
        """ takes union of two sets with leaders, leadera and leaderb
        in O(nlogn) time """
        if leadera not in self.group or leaderb not in self.group:
            raise Exception("Invalid leader specified leadera -%s, leaderb - %s" % (leadera, leaderb))
        groupa = self.group[leadera]
        groupb = self.group[leaderb]
        if len(groupa) < len(groupb):
            # swap a and b if a is a smaller set
            leadera, groupa, leaderb, groupb = leaderb, groupb, leadera, groupa
        groupa |= groupb # taking union of a with b
        del self.group[leaderb] # delete b
        for k in groupb:
            self.leader[k] = leadera

if __name__ == "__main__":
    uf = UnionFind()
    uf.insert("a", "b")
