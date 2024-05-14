#TEXTO CIFRADO
textEncryp = "lzav lz bu tluzhql kl wyblihz";#tiene error no es q es p
#LENGUAJE ABECEDARIO
languaje = ["a","b","c","d","e","f","g","h","i","j","k","l", "ñ","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
# CIFRADO CESAR
# CONSISTE EN TOMAR UNA POSICIÓN DEL ABECEDARIO:
# INICIAR EL ABECEDARIO DESDE ESA POSICIÓN
for init in range(0, 26):
    position = init;
    sustitution = []


    #TOMAMOS LOS VALORES DESPUES DE LA POSICIÓN
    for x in  range(position, len(languaje)):
        sustitution.append(languaje[x])


    #TOMAMOS LOS VALORES ANTES DE LA POSICIÓN
    for x in  range(position):
        sustitution.append(languaje[x])


    #print("languaje: ", init)
    #print(languaje)
    #print("sustitution")
    #print(sustitution)


    #Inicializamos variable para resultado final
    result = ""
    #Recorremos el texto
    for te in  textEncryp:
        if(te != " "):#SI ES DIFERENTE A UN ESPACIO
            for index, item in enumerate(sustitution):
                if(item == te):
                    result = result + (languaje[index])



    print("result end:", init)
    print(result, "\n")
