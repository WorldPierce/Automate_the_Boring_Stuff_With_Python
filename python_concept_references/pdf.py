import PyPDF2, os

os.chdir('c:\\users\\wffpi\\documents')

pdfFile = open('file.pdf', 'rb') # must open in read binary mode

reader = PyPDF2.PdfFileReader(pdfFile)
print(reader.numPages) # number of pages in file
page = reader.getPage(0) # gets specific page
print(page.extractText())

for pageNum in range(reader.numPages):
    print(reader.getPage(pageNum).extractText())

# can add remove and reorder pages can not edit text

pdf1 = open('file1','rb')
pdf2 = open('file2','rb')
reader1 = PyPDF2.PdfFileReader(pdf1)
reader2 = PyPDF2.PdfFileReader(pdf2)
writer = PyPDF2.PdfFileWriter() # blank pdf in memory
for pageNum in range(reader1.numPages):
    page = reader1.getPage(pageNum)
    writer.addPage(page)

for pageNum in range(reader2.numPages):
    page = reader2.getPage(pageNum)
    writer.addPage(page)

outputFile = open('combinedPdf.pdf','wb')
writer.write(outputFile)
outputFile.close()
pdf1.close()
pdf2.close()
