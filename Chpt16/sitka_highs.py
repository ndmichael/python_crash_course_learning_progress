from pathlib import Path
import csv
from matplotlib import pyplot as plt
from datetime import datetime as dt


path = Path("weather_data/sitka_weather_2021_simple.csv")

lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

dates, highs, lows = [], [], []
for row in header_row:
    # print(row[0])
    date = dt.strptime(row[2], "%Y-%m-%d")
    high = int(row[4])
    low = int(row[5])
    dates.append(date)
    highs.append(high)
    lows.append(low)
    


#Plot the highs and lows temperature
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color="red", alpha=0.5)
ax.plot(dates, lows, color="seagreen", alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

ax.set_title("Daily high and low temperatures 2021", fontweight="bold", fontsize=24)
ax.set_xlabel("", fontsize="16")
ax.set_ylabel("Temperature (F)", fontsize="16")

fig.autofmt_xdate()

ax.tick_params(axis="both", labelsize=20)

plt.show()

# for index, column_header in enumerate(header_row, start=1):
#     print(f"{index}: {column_header}")