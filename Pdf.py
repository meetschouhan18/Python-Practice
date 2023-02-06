import PyPDF2

p = open('pdffile.pdf','rb')
#rb stands for read bytes

r = PyPDF2.PdfFileReader(p)
#in PyPDF2 we used PdfFileReader() func inside which the opened pdf file is given as argument

print(r.numPages)
#prints number of pages in our pdf file

page = r.getPage(3)
#gets data from specified page number

print(page.extractText())
#extracts text from specified page number
