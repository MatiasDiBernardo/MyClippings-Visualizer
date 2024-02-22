import fitz
import os

def get_page_context(book_name, frase_target):
    path_base = "E:\Maty\Otros\Literatura\Libros"
    path_book = os.path.join(path_base, book_name + ".pdf")

    doc = fitz.open(path_book) # open a document

    # There are cases where the in line jump brakes the sentence. A second case fix this issue
    for page in doc:
        text_page = page.get_text() # get plain text encoded as UTF-8
        text_page_good = text_page.replace("\n", " ")
        text_page_second_case = text_page.replace("\n", "")

        if frase_target in text_page_good:
            return text_page_good
        
        if frase_target in text_page_second_case:
            return text_page_good
    
    # Only case not contemplated is when frase is in between two pages.
    
    return "No se enconto la frase especificada."
