# CS50 Shirtificate - implement a program that prompts the user for their name and outputs, using fpdf2, a CS50 shirtificate in a file called shirtificate.pdf similar to this one for John Harvard, with these specifications:
# The orientation of the PDF should be Portrait.
# The format of the PDF should be A4, which is 210mm wide by 297mm tall.
# The top of the PDF should say “CS50 Shirtificate” as text, centered horizontally.
# The shirt’s image should be centered horizontally.
# The user’s name should be on top of the shirt, in white text.

from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.ln(10)
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 24)
        # Printing title:
        self.cell(80)
        self.cell(30, 10, "CS50 Shirtificate", border=0, align="C")
        # Performing a line break:
        self.ln(20)

name = input("Name: ")

pdf = PDF(orientation = "portrait", format="A4")
pdf.add_page()

pdf.image("shirtificate.png", x=0, y=60)

pdf.set_font("Helvetica", size=36)
pdf.set_text_color(r=255, g=255, b=255)
pdf.set_y(150)
pdf.set_x(45)
pdf.cell(txt=f"{name} took CS50", align="C")

pdf.output("shirtificate.pdf")
