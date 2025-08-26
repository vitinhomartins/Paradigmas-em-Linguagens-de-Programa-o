n = int(input("Digite quantos valores você deseja: "))

a, b = 0, 1

if n <= 0:
    print("Valores negativos não permitidos!")
elif n == 1:
    print("Sequência de Fibonacci:")
    print(a)
else:
    print("Sequência de Fibonacci:")
    for _ in range(n):
        print(a)
        a, b = b, a + b
