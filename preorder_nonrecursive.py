import copy


# void pre-traverse(Treenode P)
# Treenode-stack A;
# CLEAR(A);
#     while (true)
#         if (P != nil)
#             VISIT(P);
#             STACK(A,P);
#             P ← P.LLINK;
#         else
#             if (EMPTY(A))
#                 return;
#             else
#             P ← UNSTACK(A);
#             P ← P.RLINK;

class Node:
    def __init__(self, data=None, llink=None, rlink=None):
        self.data = data
        self.llink = llink
        self.rlink = rlink

    def get_llink(self):
        return self.llink

    def set_llink(self, x):
        self.llink = x

    def get_rlink(self):
        return self.rlink

    def set_rlink(self, x):
        self.rlink = x

    def get_data(self):
        return self.data

    def set_data(self, x):
        self.data = x


# Build the tree.
tree = Node('proj', Node('coul', Node('appe', None, None), Node('impr', Node('exte', None, None), Node('mini',Node('leng', Node('incl',None, None),(Node( 'list', Node('like',None,None),None))),Node('prac',None,  Node('prog', None,None))))), Node('ther', Node('stip', None, Node('text', None, None)), None))

# Pre-order traversal.
stack = []
p = copy.deepcopy(tree)
counter = 1
while True:
    if p != None:
        print(str(counter))
        print(f'Visit {p.get_data()}')
        print('Stack is:')
        for node in stack:
            print(node.get_data())
        stack.append(p)
        p = p.get_llink()
        counter += 1
    else:
        if len(stack) == 0:
            break
        else:
            p = stack.pop()
            p = p.get_rlink()
