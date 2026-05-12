#Extracts text from PDFs.

#Example responsibilities:

#open PDF
#read pages
#return raw text

from PyPDF2 import PdfReader


def load_pdf(file_path):
    text = ""

    reader = PdfReader(file_path)

    for page in reader.pages:
        extracted = page.extract_text()

        if extracted:
            text += extracted + "\n"

    return text