# install pdfminer - pip install pdfminer
# install chardet - pip install chardet

import io

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage


def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = io.StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos = set()
    print("in")
    count=0
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages,
                                  password=password,
                                  caching=caching,
                                  check_extractable=True):
        if count == 7:
            interpreter.process_page(page)
            break
        else:
            count+=1
            
    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    print(text)

if __name__ == '__main__':
    path = 'Sample3.pdf'
    #text_extractor(path)
    convert_pdf_to_txt(path)
