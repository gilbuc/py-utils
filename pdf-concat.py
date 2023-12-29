import PyPDF2,sys

print (sys.argv[0])
if len(sys.argv) > 3:
    # Open the files that have to be merged one by one
    pdf1File = open(sys.argv[1]+'.pdf', 'rb')
    pdf2File = open(sys.argv[2]+'.pdf', 'rb')

 
    # Read the files that you have opened
    pdf1Reader = PyPDF2.PdfReader(pdf1File)
    pdf2Reader = PyPDF2.PdfReader(pdf2File)
 
    # Create a new PdfFileWriter object which represents a blank PDF document
    pdfWriter = PyPDF2.PdfWriter()
 
    # Loop through all the pagenumbers for the first document
    for pageNum in range(len(pdf1Reader.pages)):
        pageObj = pdf1Reader.pages[pageNum]
        pdfWriter.add_page(pageObj)
 
    # Loop through all the pagenumbers for the second document
    for pageNum in range(len(pdf2Reader.pages)):
        pageObj = pdf2Reader.pages[pageNum]
        pdfWriter.add_page(pageObj)
 
    # Now that you have copied all the pages in both the documents, write them into the a new document
    pdfOutputFile = open(sys.argv[3]+'.pdf', 'wb')
    pdfWriter.write(pdfOutputFile)
 
    # Close all the files - Created as well as opened
    pdfOutputFile.close()
    pdf1File.close()
    pdf2File.close()
