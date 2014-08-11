# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return
        stack = [node]
        table = {node:UndirectedGraphNode(node.label)}
        completed = set()
        while stack:
            t = stack[0]
            del stack[0]
            if t in completed:
                continue
            parent =table[t]
            neighbors = []
            for x in t.neighbors:
                stack.append(x)
                tmp = UndirectedGraphNode(x.label)
                neighbors.append(tmp)
                if x not in table:
                    table[x] = tmp
            parent.neighbors = neighbors            
            completed.add(t)
        return table[node]
        