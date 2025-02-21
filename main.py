import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="urllib3")

import pandas as pd
import folium

# Load the road data from CSV
roads = pd.read_csv("roads_sample.csv")

# Create a map centered around the first road's starting point
m = folium.Map(location=[roads["Start_Lat"][0], roads["Start_Lon"][0]], zoom_start=14)

# Loop through the roads data to create a line for each road
for _, row in roads.iterrows():
    folium.PolyLine(
        [(row["Start_Lat"], row["Start_Lon"]), (row["End_Lat"], row["End_Lon"])],
        color="blue" if row["Road_Type"] == "Highway" else "green",
        weight=5,
        tooltip=f"{row['Name']} ({row['Road_Type']})"
    ).add_to(m)

# Save the map to an HTML file
m.save("transportation_map.html")
