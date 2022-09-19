from PyPDF2 import PdfFileWriter,PdfFileReader
import getpass
mypdfwriter=PdfFileWriter()
mypdffile=PdfFileReader('Some_New_Doc.pdf')
for pages in range(mypdffile.numpages):
  mypdfwriter.addPages(mypdffile.getPage(pages))
password=getpass.getpass(Prompt='Create Password: ')  
password=input('Create password: ')  
mypdfwriter.encrypt(password)
file=open('Protected_file.pdf,'wb')
mypdfwriter.write(file)
  
