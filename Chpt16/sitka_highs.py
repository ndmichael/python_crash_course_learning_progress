from pathlib import Path
import csv


path = Path("weather_data/sitka_weather_2021_simple.csv")
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

highs = []
for row in reader:
    high = int(row[4])
    highs.append(high)

print(highs)
# for index, column_header in enumerate(header_row, start=1):
#     print(f"{index}: {column_header}")