import pandas as pd
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

# Read the data from the CSV files that lie next to this script using the absolute path
data1 = pd.read_csv('task1/CompanyCustomers.csv')
data2 = pd.read_csv('task1/PrivateCustomers.csv')

# Get the unique countries from the data and add each to a set
unique_countries1 = set(data1['Country'])
unique_countries2 = set(data2['Country'])

# Combine the unique countries from both datasets and remove duplicates
unique_countries = unique_countries1.union(unique_countries2)


capitals = ['Stockholm', 'Oslo', 'Bern', 'Brasilia', 'Paris', 'Vienna', 'Tokyo', 'Copenhagen', 'Canberra', 'Rome', 'Brussels', 'Helsinki', 'Amsterdam', 'Wellington', 'Ottawa', 'Madrid', 'Beijing', 'Berlin', 'London', 'Seoul', 'Dublin']

# Initialize the geolocator with a valid user agent
geolocator = Nominatim(user_agent="thisisanexampleuseragent")

# Function to get the latitude and longitude of a capital
def get_lat_lon(city):
    print(city)
    location = geolocator.geocode(city)
    return (location.latitude, location.longitude)

# Dictionary to store the latitude and longitude of each capital
capitals_coords = {}

for capital in capitals:
    coords = get_lat_lon(capital)
    capitals_coords[capital] = coords

# For each of the unique capitals, find the distance between each of them
distances = []

max_distance = 0

for capital1 in capitals:
    for capital2 in capitals:
        if capital1 != capital2:
            distance = geodesic(capitals_coords[capital1], capitals_coords[capital2]).kilometers
            distances.append(distance)
            if distance > max_distance:
                max_distance = distance

print(f"The maximum distance between two capitals is {max_distance:.2f} kilometers.")

# Find the distance between the northernmost and the southernmost capitals
for capital in capitals:
    if 'northernmost' not in locals() or capitals_coords[capital][0] > northernmost[0]:
        northernmost = capitals_coords[capital]
    if 'southernmost' not in locals() or capitals_coords[capital][0] < southernmost[0]:
        southernmost = capitals_coords[capital]

distance = geodesic(northernmost, southernmost).kilometers
print(f"The distance between the northernmost and southernmost capitals is {distance:.2f} kilometers.")