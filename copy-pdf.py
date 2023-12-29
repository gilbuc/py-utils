#! python3
# copy-pdf.py - Kopiert alle Seiten eines PDFs in ein Neues

import PyPDF2

pdfFile = open('2019_2.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFile)
pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(pageNum)
    pageObj.rotateClockwise(90)
    pdfWriter.addPage(pageObj)

pdfOutputFile = open('Neue-Datei.pdf', 'wb')

pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()

pdfFile.close()
