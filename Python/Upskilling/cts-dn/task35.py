coordinates = (10, 20)
def print_coordinates(coords):
    if not isinstance(coords, tuple):
        print("Input should be a tuple")
        return
    lat, long = coords
    print(f"Latitude: {lat}, Longitude: {long}")
print_coordinates(coordinates)