from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

def make_pdf(path, title, battery_life):
    c = canvas.Canvas(path, pagesize=letter)
    c.setFont("Helvetica-Bold", 20)
    c.drawString(1*inch, 10*inch, title)

    c.setFont("Helvetica-Bold", 16)
    c.drawString(1*inch, 9*inch, "1. Introduction")
    c.setFont("Helvetica", 12)
    c.drawString(1*inch, 8.5*inch, "This manual covers device operation.")

    c.setFont("Helvetica-Bold", 16)
    c.drawString(1*inch, 8*inch, "2. Specifications")
    c.setFont("Helvetica-Bold", 14)
    c.drawString(1*inch, 7.5*inch, "2.1 Battery")
    c.setFont("Helvetica", 12)
    c.drawString(1*inch, 7*inch, f"Battery life: {battery_life} hours")

    c.setFont("Helvetica-Bold", 16)
    c.drawString(1*inch, 6*inch, "3. Safety")
    c.setFont("Helvetica", 12)
    c.drawString(1*inch, 5.5*inch, "Follow all safety guidelines.")

    c.save()

make_pdf("data/ct200_manual.pdf", "CT200 Manual v1", "300")
make_pdf("data/ct200_manual_v2.pdf", "CT200 Manual v2", "250")
print("PDFs created")
