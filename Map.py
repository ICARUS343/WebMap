import folium
import pandas


data = pandas.read_csv("Volcanoes_USA.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(el):
    if(el > 2500):
        return 'red'
    elif(2000 < el <2500):
        return 'blue'
    elif (1000 < el < 2000):
        return 'orange'
    else:
        return 'green'


map = folium.Map(location = [44.31916539, -110.02333324], zoom_start = 2 , tiles = "Mapbox Bright")

#AREA":44,"POP2005":83039,"REGION":19,"SUBREGION":29,
fgv = folium.FeatureGroup(name = "Volcano")
fgp = folium.FeatureGroup(name = "Population")
fga = folium.FeatureGroup(name = "area")




for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location = [lt,ln], radius = 6,
    popup = str(el)+" m", fill_color = color_producer(el),
    color = 'grey', fill = True,fill_opacity = 0.5 ))

fgp.add_child(folium.GeoJson(data = open('world.json', 'r', encoding = 'utf-8-sig').read(),
style_function = lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

fga.add_child(folium.GeoJson(data = open('world.json', 'r', encoding = 'utf-8-sig').read(),
style_function = lambda x: {'fillColor': 'orange' if x['properties']['AREA'] < 100000
else 'black'}))


map.add_child(fgv)
map.add_child(fgp)
map.add_child(fga)
map.add_child(folium.LayerControl())

map.save("Map1.html")
