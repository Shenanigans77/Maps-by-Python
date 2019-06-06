import folium
import os
import pandas

current_dir = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(current_dir, os.path.realpath("data/Volcanoes_USA.txt"))
data = pandas.read_csv(open(filename))

# Instantiate map centered at the center of the dataset's coordinates
map = folium.Map(location=[data['LAT'].mean(),data['LON'].mean()],zoom_start=12,tiles='Stamen Terrain')

def marker_color(elevation):
    minimum = int(min(data['ELEV']))
    step = int((max(data['ELEV'])-min(data['ELEV']))/3)
    if elevation in range(minimum,minimum+step):
    	color = 'green'
    elif elevation in range(minimum+step,minimum+step*2):
    	color = 'orange' 
    else:
    	color = 'red'
    return color

for lat,lon,name,elev in zip(data['LAT'],data['LON'],data['NAME'],data['ELEV']):   	
    folium.Marker([lat, lon],popup=name,icon=folium.Icon(color=marker_color(elev))).add_to(map)

map.save('test.html')