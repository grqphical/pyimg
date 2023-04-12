from PIL import Image
from .parser import *
from rich import print

# Parse arguments given
args = parser.parse_args()

# try to load the image and if it fails return an error
try:
    image = Image.open(args.image_file)
except FileNotFoundError:
    print(f"[red]Cannot find file '{args.image_file}'[/red]")
    exit(1)

# check if user wants to view stats
if args.stats:
    print(f"File: '{image.filename}' | Width: {image.width} | Height: {image.height} | Colourspace: {image.mode}")

# Get what class of the program we are using
try:
    active_class = valid_classes[args.target_class]
except KeyError:
    print(f"[red]ERROR: Invalid subcommand '{args.target_class}'[/red]")

# Find what method we are calling and run it
method = getattr(active_class, args.action)
new_image = method(image, *args.args)

# Save the image at the end
new_image.save(args.image_file)