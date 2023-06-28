import csv
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table

def generate_table_from_csv(csv_file_path, output_file_path):
    # Read data from CSV file
    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)

    # Create the PDF document
    doc = SimpleDocTemplate(output_file_path, pagesize=letter)

    # Create the table and add data
    table = Table(data)

    # Apply table styles
    table.setStyle([
        ('GRID', (0, 0), (-1, -1), 1, (0.5, 0.5, 0.5)),
        ('BACKGROUND', (0, 0), (-1, 0), (0.8, 0.8, 0.8)),
        ('TEXTCOLOR', (0, 0), (-1, 0), (0, 0, 0)),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), (0.9, 0.9, 0.9)),
        ('TEXTCOLOR', (0, 1), (-1, -1), (0, 0, 0)),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')
    ])

    # Build the PDF document
    elements = [table]
    doc.build(elements)

# Example usage
csv_file_path = 'map.csv'
output_file_path = 'table.pdf'
generate_table_from_csv(csv_file_path, output_file_path)
