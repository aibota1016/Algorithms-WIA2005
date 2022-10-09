import requests





def geocodeThis(address):
    url = "https://forward-reverse-geocoding.p.rapidapi.com/v1/forward"
    querystring = {"q": f"{address}", "accept-language": "en", "polygon_threshold": "0.0"}

    headers = {
        "X-RapidAPI-Host": "forward-reverse-geocoding.p.rapidapi.com",
        "X-RapidAPI-Key": "6c4b6bab23mshaa927ad6022961cp170e32jsn025a1defbb7a"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data=response.json()[0]

    return data["lon"],data["lat"]

# def findDistance(start_lat,start_lon,end_lat,end_lon):
#
#     url = "https://distance-calculator1.p.rapidapi.com/v1/getdistance"
#
#     querystring = {"start_lat": f"{start_lat}", "start_lng":  f"{start_lon}", "end_lat":  f"{end_lat}",
#                    "end_lng": f"{end_lon}", "unit": "kilometers"}
#
#     headers = {
#         "X-RapidAPI-Host": "distance-calculator1.p.rapidapi.com",
#         "X-RapidAPI-Key": "6c4b6bab23mshaa927ad6022961cp170e32jsn025a1defbb7a"
#     }
#
#     response = requests.request("GET", url, headers=headers, params=querystring)
#
#     return response.json()


# startloc=geocodeThis("Myeongji-Dong, Gangseo-Gu, 1 & 2F Busan KR")
# endloc=geocodeThis("Garak-Dong, Songpa-Gu, 1F")
#
# findDistance(startloc[0],startloc[1],endloc[0],endloc[1])


import openrouteservice
from openrouteservice import convert
import folium
import json


def findDistance(onelat, onelon, twolat, twolon):
    client = openrouteservice.Client(key='5b3ce3597851110001cf6248f917440de73241ee8921b468dc660327')

    coords = ((onelat, onelon), (twolat, twolon))
    res = client.directions(coords)
    geometry = client.directions(coords)['routes'][0]['geometry']
    decoded = convert.decode_polyline(geometry)
    distance_notes = str(round(res['routes'][0]['summary']['distance'] / 1000, 1))
    duration_notes = str(round(res['routes'][0]['summary']['duration'] / 60, 1))

    distance_txt = "<h4> <b>Distance :&nbsp" + "<strong>" + str(
        round(res['routes'][0]['summary']['distance'] / 1000, 1)) + " Km </strong>" + "</h4></b>"
    duration_txt = "<h4> <b>Duration :&nbsp" + "<strong>" + str(
        round(res['routes'][0]['summary']['duration'] / 60, 1)) + " Mins. </strong>" + "</h4></b>"

    m = folium.Map(location=[twolon, onelat], zoom_start=10, control_scale=True, tiles="cartodbpositron")
    folium.GeoJson(decoded).add_child(folium.Popup(distance_txt + duration_txt, max_width=300)).add_to(m)

    folium.Marker(
        location=list(coords[0][::-1]),
        popup="Galle fort",
        icon=folium.Icon(color="green"),
    ).add_to(m)

    folium.Marker(
        location=list(coords[1][::-1]),
        popup="Jungle beach",
        icon=folium.Icon(color="red"),
    ).add_to(m)
    return m, distance_notes, duration_notes

# m.save('map.html')

# data=findDistance(101.6566987,3.1640273,  101.6620276,3.083534)
#
# print(data[1])
#
# import folium
# from IPython.display import display
# # LDN_COORDINATES = (51.5074, 0.1278)
# # myMap = folium.Map(location=LDN_COORDINATES, zoom_start=12)
# display(data[0])