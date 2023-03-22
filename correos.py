#este programa crea correos
nombres=["Adrian","francisco","sarai","sergio","aurelio"]
apellidos=["Hernandez","perez","patricio","Lezama","hernandez"]
correos=[]
#Checar que sean de igual tamaño
ln=len(nombres)
la=len(apellidos)
if ln==la:
    #abrir archivo
    lista=open("lista.txt","w")
    for i in range(ln):
        correo=nombres[i]+"."+apellidos[i]+"@correo.com"
        correos.append(correo)
        print(correo)
for x in range(ln):
    lista.write(correos[x])
    lista.write("\n")
lista.close()
        
