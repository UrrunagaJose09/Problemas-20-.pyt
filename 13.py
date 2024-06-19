print("--------------------------------------------------------------")
print ("/ 13. Determinar si un año es un siglo/")
print("--------------------------------------------------------------")

año= float(input("Ingrese el año: "))

if año % 100 ==0:
    print(f"El año {año} es un siglo")

else:
    print(f"El año {año} no un siglo")
