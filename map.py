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
    {
        "name": "Tukuma novads",
        "file": "TukumaNovads35.gpx",
        "color": "red",
        "gpx_url": "https://drive.google.com/drive/folders/1vnCrKQyn5GcmnsYKpNUdQLO9SJWDJbZA?usp=sharing"
    },
    {
        "file": "TukumaNovads27.gpx",
        "color": "orange"
    },
    {
        "name": "Limbažu novads",
        "file": "LimbazuNovads34.gpx",
        "color": "red",
        "gpx_url": "https://drive.google.com/drive/folders/1c4WqRQSGvLVMPSEJ3y2CUz0CgyG4Gbvm?usp=sharing"
    },
    {
        "file": "LimbazuNovads28.gpx",
        "color": "orange"
    },
    {
        "name": "Bauskas novads",
        "file": "BauskasNovads35.gpx",
        "color": "red",
        "gpx_url": "https://drive.google.com/drive/folders/1PQh8eih2pCgpUWpF-OA6N6J8g9Gt_viH?usp=sharing"
    },
    {
        "file": "BauskasNovads24.gpx",
        "color": "orange"
    },
    {
        "name": "Mārupes novads",
        "file": "MarupesNovads32.gpx",
        "color": "red",
        "gpx_url": "https://drive.google.com/drive/folders/1e_ir0mFYS0ngU-bJDhErtWMoU10WNMWB?usp=sharing"
    },
    {
        "file": "MarupesNovads22.gpx",
        "color": "orange"
    },
    {
        "name": "Jelgava",
        "file": "Jelgava22.gpx",
        "color": "red",
        "gpx_url": "https://drive.google.com/drive/folders/1SWh3PFD-ljJqOaQUEZgy4lc3HaIr5jWS?usp=sharing"
    },
    {
        "file": "Jelgava14.gpx",
        "color": "orange"
    },
    {
        "name": "Salaspils novads",
        "file": "SalaspilsNovads27.gpx",
        "color": "red",
        "gpx_url": "https://drive.google.com/drive/folders/1Wn0YGf0pwEF4wZNWJU6Ekbv78IqILAJ1?usp=sharing"
    },
    {
        "file": "SalaspilsNovads18.gpx",
        "color": "orange"
    },
    {
        "name": "Ropažu novads",
        "file": "RopazuNovads30.gpx",
        "color": "red",
        "gpx_url": "https://drive.google.com/drive/folders/1xHNU776wfjLf1F3z1BR1PapesAxiHdEk?usp=sharing"
    },
    {
        "file": "RopazuNovads18.gpx",
        "color": "orange"
    },
    {
        "name": "Jūrmala",
        "file": "JurmalaPlanotais23.gpx",
        "color": "red",
        "gpx_url": "https://drive.google.com/drive/folders/1IRUWyVSBc3QTgcyLY7JVI9apY7wtpGXg?usp=sharing",
        "description": "Pateicoties Latvijas ziemai tika veikts cits maršruts, veiktais maršruts ir dzeltenā krāsā."
    },
    {
        "file": "JurmalaPlanotais18.gpx",
        "color": "orange"
    },
        {
        "file": "JurmalaRealais22.gpx",
        "color": "yellow"
    },
    {
        "name": "Cēsu novads",
        "file": "CesuNovads31.gpx",
        "color": "red",
        "gpx_url": "https://drive.google.com/drive/folders/1U5bARpzS2TWvD97Qb2RBt-8IOCiElxED?usp=sharing"
    },
    {
        "name": "Rēzekne",
        "file": "Rezekne_25km.gpx",
        "color": "red",
        "gpx_url": "https://drive.google.com/drive/folders/1UJAi_m9I3XJ0Z7JmDvoDZHnzMLiXC7YI?usp=sharing"
    },
    {
        "file": "Rezekne_20km.gpx",
        "color": "orange"
    },
    {
        "file": "Rezekne_15km.gpx",
        "color": "yellow"
    },
    {
        "file": "33km_Rezeknes_novads_ILN.gpx",
        "color": "orange"
    },
    {
        "name": "Rēzeknes novads",
        "file": "37km_Rezeknes_novads_ILN.gpx",
        "color": "red",
        "gpx_url": "https://drive.google.com/drive/folders/1UJAi_m9I3XJ0Z7JmDvoDZHnzMLiXC7YI?usp=sharing"
    },
    {
        "file": "20km_Rezeknes_novads_ILN.gpx",
        "color": "yellow"
    },
    {
        "name": "Dobeles novads",
        "file": "ILN_Dobeles_novads_37km.gpx",
        "color": "red",
        "gpx_url": "https://drive.google.com/drive/folders/1FIKcqC45QMsZpah4lD4ag9pvqg8xRgzp?usp=sharing"
    },
    {
        "file": "ILN_Dobeles_novads_26km.gpx",
        "color": "orange"
    },
    {
        "file": "ILN_Dobeles_novads_10km.gpx",
        "color": "yellow"
    },
    {
        "name": "Valkas novads",
        "file": "ILN_Valkas_novads_35km.gpx",
        "color": "red",
        "gpx_url": "https://drive.google.com/drive/folders/1ZgUjN46jlWOrbawspFkVIgD37llCSvb6?usp=sharing"
    },
    {
        "file": "ILN_Valkas_novads_13km.gpx",
        "color": "orange"
    },
    {
        "file": "ILN_Valkas_novads_12km.gpx",
        "color": "yellow"
    },
    {
        "name": "Kuldīgas novads",
        "file": "ILN_Kuldīgas_novads_36km.gpx",
        "color": "red",
        "gpx_url": "https://drive.google.com/drive/folders/1C9CNFAyLtFux74XJbD8wd258qYOyqxC9?usp=sharing"
    },
    {
        "file": "ILN_Kuldīgas_novads_23km.gpx",
        "color": "orange"
    },
    {
        "name": "Ādažu novads",
        "file": "ILN_Adazu_novads_40km.gpx",
        "color": "red",
        "gpx_url": "https://drive.google.com/drive/folders/14BHiEzPtNgIbswpgpSwp2u6RKVy8x8cR?usp=sharing"
    },
    {
        "file": "ILN_Adazu_novads_25km.gpx",
        "color": "orange"
    },
    {
        "file": "ILN_Adazu_novads_16km.gpx",
        "color": "yellow"
    },
]

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def process_gpx_to_df(file_name):
    gpx = gpxpy.parse(open(file_name)) 
    
    points = []
    for track in gpx.tracks:
        for segment in track.segments:        
            for point in segment.points:
                points.append(tuple([point.latitude, point.longitude]))
    
    return points

map = folium.Map(location=(56.9, 24.5), zoom_start=8)

#with open(os.path.join(__location__, "novadi.geojson")) as f:
    #gj = json.load(f)
    
#folium.GeoJson(gj).add_to(map)

for gpx in gpxFiles:
    points = process_gpx_to_df(os.path.join(__location__, "gpx/" + gpx["file"]))
    folium.PolyLine(points, color=gpx["color"], weight=4.5, opacity=1).add_to(map)

    if "name" in gpx and "gpx_url" in gpx:
        description = f"<p>{gpx['description']}</p>" if "description" in gpx else ""
        html = f"<div><h5>{gpx['name']}</h5><a href='{gpx['gpx_url']}' target='_blank'>GPX faili</a>{description}</div>"
        popup = folium.Popup(html, max_width=300)
        tooltip = "<h6>" + gpx["name"] + "</h6>"
        folium.Marker(points[0], tooltip=tooltip,popup=popup,icon=folium.Icon(color='green', icon='circle', icon_color='white', prefix='fa')).add_to(map)

map.save(os.path.join(__location__, "izskrien_latvijas_novadus.html"))