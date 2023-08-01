def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        data = [line.strip().split() for line in file]
        data = [(float(x), float(y)) for x, y in data]
    return data

def calculate_centroid(data):
    num_points = len(data)
    if num_points == 0:
        raise ValueError("No data points found.")

    sum_x = sum(y for x, y in data)
    sum_y = sum(x for x, y in data)

    centroid_x = sum_x / num_points
    centroid_y = sum_y / num_points

    return centroid_x, centroid_y

if __name__ == "__main__":
    file_path = "your_data_file.dat"  # Replace with the path to your dat file
    try:
        data = read_data_from_file(file_path)
        centroid_x, centroid_y = calculate_centroid(data)
        print("Centroid coordinates: ({:.2f}, {:.2f})".format(centroid_x, centroid_y))
    except FileNotFoundError:
        print("File not found.")
    except ValueError as ve:
        print(ve)
