# Import Required Modules
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A2
from reportlab.lib.styles import getSampleStyleSheet

# Prepare Date
DATA = [
    ["Date", "Name", "Subscription", "Price (Rs.)"]
    ["06/08/2026", "Biscuit", "Britannia bourbon two family pack", "2,000/-"]
    ["06/08/2026", "Fortune", "Fortune soybean oil twenty packets", "2,700/-"]
    ["06/08/2026", "Garnier", "Face Wash", "560\-"]
    ["Sub Total", "-", "-", "5,260/-"]
    ["Discount", "", "", "-438.3/-"]
    ["Total", "", "", "4,822/-"]
]
# Create PDF Template
pdf = SimpleDocTemplate("receipt.pdf", pagesize=A2)

# Create the Styles
styles = getSampleStyleSheet()
title_style = styles["Heading1"]
title_style.alignment = 1

# Create the Title
title = Paragraph("Mahakal Super Shop", title_style)

# Create Table Style
style = TableStyle([
    ("BOX", (0, 0), (-1, -1), 1, colors.black),
    ("GRID", (0, 0), (-1, -1), 1, colors.black),
    ("BACKGROUND", (0, 0), (-1, 0), colors.Gray),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
    ("ALIGN", (0, 0), "CENTER"),
    ("BACKGROUND", (0, 1), (-1, -1), colors.white)
])

# Create the Table
table = Table(DATA, style=style)
# Built the PDF
pdf.build([title, table])