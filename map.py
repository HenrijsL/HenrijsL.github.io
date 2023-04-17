import folium
import gpxpy
import os

gpxFiles = [
    {
        "name": "Gulbenes novads",
        "file": "GulbenesNovads38.gpx",
        "color": "red",
        "gpx_url": "https://drive.google.com/drive/folders/1N5Bd9Tcw8mtJYNsPFkSWXipClJpBkKHs?usp=sharing"
    },
    {
        "file": "GulbenesNovads30.gpx",
        "color": "orange"
    },
    {
        "name": "Valmieras novads",
        "file": "ValmieraNovads32.gpx",
        "color": "red",
        "gpx_url": "https://drive.google.com/drive/folders/1Dh836LENrAnS0BU7f3A0ikqYYFjoRrYl?usp=sharing"
    },
    {
        "file": "ValmieraNovads25.gpx",
        "color": "orange"
    },
]

def process_gpx_to_df(file_name):
    gpx = gpxpy.parse(open(file_name)) 
    
    points = []
    for track in gpx.tracks:
        for segment in track.segments:        
            for point in segment.points:
                points.append(tuple([point.latitude, point.longitude]))
    
    return points

map = folium.Map(location=(56.9, 24.5), zoom_start=8)

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

for gpx in gpxFiles:
    points = process_gpx_to_df(os.path.join(__location__, "gpx/" + gpx["file"]))
    folium.PolyLine(points, color=gpx["color"], weight=4.5, opacity=1).add_to(map)

    if "name" in gpx and "gpx_url" in gpx:
        html = "<div><h5>" + gpx["name"] + "</h5><a href='" + gpx["gpx_url"] + "' target='_blank'>GPX faili</a></div>"
        popup = folium.Popup(html, max_width=300)
        tooltip = "<h6>" + gpx["name"] + "</h6>"
        folium.Marker(points[0], tooltip=tooltip,popup=popup,icon=folium.Icon(color='green', icon='circle', icon_color='white', prefix='fa')).add_to(map)

map.save(os.path.join(__location__, "izskrien_latvijas_novadus.html"))