from pypdf import PdfWriter

writer = PdfWriter()
#FIles must be in the same folder as the python script, put the name of the pdf in question in the brackets here!
pdfs =['file1.pdf', 'file2.pdf', 'file3.pdf']

for pdf in pdfs:
    writer.append(pdf)
#this is what the new file will be saved as, so be on the look out for i t!
writer.write("merged.pdf")
print("PDF's merge has been successful")