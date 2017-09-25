from collections import defaultdict

class Node:
    def __init__(self, children=[], number=0):
        self.number = number
        self.children = {}
        for c in children:
            self.children[c] = Node(number=self.number + len(c))
        self.pointer = None

    def add(self, child):
        c = Node(number=self.number + len(child))
        self.children[child] = c
        return c

    def print_from_here(self, depth=0):
        if len(self.children) == 0:
            print depth * '\t' + 'Leaf'
        else:
            print depth * '\t' + 'Internal. Edges:'
            for ss, n in self.children.items():
                print depth * '\t' + '\t{}'.format(ss)
                n.print_from_here(depth + 1)

    def extend(self, ss):
        if len(ss) == 0:
            return
        for edge in self.children:
            if len(edge) == 0:
                continue
            if edge[0] == ss[0]:
                for i, ch in enumerate(ss):
                    if i >= len(edge):
                        # end of edge: is this a leaf?
                        if len(self.children[edge].children) == 0:
                            self.children[edge + ch] = self.children[edge]
                            del self.children[edge]
                            return
                        else:
                            return self.children[edge].extend(ss[i:])
                    elif ch != edge[i]:
                        # need to split
                        split = self.children[edge[:i]] = Node(children=[edge[i:], ss[i:]])
                        # for k, v in self.children.items():
                        #     if len(k) > i:
                        #         split.children[k[i:]] = v
                        #         del self.children[k]
                        del self.children[edge]
                        return
                # if len(ss) < len(edge):
                #     self.split_edge(edge, ss, i + 1)
                return
        self.children[ss] = Node()


    def split_edge(self, edge_label, new_edge, split_point):
        split = self.children[edge_label[:split_point]] = \
            Node(children=[edge_label[split_point:], new_edge[split_point:]])
        del self.children[edge_label]
        # for k, v in self.children.items():
        #     if len(k) > split_point:
        #         split.children[k[split_point:]] = v
        #         del self.children[k]



def makeTree(s):
    if len(s) == 0:
        return None
    root = Node('')
    for i, ch in enumerate(s):
        # begin phase i
        for j in range(i + 1):
            # begin extension j
            root.extend(s[j:i + 1])
    return root




r = makeTree('axabx')
r.print_from_here()