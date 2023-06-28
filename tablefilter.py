import csv
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table

def generate_table_from_csv(csv_file_path, output_file_path, start_range, end_range):
    # Read data from CSV file
    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)

    # Filter data based on specified range
    filtered_data = data[start_range:end_range+1]

    # Create the PDF document
    doc = SimpleDocTemplate(output_file_path, pagesize=letter)

    # Create the table and add data
    table = Table(filtered_data)

    # Apply table styles
    table.setStyle([
        # Table styles here
    ])

    # Build the PDF document
    elements = [table]
    doc.build(elements)

# Example usage
csv_file_path = 'map.csv'
output_file_path = 'filteredtable.pdf'
start_range = 2  # Start index of the range
end_range = 100   # End index of the range
generate_table_from_csv(csv_file_path, output_file_path, start_range, end_range)