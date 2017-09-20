from Graph import *

if __name__ == '__main__':
    myGraph = Graph("People")
    myGraph.fromCSV("rooster_teeth_Nodes.csv", "rooster_teeth_Edges.csv")

    print(myGraph.toString() )

    print("\n==================================================================\n\t\t\t== BFS of the Graph ==\n==================================================================\n")
    bfsNodes, bfsString = myGraph.breadthFirstSearch(150672761669948)

    for node, i in zip(bfsNodes, bfsString):
        tab = "  " * node.level
        print(tab + i)

    print("\n==================================================================\n\t\t\t== DFS of the Graph ==\n==================================================================\n")
    dfsNodes, dfsString = myGraph.depthFirstSearch(150672761669948)
    for node, i in zip(dfsNodes, dfsString):
        tab = "  " * node.level
        print(tab + i)
    del myGraph
