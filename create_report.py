from txt_to_dicc import get_data
from pdf_to_text import get_page_context 

# To pass to txt to pdf keeping format this site works: https://convertio.co/es/txt-pdf/

autor = "Haruki Murakami"

path_myclipppings = "My Clippings.txt"
path_txt_report = f"{autor} Report.txt"

data = get_data(path_myclipppings)

with open(path_txt_report, 'w', encoding='utf-8') as file:

    text_content = f"Recopilación de {autor}\n"
    for d in data:
        if d['Autor'] == autor:
            name_file = d['Autor'] + " - " + d['Libro']
            contexto = get_page_context(name_file, d['Frase'])
            text_content += f"""Libro: {d['Libro']} | Fecha: {d['Fecha']}

{d['Frase']}

Contexto:
{contexto}

----------------------

"""

    file.write(text_content)
