from sklearn.cluster import KMeans
import numpy as np
from PIL import Image

def get_dominant_colors(image_path, k=5):
    # Open image and convert to numpy array
    image = Image.open(image_path)
    image = image.convert('RGB')
    image_array = np.array(image)
    
    # Reshape the image to be a list of pixels
    pixels = image_array.reshape((-1, 3))
    
    # Apply KMeans clustering to find dominant colors
    kmeans = KMeans(n_clusters=k, n_init=10)
    kmeans.fit(pixels)
    
    # Get the colors and their frequencies
    colors = kmeans.cluster_centers_
    labels, counts = np.unique(kmeans.labels_, return_counts=True)
    
    # Sort colors by frequency
    sorted_indices = np.argsort(counts)[::-1]
    dominant_colors = colors[sorted_indices]
    
    # Convert to integer values
    dominant_colors = dominant_colors.astype(int)
    
    return dominant_colors

def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])

# Analyze colors from the cover page
try:
    dominant_colors = get_dominant_colors('cover_page.png', k=5)
    print("Dominant colors in cover page:")
    for i, color in enumerate(dominant_colors):
        hex_color = rgb_to_hex(color)
        print(f"Color {i+1}: RGB{tuple(color)} - Hex: {hex_color}")
        
    # Analyze colors from page 2
    dominant_colors_page2 = get_dominant_colors('page2.png', k=5)
    print("\nDominant colors in page 2:")
    for i, color in enumerate(dominant_colors_page2):
        hex_color = rgb_to_hex(color)
        print(f"Color {i+1}: RGB{tuple(color)} - Hex: {hex_color}")
        
    # Analyze colors from page 3
    dominant_colors_page3 = get_dominant_colors('page3.png', k=5)
    print("\nDominant colors in page 3:")
    for i, color in enumerate(dominant_colors_page3):
        hex_color = rgb_to_hex(color)
        print(f"Color {i+1}: RGB{tuple(color)} - Hex: {hex_color}")
        
except Exception as e:
    print(f"Error analyzing colors: {e}")