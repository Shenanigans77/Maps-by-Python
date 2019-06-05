import folium
import os
import pandas

current_dir = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(current_dir, os.path.realpath("data/Volcanoes_USA.txt"))
data = pandas.read_csv(open(filename))

map = folium.Map(location=[45.372, -121.697],zoom_start=12,tiles='Stamen Terrain')

def marker_color(elevation):
    if elevation in range(0,1000):
    	color = 'green'
    elif elevation in range(1000,3000):
    	color = 'orange' 
    else:
    	color = 'red'
    return color

for lat,lon,name,elev in zip(data['LAT'],data['LON'],data['NAME'],data['ELEV']):   	
    folium.Marker([lat, lon],popup=name,icon=folium.Icon(color=marker_color(elev))).add_to(map)

map.save('test.html')