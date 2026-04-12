
# Text extraction from the Image
# Install Tesseract (Capture text in the image) --> pip install pytesseract

# Import Libraries
import pytesseract
from PIL import Image, ImageFilter, ImageOps
import os


# Install tesseract --> https://github.com/UB-Mannheim/tesseract/wiki.

# Set Tesseract path.
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def preprocess_image(img):
    img = img.convert('L')
    img = ImageOps.autocontrast(img)
    img = img.filter(ImageFilter.SHARPEN)
    img = img.point(lambda x: 0 if x < 140 else 255, '1')
    return img

def extract_text(image_path):
    try:
        img = Image.open(image_path)
    except FileNotFoundError:
        return "File not found. Please check the path."
    except Exception as e:
        return f"Error opening image: {e}"

    processed_img = preprocess_image(img)
    text = pytesseract.image_to_string(processed_img)

    if not text.strip():
        print("No text found. Retrying with different settings...")
        custom_config = r'--oem 3 --psm 6'
        text = pytesseract.image_to_string(processed_img, config=custom_config)
    if not text.strip():
        return "No readable text found in image."

    return text


# ===== Program execution =====

# Ask user for image path
image_path = input("Enter image path: ").strip().strip('"')

if not image_path:
    print("No path entered.")
    exit()

# check file exists before processing
if not os.path.exists(image_path):
    print("File does not exist.")
    exit()

# Extract text
result = extract_text(image_path)

print("\nExtracted Text:\n")
print(result)