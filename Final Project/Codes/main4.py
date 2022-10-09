

from pandas import DataFrame

from newGraph import minspan

#Declare every possible route with it's Distance
routes = [['Hartamas 1, Sri Hartamas, Kuala Lumpur ', 'Jalan Kelang Lama Kuala Lumpur', 13.6],
          ['Hartamas 1, Sri Hartamas, Kuala Lumpur ', 'Jalan Imbi,  1st Avenue, Kuala Lumpur', 10.9],
          ['Hartamas 1, Sri Hartamas, Kuala Lumpur ', 'Lebuh Bandar Utama Kuala Lumpur', 10.9],
          ['Hartamas 1, Sri Hartamas, Kuala Lumpur ', 'Jalan Telawi 1, Bangsar Baru', 8.8],
          ['Hartamas 1, Sri Hartamas, Kuala Lumpur ', 'KL Sentral, Arrival Hall', 7.9],
          ['Hartamas 1, Sri Hartamas, Kuala Lumpur ', 'Jalan Ampang Kuala Lumpur', 15.2],
          ['Jalan Kelang Lama Kuala Lumpur', 'Jalan Imbi,  1st Avenue, Kuala Lumpur', 11.5],
          ['Jalan Kelang Lama Kuala Lumpur', 'Lebuh Bandar Utama Kuala Lumpur', 14.4],
          ['Jalan Kelang Lama Kuala Lumpur', 'Jalan Telawi 1, Bangsar Baru', 6.9],
          ['Jalan Kelang Lama Kuala Lumpur', 'KL Sentral, Arrival Hall', 8.1],
          ['Jalan Kelang Lama Kuala Lumpur', 'Jalan Ampang Kuala Lumpur', 20.9],
          ['Jalan Imbi,  1st Avenue, Kuala Lumpur', 'Lebuh Bandar Utama Kuala Lumpur', 15.7],
          ['Jalan Imbi,  1st Avenue, Kuala Lumpur', 'Jalan Telawi 1, Bangsar Baru', 7.9],
          ['Jalan Imbi,  1st Avenue, Kuala Lumpur', 'KL Sentral, Arrival Hall', 4.8],
          ['Jalan Imbi,  1st Avenue, Kuala Lumpur', 'Jalan Ampang Kuala Lumpur', 10.7],
          ['Lebuh Bandar Utama Kuala Lumpur', 'Jalan Telawi 1, Bangsar Baru', 10.1],
          ['Lebuh Bandar Utama Kuala Lumpur', 'KL Sentral, Arrival Hall', 12.8],
          ['Lebuh Bandar Utama Kuala Lumpur', 'Jalan Ampang Kuala Lumpur', 23.1],
          ['Jalan Telawi 1, Bangsar Baru', 'KL Sentral, Arrival Hall', 3.8],
          ['Jalan Telawi 1, Bangsar Baru', 'Jalan Ampang Kuala Lumpur', 16.1],
          ['KL Sentral, Arrival Hall', 'Jalan Ampang Kuala Lumpur', 14.9]]
print()

# convert address to vertice that is identifiable by indeks
def encoding():
    distributionCenterList = []
    for i in range(len(routes)):
        if routes[i][0] not in distributionCenterList:
            distributionCenterList.append(routes[i][0])
        if routes[i][1] not in distributionCenterList:
            distributionCenterList.append(routes[i][1])
    return distributionCenterList
distributioncenterList = encoding()

#declare an empty adjacency matrix
routesadjcMatr = [[0] * (len(distributioncenterList)) for x in range(len(distributioncenterList))]

#input the distant data as weight in adjacency matrix
for i in range(len(routes)):
    j = distributioncenterList.index(routes[i][0])
    k = distributioncenterList.index(routes[i][1])
    routesadjcMatr[j][k] = routes[i][2]
    routesadjcMatr[k][j] = routes[i][2]
# print(DataFrame(routesadjcMatr))

#for every possible distribution center find the min span
#distribution center == the first vertices
for i in range(len(distributioncenterList)):
    print("DistributionCenter : "+ distributioncenterList[i])
    data=minspan(i,routesadjcMatr,distributioncenterList)
    print("total Distance : "+str(data[1]))
    print("\n")
