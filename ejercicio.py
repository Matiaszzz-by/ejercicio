ListaN = []
def Añadirnombres():
    print(f"Tu lista se ve asi actualmente: {ListaN}")
    while True:
        try:
            veces = int(input("Ingrese cuantos nombres agregara:"))
            break
        except ValueError:
            print("Ingrese un valor numerico.")
    for i in range(veces):
        nombres = input("Ingrese Nombres a agregar:")
        ListaN.append(nombres)
        print(f"Tu lista se ve asi actualmente: {ListaN}")

def vaciarlista():
    if ListaN == []:
        print("Lista vacia agregue nombres primero")
    else:
        print("Lista vaciada correctamente")
        ListaN.clear()
        print(f"Lista actual:{ListaN}")

def eliminar_nombre():
    if ListaN == []:
        print("La lista esta vacia no hay nada para eliminar")
        return
    nombre = input("Ingrese el nombre que desea eliminar:")
    if nombre in ListaN:
        ListaN.remove(nombre)
        print(f"{nombre} eliminado correctamente")
        print(f"Lista actualizada: {ListaN}")
    else:
        print(f"{nombre} no esta en la lista.")

def salir():
    print("ADIOS HERMANITO...")
    
def mostrar_menu():
    ListaN = []
    while True:
        print("1.-AÑADIR NOMBRES A LAS LISTAS")
        print("2.-VACIAR LAS LISTAS")
        print("3.-ELIMINAR NOMBRE DE LISTA")
        print("4.-SALIR")
        try:
            opcion = int(input("Ingrese una opcion:"))
        except ValueError:
            print("Ingrese un valor numerico")
        else:
            if opcion == 1:
                Añadirnombres()
            elif opcion == 2:
                vaciarlista()
            elif opcion == 3:
                eliminar_nombre()
            elif opcion == 4:
                salir()
                break
            else:
                print("Opcion no valida es del 1 al 4")
mostrar_menu()


    