def content_to_dicc(cite):
    cite = cite.split("\n")
    
    info = cite[1]
    libro = info[:info.index("(") - 1]
    autor =  info[info.index("(") + 1:-1]
    metadata = cite[2]
    fecha = metadata.split("|")[-1]
    frase = cite[4]

    dicc = {"Autor": autor, 
            "Libro": libro,
            "Fecha": fecha,
            "Frase": frase}
    
    return dicc

def get_data(path_myclippings):
    data = []
    with open(path_myclippings, 'r', encoding="utf8") as file:
            content = file.read()

            # Reformular algunas cosas para tener la data ordenada
            content = content.replace("Un mundo feliz*Retorno a un mundo feliz (Colección Sepan Cuantos: 587) (Spanish Edition) (Huxley, Aldous)", "Un mundo feliz (Huxley, Aldous)")
            content = content.replace("ALEJANDRA PIZARNIK", "Alejandra Pizarnik")
            content = content.replace("Una Temporadan en el Infierno (Rimbaud)", "Una Temporada en el Infierno (Arthur Rimbaud)")
            content = content.replace("Fyodor Mikhailovich Dostoyevsky", "Fiodor Dostoievski")
            content = content.replace("Fiódor Dostoyevski", "Fiodor Dostoievski")
            content = content.replace("Haruiki Murakami", "Haruki Murakami")
            content = content.replace("Murakami Haruki", "Haruki Murakami")
            content = content.replace("kyllesdal master - Kyllesdal", "kyllesdal master (Kyllesdal)")
            content = content.split("==========")
            content[0] = "'\nPoesía Completa (Alejandra Pizarnik)\n- La subrayado en la página 49 | posición 741-742 | Añadido el lunes, 6 de noviembre de 2017 1:04:16\n\nLA CARENCIA\n'"
            content.pop()

            for cite in content:
                data.append(content_to_dicc(cite))
    
    return data
