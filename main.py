from PIL import Image
import pytesseract
import os

path_image = "/home/lhenaoll/Pictures/Screenshots/TexFromImage.png"
data = os.system(f'grim -g "$(slurp -c \"#ff0000ff\")" {path_image}')

# If user no take a screenshot, exit
if str(data.real).split("\\n")[0] != "0":
    exit(1)

image = Image.open(path_image)
text = pytesseract.image_to_string(image, output_type="string")

os.system(f'wl-copy "{text}"')
os.system(f'notify-send -i x "TFI - @lhenaoll" "{text}"')
