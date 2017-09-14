"""Node

"""
class Node(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.adj = {}

    def addConnection(self, node, cost):
        self.adj[node.id] = [cost, node]

    def toString(self):
        string = str(self.id) + ", " + self.name + ":"
        for i in self.adj.values():
            string += "\n\t(" + str(i[1].id) + ", " + i[1].name + ", cost: " + str(i[0]) + ")"
        return string

"""Graph

"""
class Graph (object):
    def __init__(self, name="Graph"):
        self.name = name
        self.size = 0
        self.nodes = {}

    def insertNode(self, node):
        self.nodes[node.id] = node
        self.size += 1

    def breadthFirstSearch(self, startId):
        startNode = self.nodes[startId]
        result = []
        resultString = []
        Q = []
        result.append(startNode)
        Q.append(startNode)
        level = 0
        resultString.append(str(level) + " " + startNode.name)
        while Q:
            current = Q.pop(0)
            level += 1
            for i in current.adj.values():
                if i[1] not in result:
                    result.append(i[1])
                    Q.append(i[1])
                    resultString.append(str(level) + " " + i[1].name)
        return result, resultString

    def toString(self):
        string = ""
        for i in self.nodes.values():
            string += "\n" + i.toString()
        return self.name + " of size: " + str(self.size) + " with Nodes: " + string

    def fromCSV(self, pathToNodes, pathToEdges):
        """
        Alias: "JavaIn2017LULMermesSeLaCome"
        """
        import pandas as pd
        csvNodes = pd.read_csv(pathToNodes)
        for i, row in csvNodes.iterrows():
            self.insertNode(Node(row['id'], row['label']))
        csvEdges = pd.read_csv(pathToEdges)
        for i, row in csvEdges.iterrows():
            self.nodes[row['Source']].addConnection(self.nodes[row['Target']], 1)
