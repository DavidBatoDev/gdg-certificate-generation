from PIL import Image, ImageDraw, ImageFont
import os

TEMPLATE_PATH = "certificate_templates/certificate_template.png"  # Make sure this matches your actual template name, it can be a certificate for studyjams, levelling system etc.
FONT_PATH = "Inter/static/Inter_24pt-SemiBold.ttf"
OUTPUT_FOLDER = "generated_certificates"

names = ["Jane Smith", "Alice Johnson"] 

if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

for name in names:
    # Open the certificate template
    print(f"Generating certificate for {name}...")
    img = Image.open(TEMPLATE_PATH)
    draw = ImageDraw.Draw(img)

    # Load the font with adjusted size to 94 (based on the template)
    font = ImageFont.truetype(FONT_PATH, 94)

    # Use textbbox instead of textsize (for newer Pillow versions)
    text_bbox = draw.textbbox((0, 0), name, font=font) # Get the bounding box of the text
    text_width = text_bbox[2] - text_bbox[0] # Calculate width and height of the text
    text_height = text_bbox[3] - text_bbox[1] # Calculate width and height of the text
    
    # Calculate position - center horizontally and position vertically at the line
    # Based on the certificate image, adjusting to position the text at the name line
    x = (img.width - text_width) / 2 # Center horizontally
    y = img.height * 0.47 - text_height / 2  # Position at around 47% from the top of the image

    # Draw text (white)
    draw.text((x, y), name, fill="white", font=font)

    # Save the certificate
    output_path = os.path.join(OUTPUT_FOLDER, f"{name}.png")
    
    # If the file exists, remove it so we can replace it
    if os.path.exists(output_path):
        os.remove(output_path)

    # Save the certificate
    img.save(output_path)

print("Certificates generated successfully!")
