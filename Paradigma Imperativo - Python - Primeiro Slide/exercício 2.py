my_int_list = []
for i in range(0, 3):
    my_int_list.append(int(input("Digite o numero: ")))
if(my_int_list[0] > my_int_list[1]):
    aux = my_int_list[0]
    my_int_list[0] = my_int_list[1]
    my_int_list[1] = aux
if(my_int_list[1] > my_int_list[2]):
    aux = my_int_list[1]
    my_int_list[1] = my_int_list[2]
    my_int_list[2] = aux    
if(my_int_list[0] > my_int_list[1]):
    aux = my_int_list[0]
    my_int_list[0] = my_int_list[1]
    my_int_list[1] = aux
print(my_int_list[0], " ", my_int_list[1], " ", my_int_list[2])