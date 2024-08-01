from pathlib import Path
import json

#Read data as a string and convert to a python object
path = Path("eq_data/eq_data_1_day_m1.geojson")
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)

#Read all data from the dataset
all_eq_dicts = all_eq_data['features']

#Read mag properties
mags = []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    mags.append(mag)

print(mags[:10])
print(len(all_eq_dicts))

#Create a more readable versions of the data file
path = Path("eq_data/readable_eq_data.geojson")
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)



