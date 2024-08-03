from pathlib import Path
import json
import plotly.express as px

#Read data as a string and convert to a python object
path = Path("eq_data/eq_data_30_day_m1.geojson")
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)

#Read all data from the dataset
all_eq_dicts = all_eq_data['features']

#Read mag properties
mags, lons, lats, eq_titles = [], [], [], []

for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    title = eq_dict["properties"]['title']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    eq_titles.append(title)
    lons.append(lon)
    lats.append(lat)

# print(mags[:10])
# print(lons[:10])
# print(lats[:10])
# print(len(all_eq_dicts))

title = "Global Earthquakes"
fig = px.scatter_geo(
    lat=lats, lon=lons, size=mags, title=title,
    color=mags,
    color_continuous_scale='Viridis',
    labels={'color': 'Magnitude'},
    projection='natural earth1',
    hover_name= eq_titles,

)
fig.show()
#Create a more readable versions of the data file
path = Path("eq_data/readable_eq_data.geojson")
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)



