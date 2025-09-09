import random
import string

def gerar_senha(tipo):
    tamanho = 8
    
    if tipo == 1:
        caracteres = string.ascii_letters  
    elif tipo == 2:
        caracteres = string.ascii_letters + string.digits  
    elif tipo == 3:
        caracteres = string.ascii_letters + string.digits + string.punctuation 
    else:
        return "Opção inválida!"
    
    senha = ""
    for i in range(tamanho):
        senha += random.choice(caracteres) 
    
    return senha

usuarios = {}  

while True:
    nome = input("Digite o nome do usuário [caso digite 'sair' o programa parará imediatamente] : ")

    if nome.lower() == "sair":
        break
    
    if nome in usuarios:
        print("Esse nome já foi cadastrado. Tente outro para ser adicionado ao banco de dados.\n")
        continue
    
    print("Escolha o tipo de senha:")
    print("1 - Apenas letras")
    print("2 - Letras e números")
    print("3 - Letras, números e símbolos especiais")
    
    tipo = int(input("Digite a opção: "))
    senha = gerar_senha(tipo)
    
    usuarios[nome] = senha
    print(f"Usuário '{nome}' cadastrado com a senha: {senha}\n")

print("\nLista final de usuários e senhas no banco de dados:")
for user, senha in usuarios.items():
    print(f"{user} : {senha}")
