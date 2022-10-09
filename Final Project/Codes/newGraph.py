import sys

#defining class route
class Route:
    def __init__(self, initialLocation, destinationLocation, Distance,dictionary):
        self.initialLocation = initialLocation
        self.destinationLocation = destinationLocation
        self.distance = Distance
        self.dictionary=dictionary

    def __str__(self):
        location1=self.dictionary[self.initialLocation]
        location2= self.dictionary[self.destinationLocation]
        return location1 + "--" + str(self.distance) + "-->" +location2

#defining minspan function
def minspan(distributioncenter,graph,distributionCenterList):
    distributionCenter=distributioncenter
    prevLocation=[]
    routeList=[]


    #findpath function are used to find and explore route with the minimum cost
    #it uses the Depth first search method but sorted the next route to explore by the cost
    #This is because we assume theres only one distributor will move through out the graph
    def findpath(current,graph,prevlocation):
        #Initializing the cost for min as max value
        min = sys.maxsize
        nextLocation=None

        #if the path haven't explore all the vertices; find the next edge with the lowest cost that will lead to vertices that havent been discovered
        if len(prevlocation) != len(graph):
            for i in range(len(graph[current])):
                if graph[current][i] < min and i not in prevLocation and graph[current][i]!=0:
                    min = graph[current][i]
                    # print(min)
                    nextLocation = i

            prevlocation.append(current)
            if len(prevlocation) < len(graph):
                routeList.append(Route(current,nextLocation,min,distributionCenterList))
            m=findpath(nextLocation, graph, prevlocation)
        return prevLocation




    findpath(distributionCenter,graph,prevLocation)
    totalDistance=0
    for x in routeList:
        print(x)
        totalDistance+=x.distance

    return (routeList,totalDistance)
