from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, PageTemplate, Frame, Image

def add_image(canvas, doc):
    image_path = "your_image_path.jpg"  # Specify the path to your image
    canvas.drawImage(image_path, 100, 100)  # Adjust the coordinates as needed

doc = SimpleDocTemplate("output.pdf", pagesize=letter)

# Define a page template with your image added
frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height)
template = PageTemplate(frames=[frame], onPage=add_image)

# Add the page template to the document
doc.addPageTemplates(template)

# Now, add your content as usual
content = []  # Your content here
doc.build(content)
