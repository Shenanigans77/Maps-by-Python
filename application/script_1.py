import folium
import os
import pandas

current_dir = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(current_dir, os.path.realpath("data/Volcanoes_USA.txt"))
data = pandas.read_csv(open(filename))

map = folium.Map(location=[45.372, -121.697],zoom_start=12,tiles='Stamen Terrain')

for lat,lon,name in zip(data['LAT'], data['LON'],data['NAME']):
    folium.Marker(
        [lat, lon],
        popup=name
        ).add_to(map)


map.save('test.html')