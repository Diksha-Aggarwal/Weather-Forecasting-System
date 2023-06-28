import csv
import matplotlib.pyplot as plt

def create_graph_from_csv(df, start_range, end_range):
    # Read data from CSV file
    with open(df, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    df = 'map.csv'
    # Separate x and y data
    x = df['HGHT']
    y1 = df['TEMP']
    y2 = df['PRES']
    y3 = df['RELH']
    y4 = df['DRCT']
    y5 = df['SPED']
    # x = []
    # y = []
    # for row in data[start_range:end_range+1]:
    #     x.append(float(row[0]))
    #     y1.append(float(row[1]))

    # Plot the graph
    plt.plot(x, y1)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('graphfilter')
    plt.grid(True)

    # Show the graph
    plt.show()

# Example usage
df = 'map.csv'
start_range = 2  # Start index of the range
end_range = 99    # End index of the range
create_graph_from_csv(df, start_range, end_range)
