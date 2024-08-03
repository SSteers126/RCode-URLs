from PIL import Image
import pytesseract
from django.core.files import File
from uuid import uuid4

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Get the bounding box proportional to the full screen tested on, so that it can be used for other resolutions
crop_box_ratio = (655/1920, 965/1080, 830/1920, 990/1080)


def prepare_screenshot(screenshot) -> Image:
    image = Image.open(screenshot)

    # Estimate a bounding box based on where the ID was tested to be on a 1080p screen
    bounding_box = (int(crop_box_ratio[0]*image.width), int(crop_box_ratio[1]*image.height),
                    int(crop_box_ratio[2]*image.width), int(crop_box_ratio[3]*image.height))

    image = image.crop(bounding_box)

    # Ensure any newlines added by tesseract aren't then passed to any functions wanting to treat it as an int
    return pytesseract.image_to_string(image, lang="eng").strip()


if __name__ == "__main__":
    prepare_screenshot("R-Code.png")
