from pathlib import Path
import csv
from matplotlib import pyplot as plt


path = Path("weather_data/sitka_weather_2021_simple.csv")
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

highs = []
for row in reader:
    high = int(row[4])
    highs.append(high)


#Plot the highs and lows temperature
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(highs, color="red")

ax.set_title("Daily high temperatures, July 2021", fontweight="bold", fontsize="20")
ax.set_xlabel("", fontsize="16")
ax.set_ylabel("Temperature (F)", fontsize="16")

ax.tick_params(axis="both", labelsize=20)

plt.show()

# for index, column_header in enumerate(header_row, start=1):
#     print(f"{index}: {column_header}")