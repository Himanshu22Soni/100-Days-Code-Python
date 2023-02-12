# Exercise 08 Merge the PDF.

import os
from PyPDF2 import PdfWriter

merger = PdfWriter()

pdfFiles = os.listdir("TestingPDF")

print(pdfFiles)
for pdf in pdfFiles:
    merger.append(f"TestingPDF/{pdf}")

merger.write("TestingPDF/merged-pdf.pdf")
merger.close()
