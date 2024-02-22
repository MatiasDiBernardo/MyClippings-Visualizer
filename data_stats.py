from txt_to_dicc import get_data

def organize_by_autor(data):
    dicc_autor = {}
    for d in data:
        if d['Autor'] in dicc_autor.keys():
            dicc_autor[d['Autor']].append([d['Libro'], d['Fecha'], d['Frase']]) 
        else:
            dicc_autor[d['Autor']] = [[d['Libro'], d['Fecha'], d['Frase']]]
    
    return dicc_autor

def libros_por_autor(data_autor):
    libros = []
    for d in data_autor:
        libros.append(d[0])
    
    libros = list(set(libros))
    return libros

def info_from_data(data):
    dicc_autores = organize_by_autor(data)

    for key in dicc_autores.keys():
        print(f"Autor: {key}")
        print("Libros leídos: ", libros_por_autor(dicc_autores[key]))
        print("Cantidad de frases: ", len(dicc_autores[key]))
        print("----------------")

path_myclipppings = "My Clippings.txt"
data = get_data(path_myclipppings)
info_from_data(data)