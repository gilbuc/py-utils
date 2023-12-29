#! python3
# merge-pdf.py - Kopiert alle Seiten eines PDFs und merged ein Wasserzeichen

import PyPDF2

pdfFile = open('2019_2.pdf', 'rb')
wasserZeichenFile = open('wasserzeichen.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFile)
pdfWasserZeichenReader = PyPDF2.PdfFileReader(wasserZeichenFile)
pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(pageNum)
    pageObj.mergePage(pdfWasserZeichenReader.getPage(0))
    pdfWriter.addPage(pageObj)

pdfOutputFile = open('Neue-Datei.pdf', 'wb')

pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()

pdfFile.close()
