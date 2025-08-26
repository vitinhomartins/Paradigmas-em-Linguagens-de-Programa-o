def existe_matricula(lista, matricula):
    for estudante in lista:
        if estudante["matricula"] == matricula:
            return True
    return False

n = int(input("Digite o número de registrados a ser preenchidos: "))
estudantes = []
while len(estudantes) < n:
    matricula = input("Digite a matricula do estudante: ")
    if existe_matricula(estudantes, matricula):
        print("Já existe essa matricula! Digite outro aluno: ")
        continue
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))
    estudante = {
        "nome" : nome,
        "matricula" : matricula,
        "nota" : nota
    }
    estudantes.append(estudante)
print("Estudantes Cadastrados!")
for estudante in estudantes:
    print(estudante)