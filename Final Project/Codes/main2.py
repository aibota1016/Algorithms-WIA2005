from geocoding import geocodeThis

address=['Hartamas 1, Sri Hartamas, Kuala Lumpur ']

addressCoorlist=[]
for i in address:
    Coor=geocodeThis(i)
    addressCoorlist.append([i,Coor[0],Coor[1]])

print(addressCoorlist)

