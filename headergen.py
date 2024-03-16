from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def draw_header(canvas):
    # Draw your header image here
    header_image_path = "images/header_A.png"
    canvas.drawImage(header_image_path, 0,0, width=650, height=50)

def create_pdf():
    c = canvas.Canvas("example.pdf", pagesize=letter)

    # Draw content on each page
    for i in range(10):  # Example: 10 pages
        draw_header(c)
        c.showPage()

    c.save()

if __name__ == "__main__":
    create_pdf()
