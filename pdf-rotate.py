import PyPDF2,sys

pdf_in = open(sys.argv[1], 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_in)
pdf_writer = PyPDF2.PdfWriter()

for pagenum in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[pagenum]
    page.rotate(180)
    pdf_writer.add_page(page)

pdf_out = open('rotated.pdf', 'wb')
pdf_writer.write(pdf_out)
pdf_out.close()