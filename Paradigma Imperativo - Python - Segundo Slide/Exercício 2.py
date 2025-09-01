aluno = ["João", "Maria", "Pedro", "Ana"]
aluno.append("Carlos")
aluno.append("Beatriz")
aluno.sort()
aluno_remove = input("Qual aluno deseja remover?: ")
if(aluno_remove in aluno):
    print(aluno_remove, " foi removido!")
    aluno.remove(aluno_remove)
else:
    print("esse aluno não existe!")
if("Ana" in aluno):
    print("Posição da Ana é ", aluno.index("Ana"))
else:
    print("A Ana não está presente!")
if not aluno:
    print("A lista está vazia!")
