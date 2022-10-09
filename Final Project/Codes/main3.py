import json
import time
from itertools import combinations
from tabulate import tabulate
import pandas as pd
import numpy as np
from geocoding import geocodeThis, findDistance

#defining the location of stores with it's coordinate
addressCoorlist=[['Hartamas 1, Sri Hartamas, Kuala Lumpur ', 101.6566987, 3.1640273],
            ['Jalan Kelang Lama Kuala Lumpur', 101.6620276, 3.083534],
            ['Jalan Imbi,  1st Avenue, Kuala Lumpur', 101.71169, 3.1433042],
            ['Lebuh Bandar Utama Kuala Lumpur', 101.6068183655304, 3.1362848000000003],
            ['Jalan Telawi 1, Bangsar Baru', 101.6720542, 3.1299663],
            ['KL Sentral, Arrival Hall', 101.6868207, 3.1341423],
            ['Jalan Ampang Kuala Lumpur', 101.7496258, 3.1577259]]

# do combination of 2 address (5C2) to get every possible route
item=combinations(addressCoorlist, 2)
routlist=list(item)

#loop through every possible rout to plot the route on the map and get the distant
routemap={}
routelist2=[]
for i in routlist:
    distributioncenter1=i[0][0]
    distributioncenter2 = i[1][0]
    data=findDistance(i[0][1],i[0][2],i[1][1],i[1][2])
    distant=float(data[1])

    #apped the data of places andd the distant
    routelist2.append([distributioncenter1, distributioncenter2, distant])

    #save the map plot into html
    data[0].save(f'{i[0][0]} to {i[1][0]} {distant}km.html')

    #sleep the program for 10 sec to counter api request rate limit
    time.sleep(10)

    if distributioncenter1 not in routemap:
        routemap[distributioncenter1]=[]
    routemap[distributioncenter1].append([distributioncenter2,distant])
    if distributioncenter2 not in routemap:
        routemap[distributioncenter2]=[]
    routemap[distributioncenter2].append([distributioncenter1,distant])

#print the data to copy for the min span algo
# print(routelist2)

#safe route data in jason file
# with open('routemap.json', 'w') as fp:
#     json.dump(routemap, fp)

# print(json.dumps(routemap, indent=4, sort_keys=True))

#for every possible distribution center find its total distant to every other location
arr=[]
for i in routemap.keys():
    k=0
    for j in routemap[i]:
        k+=float(j[1])
    arr.append([i,k])

print(tabulate(arr,headers=["Distribution Center","Total Distance"]))



























