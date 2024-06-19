print("--------------------------------------------------------------")
print ("/ 19. Verificar si un nombre es corto, medio o largo /")
print("--------------------------------------------------------------")

nombre = input("Ingrese su nombre: ")

leernombre = len(nombre)

if leernombre < 5:
    print(f"El nombre {nombre} es corto.")
elif leernombre <= 8:
    print(f"El nombre {nombre} es mediano.")
else:
    print(f"El nombre {nombre} es largo.")
