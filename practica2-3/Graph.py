"""Node

"""
class Node(object):
    def __init__(self, id, name, pageRank = 0):
        self.id = id
        self.name = name
        self.adj = {}
        # Breadth First Search related information.
        self.level = 0
        # Page Rank related information.
        self.invAdj = {}
        self.connected = 0
        self.pageRank = pageRank

    def addConnection(self, node, cost):
        self.adj[node.id] = [cost, node]
        # Page Rank related information.
        node.invAdj[self.id] = self
        self.connected += 1

    def updatePageRank(self, d = 0.85):
        accum = 0
        for node in self.invAdj.values():
            accum += node.pageRank / node.connected
        self.pageRank = (1 - d) + (d) * accum

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
        startNode.level = 0
        resultString.append(str(startNode.level) + " " + startNode.name)
        while Q:
            current = Q.pop(0)
            for i in current.adj.values():
                if i[1] not in result:
                    i[1].level = current.level + 1
                    result.append(i[1])
                    Q.append(i[1])
                    resultString.append(str(i[1].level) + " " + i[1].name)
        return result, resultString

    def depthFirstSearch(self, startId):
        startNode = self.nodes[startId]
        result = []
        resultString = []
        S = []
        S.append(startNode)
        startNode.level = 0
        while S:
            current = S.pop()
            if(current not in result):
                result.append(current)
                resultString.append(str(current.level) + " " + current.name)
            for i in current.adj.values():
                if i[1] not in result:
                    i[1].level = current.level + 1
                    S.append(i[1])
        return result, resultString

    def pageRank(self, iterations = 0):
        keys = self.nodes.keys()
        for _ in range(iterations):
            for key in keys:
                self.nodes[key].updatePageRank(d=0.85)
        pageRankDictionary = {}
        for key in keys:
            pageRankDictionary[self.nodes[key].name] = self.nodes[key].pageRank
        keyValue = zip(pageRankDictionary.keys(), pageRankDictionary.values())
        return dict(sorted(keyValue, key = lambda x: x[1], reverse=True))

    def toString(self):
        string = ""
        for i in self.nodes.values():
            string += "\n" + i.toString()
        return self.name + " of size: " + str(self.size) + " with Nodes: " + string

    def fromCSV(self, pathToNodes, pathToEdges):
        """
        Alias: "JavaIn2017LUL"
        """
        import pandas as pd
        csvNodes = pd.read_csv(pathToNodes)
        for i, row in csvNodes.iterrows():
            self.insertNode(Node(row['id'], row['label']))
        csvEdges = pd.read_csv(pathToEdges)
        for i, row in csvEdges.iterrows():
            self.nodes[row['Source']].addConnection(self.nodes[row['Target']], 1)
