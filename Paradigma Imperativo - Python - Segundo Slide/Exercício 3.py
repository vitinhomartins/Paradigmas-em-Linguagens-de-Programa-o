nomes = ["Homer", "Marge", "Bart", "Lisa", "Maggie"]
vogais = 'aeiouAEIOU'
for nome in nomes:
    contador = 0
    for letra in nome:
        if letra in vogais:
            contador = contador + 1
    print(nome, " tem ", contador, " vogal(is)")