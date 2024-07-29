import matplotlib.pyplot as plt
from pathlib import Path
import csv
from datetime import datetime as dt


path = Path("weather_data/sitka_weather_2021_full.csv")
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

dates, rainfalls = [], []

for row in reader:
    date = dt.strptime(row[2], '%Y-%m-%d')
    try:
        rainfall = float(row[5])
    except ValueError:
        print(f"missing for {date}")
    else:
        dates.append(date)
        rainfalls.append(rainfall)

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.bar(dates, rainfalls, color="navy")

ax.set_title("Death Valley Rainfalls")
ax.set_ylabel("Rainfalls")
ax.set_xlabel("Dates")


fig.autofmt_xdate()
ax.tick_params(axis="both", labelsize=10)

plt.show()

for index, row in enumerate(header_row):
    print(index, row)