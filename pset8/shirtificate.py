#creates a PDF image of a t-shirt with overlay of text: x took CS50!

from fpdf import FPDF

name = input("What is your name? ")
pdf = FPDF(orientation="landscape", format="A5")
pdf.add_page()
pdf.set_font('helvetica', size=12)
pdf.image("shirtificate.png",x = 0, y=70)
pdf.text(x =100, y=100, txt=(f"{name} took CS50"))
pdf.output("shirtificate.pdf")

