from Graph import *

if __name__ == '__main__':
    myGraph = Graph("People")
    myGraph.fromCSV("rooster_teeth_Nodes.csv", "rooster_teeth_Edges.csv")

    print(myGraph.toString() )

    print("\n==================================================================\n\t\t\t== BFS of the Graph ==\n==================================================================\n")
    bfsLevel, bfsString = myGraph.breadthFirstSearch(150672761669948)

    for i in bfsString:
        print(i)
    for i in bfsLevel:
        print(i)

    del myGraph
