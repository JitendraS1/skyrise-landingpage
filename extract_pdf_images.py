import fitz  # PyMuPDF
import os

def extract_specific_images(pdf_path, output_dir):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Open the PDF
    doc = fitz.open(pdf_path)
    
    # Extract specific pages as images
    pages_to_extract = [0, 1, 2, 3, 4, 7]  # Cover page, 3D view, amenities, layout, legal, location
    page_names = ['hero-bg', '3d-view-1', 'amenities', 'layout-plan', 'legal-docs', 'location-map']
    
    for i, page_num in enumerate(pages_to_extract):
        # Check if page exists
        if page_num < len(doc):
            page = doc.load_page(page_num)
            # Create a higher resolution pixmap
            mat = fitz.Matrix(2.0, 2.0)  # 2x zoom
            pixmap = page.get_pixmap(matrix=mat)
            
            # Save the image
            image_name = f"{page_names[i]}.jpg"
            image_path = os.path.join(output_dir, image_name)
            pixmap.save(image_path)
            print(f"Saved {image_name}")
    
    doc.close()
    print(f"Extracted {len(pages_to_extract)} images to {output_dir}")

if __name__ == "__main__":
    pdf_path = "skyrise residential township.pdf"
    output_dir = "images"
    extract_specific_images(pdf_path, output_dir)