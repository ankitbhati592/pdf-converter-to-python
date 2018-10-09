 
import io
 
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage
 
pdf_path = '/home/ankur/downloads'
complete_text = ""
 
 
def extract_text_by_page(pdf_path):
    with open(pdf_path, 'rb') as fh:
        for page in PDFPage.get_pages(fh, 
                                      caching=True,
                                      check_extractable=True):
            resource_manager = PDFResourceManager()
            fake_file_handle = io.BytesIO()
            print fake_file_handle
            converter = TextConverter(resource_manager, fake_file_handle)
            print converter
            page_interpreter = PDFPageInterpreter(resource_manager, converter)
            print page_interpreter
            
            page_interpreter.process_page(page)
            print 'After page interpreter'
            text = fake_file_handle.getvalue()
            print text
            yield text
 
            # close open handles
            converter.close()
            fake_file_handle.close()
 
def extract_text(pdf_path):
    global complete_text
    for page in extract_text_by_page(pdf_path):
        # print(page)
        complete_text += page
    print complete_text

if __name__ == '__main__':
    print(extract_text('/home/ankur/Downloads/Resume.pdf'))
