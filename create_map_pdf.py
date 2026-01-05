from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors

def create_map_pdf():
    # Create PDF document
    doc = SimpleDocTemplate("images/skyrise-residential-township-map.pdf", pagesize=A4)
    
    # Container for the 'Flowable' objects
    elements = []
    
    # Get sample styles
    styles = getSampleStyleSheet()
    
    # Add title
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        spaceAfter=30,
        alignment=1,  # Center alignment
        textColor=colors.HexColor('#41aeab')
    )
    
    title = Paragraph("Sky Rise Residential Township", title_style)
    elements.append(title)
    elements.append(Spacer(1, 20))
    
    # Add subtitle
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Normal'],
        fontSize=16,
        spaceAfter=20,
        alignment=1,  # Center alignment
        textColor=colors.HexColor('#fcec14')
    )
    
    subtitle = Paragraph("Master Plan & Location Map", subtitle_style)
    elements.append(subtitle)
    elements.append(Spacer(1, 30))
    
    # Add description
    desc_style = ParagraphStyle(
        'Description',
        parent=styles['Normal'],
        fontSize=12,
        spaceAfter=20,
        alignment=0,  # Left alignment
        leftIndent=20,
        rightIndent=20
    )
    
    description = Paragraph(
        "This map shows the layout and location of Sky Rise Residential Township, "
        "featuring premium plots with world-class amenities. The township is strategically "
        "located in Dholera Smart City, Gujarat, offering easy connectivity to major urban centers.",
        desc_style
    )
    elements.append(description)
    elements.append(Spacer(1, 20))
    
    # Add features list
    features = [
        "Strategic Location in Dholera Smart City",
        "Premium Residential Plots",
        "World-Class Amenities",
        "Secure Documentation",
        "Well-Planned Infrastructure",
        "Green & Sustainable Development"
    ]
    
    for feature in features:
        feature_para = Paragraph(f"• {feature}", styles['Normal'])
        elements.append(feature_para)
        elements.append(Spacer(1, 8))
    
    elements.append(Spacer(1, 30))
    
    # Add contact information
    contact_style = ParagraphStyle(
        'Contact',
        parent=styles['Normal'],
        fontSize=12,
        spaceAfter=10,
        alignment=1,  # Center alignment
        textColor=colors.HexColor('#333333')
    )
    
    contact_info = [
        "Sky Rise Residential Township",
        "Dholera Smart City, Gujarat",
        "Contact: +91 98765 43210",
        "Email: info@skyrise-township.com"
    ]
    
    for info in contact_info:
        elements.append(Paragraph(info, contact_style))
    
    elements.append(Spacer(1, 20))
    
    # Add a simple map placeholder (in a real PDF, this would be an actual map image)
    try:
        # Try to add a layout plan image if it exists
        layout_img_path = "images/layout-plan.jpg"
        import os
        if os.path.exists(layout_img_path):
            img = Image(layout_img_path)
            img.drawHeight = 4*inch
            img.drawWidth = 6*inch
            img.hAlign = 'CENTER'
            elements.append(img)
            elements.append(Spacer(1, 20))
    except:
        # If no image, add a placeholder
        map_placeholder = Paragraph("Map/Location Image Placeholder", styles['Italic'])
        elements.append(map_placeholder)
        elements.append(Spacer(1, 20))
    
    # Add footer
    footer_style = ParagraphStyle(
        'Footer',
        parent=styles['Normal'],
        fontSize=10,
        spaceAfter=10,
        alignment=1,
        textColor=colors.gray
    )
    
    footer = Paragraph("© 2026 Sky Rise Residential Township. All Rights Reserved.", footer_style)
    elements.append(footer)
    
    # Build PDF
    doc.build(elements)
    print("Map PDF created successfully: images/skyrise-residential-township-map.pdf")

if __name__ == "__main__":
    create_map_pdf()