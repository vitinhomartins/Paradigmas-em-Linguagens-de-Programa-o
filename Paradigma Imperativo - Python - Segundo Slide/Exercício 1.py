estoque = ["Camisa", "Calça", "Blusa", "Jaqueta"]
estoque.append("Sapato")
estoque.insert(2, "Boné")
if "Chapéu" in estoque:
    print("Chapéu está no estoque!")
    estoque.remove("Chapéu")
else:
    print("Não está no estoque!")
estoque.sort()
print(estoque)
