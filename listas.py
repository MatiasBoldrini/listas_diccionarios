listaDeNumeros = [1,2,3,4,3,5,6,7,8,9,4,2,2]

def encontrar_Numeros_Repetidos(listaDeNumeros):
    diccionarioDeValores={}
    for element in listaDeNumeros: 
        if element in diccionarioDeValores:
            diccionarioDeValores[element] += 1
        else: 
            diccionarioDeValores[element] = 1

    return diccionarioDeValores
