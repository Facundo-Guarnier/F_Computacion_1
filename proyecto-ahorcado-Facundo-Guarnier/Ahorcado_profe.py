def ahorcado(word: str, chars):
    # Unicas guardará las letras de la palabra sin repetición
    unicas = []
    # Este for arma la lista unicas con las letras sin repetición
    for char in word:
        if char not in unicas:
            unicas.append(char)
    # Acá recién empieza a "jugar"
    counter = 0
    for char in chars:
        counter += 1
        if char in unicas:
            unicas.remove(char)
    return counter


if __name__ == '__main__':
    word = list(input('Palabra a adivinar: '))
    chars = []
    for char in word:
        if char not in chars:
            chars.append(char)
    counter = 0
    while len(chars) > 0:
        counter += 1
        char = input('Letra: ')
        if char in chars:
            chars.remove(char)
    print(counter)