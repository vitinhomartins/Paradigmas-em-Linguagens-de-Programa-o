a = int(input("Digite o primeiro lado: "))
b = int(input("Digite o segundo lado: "))
c = int(input("Digite o terceiro lado: "))

if(a + b) > c and (a + c) > b and (b + c) > a:
    print("os lados formam um triângulo!")
    if(a == b == c):
        print("Formam um triângulo equilátero")
    elif a == b or b == c or a == c:
        print("Formam um triangulo isóceles")
    else:
        print("Formam um triangulo escaleno")
else:
    print("Não formam um triângulo")