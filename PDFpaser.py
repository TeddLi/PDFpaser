import PyPDF2
import logging
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
# create file object variable
# opening method will be rb
filename="UMIR-01032023-EN.pdf"
pdffileobj = open(f'{filename}', 'rb')

# create reader variable that will read the pdffileobj
pdfreader = PyPDF2.PdfReader(pdffileobj)

# This will store the number of pages of this pdf file
x = len(pdfreader.pages)

# create a variable that will select the selected number of pages
pageobj = pdfreader.pages[x-1]

# (x+1) because python indentation starts with 0.
# create text variable which will store all text datafrom pdf file
text = pageobj.extract_text()

# save the extracted data from pdf to a txt file
# we will use file handling here
# dont forget to put r before you put the file path
# go to the file location copy the path by right clicking on the file
# click properties and copy the location path and paste it here.
# put "\\your_txtfilename"
with open(f"./{filename.split('.')[0]}.txt", "a") as file:
    logging.info("Start parsing")
    for page in range(x):
        logging.info(f"Parsing page {page}")
        pageobj = pdfreader.pages[page]
        text = pageobj.extract_text()
        file.writelines(text)
