import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="urllib3")

import pandas as pd
import folium

# Load the road data from CSV
roads = pd.read_csv("roads_sample.csv")

# Create a map centered around the first road's starting point
m = folium.Map(location=[roads["Start_Lat"][0], roads["Start_Lon"][0]], zoom_start=14)

# Creating FeatureGroups for Highways and Local Roads
highway_layer = folium.FeatureGroup(name="Highways")
local_road_layer = folium.FeatureGroup(name="Local Roads")

# Step 2: Add roads to the respective layers based on road type
for index, row in roads.iterrows():
    # Check if the road is a "Highway" or "Local Road"
    if row["Road_Type"] == "Highway":
        folium.PolyLine(
            [(row["Start_Lat"], row["Start_Lon"]), (row["End_Lat"], row["End_Lon"])],
            color="blue",  # Highways are blue
            weight=5,      # Make highways thicker
            tooltip=f"{row['Name']} ({row['Road_Type']})"  # Show road name and type in tooltip
        ).add_to(highway_layer)
    else:
        folium.PolyLine(
            [(row["Start_Lat"], row["Start_Lon"]), (row["End_Lat"], row["End_Lon"])],
            color="green",  # Local roads are green
            weight=3,       # Make local roads thinner
            tooltip=f"{row['Name']} ({row['Road_Type']})"
        ).add_to(local_road_layer)


# Save the map to an HTML file
m.save("transportation_map.html")
