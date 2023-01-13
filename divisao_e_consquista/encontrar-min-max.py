def encontrar_min_max(numeros):
    # se o vetor estiver vazio, retorna apenas uma mensagem
    if len(numeros) == 0:
        return 'vetor vazio'
    # caso base: se a lista tem apenas um elemento, retorne o elemento como min e max
    if len(numeros) == 1:
        return (numeros[0], numeros[0])
    # divida a lista ao meio
    meio = len(numeros) // 2
    min_esq, max_esq = encontrar_min_max(numeros[:meio])
    min_dir, max_dir = encontrar_min_max(numeros[meio:])
    # conquistar: retorne o min e o max das duas metades
    return (min(min_esq, min_dir), max(max_esq, max_dir))

# teste a função
print(encontrar_min_max([1, 2, 3, 4, 5]))  # (1, 5)
print(encontrar_min_max([5, 4, 3, 2, 1]))  # (1, 5)
print(encontrar_min_max([5, 1, 2, 4, 3]))  # (1, 5)
print(encontrar_min_max([]))  # (1, 5)