def numero_decir(palabra, n):
    resultado = ""
    i = 0       #Indice de la palabra.

    if n == 0: 
        return ""
    
    else:
        while i < len(palabra):
            j = 1       #Contador de repeticion

            while i + 1 < len(palabra) and palabra[i] == palabra[i+1]:
                i += 1
                j += 1
            resultado += (str(j) + palabra[i])
            i += 1

        return str((resultado)) + "\n" + numero_decir((resultado), n-1)


s = numero_decir("11221", 3)        #Palabra y cantidad de "leer y decir" 
print(s)