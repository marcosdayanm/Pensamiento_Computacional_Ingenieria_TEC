# Lista de listas que contiene el inventario (15 productos)
inventario = [["#              ","Producto                       ","Cantidad       ","Precio ($)     ","Código"],
              [1,"Vasos(100pz)        ",380,135,"EMK3047"],
              [2,"Filtros de café     ",840,2,"EMK3048"],
              [3,"Leche en Polvo(5kg) ",230,120,"EMK3049"],
              [4,"Servilletas(400pz)  ",430,89,"EMK3050"],
              [5,"Palos mezcla (200pz)",880,42,"EMK3051"],
              [6,"Cafetera Turca      ",8,1300,"EMK3052"],
              [7,"Cafetera de Espresso",40,4300,"EMK3053"],
              [8,"Cafetera de Goteo   ",25,3600,"EMK3054"],
              [9,"Portavasos para 4   ",570,22,"EMK3055"],
              [10,"Cuchara café(150pz) ",350,73,"EMK3056"],
              [11,"Jarabes de sabores  ",220,39,"EMK3057"],
              [12,"Popotes ecológicos  ",610,5,"EMK3058"],
              [13,"Molino de café      ",23,790,"EMK3059"],
              [14,"Espumadora de leche ",17,1060,"EMK3060"],
              [15,"Azúcar en Polvo(5kg)",140,120,"EMK3061"]
              ] # Caben 20 caracteres en cada palabra


# Lista de listas que contiene los vendedores en el eje x y los productos en el eje y y muestra las ventas de cada producto por cada vendedor
empleados = [["---Ventas---                  ","1. Veronica   ","2. Eduardo    ","3. Marcos     ","4. Federico   ","5. Yosune   ",], # 14 celdas de espacio c/u
              ["Vasos(100pz)        ",000,000,000,000,000],
              ["Filtros de café     ",000,000,000,000,000],
              ["Leche en Polvo(5kg) ",000,000,000,000,000],
              ["Servilletas(400pz)  ",000,000,000,000,000],
              ["Palos mezcla (200pz)",000,000,000,000,000],
              ["Cafetera Turca      ",000,000,000,000,000],
              ["Cafetera de Espresso",000,000,000,000,000],
              ["Cafetera de Goteo   ",000,000,000,000,000],
              ["Portavasos para 4   ",000,000,000,000,000],
              ["Cuchara café(150pz) ",000,000,000,000,000],
              ["Jarabes de sabores  ",000,000,000,000,000],
              ["Popotes ecológicos  ",000,000,000,000,000],
              ["Molino de café      ",000,000,000,000,000],
              ["Espumadora de leche ",000,000,000,000,000],
              ["Azúcar en Polvo(5kg)",000,000,000,000,000],
             ]




def imprimirempleados(): # Función que imprime el reporte de ventas de todos los empleados
    for i in empleados:
        print()
        for j in i: # Loop adentro de otro, para imprimir cada elemento de la lista de listas y luego pasar al siguiente
            if i == empleados[0]:
                print(j, end="  ")
            else:
                print(j, end="\t\t")
    print("\n\n")




def imprimirinventario(): # Función que imprime el inventario con el formato y los espacios adecuados
    for i in inventario: 
        print()
        for j in i:
            if i == inventario[0]:
                print(j, end=" ")
            else:
                print(j, end="\t\t")
    print("\n\n")




def registrarventas(): # Función que registra ventas, actualiza inventario y lista de empleados y calcula el monto final
    imprimirinventario()
    
    while True: # Loop para validar que artículo se va a vender
        quearticulo = int(input("Seleccione el número del artículo que quiere vender: "))
        if quearticulo >0 and quearticulo < len(inventario): # Cambiar esto cuando meta mas productos
            articulofinal = inventario[quearticulo][1] # Esta variable guarda el nombre del artículo
            break
        else:
            print("Error, debe de escoger un número dentro del rango de los artículos, vuelva a intentar\n")
            continue
   
    
    while True: #Loop que verifica si hay suficiente inventario para vender el artículo
        cuantos = int(input("¿Cuántos artículos quiere vender? "))
        if cuantos <= inventario[quearticulo][2]:
            final = inventario[quearticulo][2] - cuantos
            inventario[quearticulo][2] = final
            precio = inventario[quearticulo][3] # Variable que almacena el precio del artículo seleccionado
            break
        else:
            print("Artículo sin inventario suficiente, intente de nuevo con una cantidad menor")
            continue
      
    while True: # Loop para pregunar el nombre del empleado y asignar venta al indicado
        ventastemporales = 0
        vendedor = input("Qué vendedor realiza la venta? (Veronica/Eduardo/Marcos/Federico,Yosune): ")
        
        # Asignar un número de empleado de acuerdo al input para poder meter la venta al empleado correcto
        if vendedor.lower() == "veronica":
            numeroempleado = 1
        elif vendedor.lower() == "eduardo":
            numeroempleado = 2
        elif vendedor.lower() == "marcos":
            numeroempleado = 3  
        elif vendedor.lower() == "federico":
            numeroempleado = 4
        elif vendedor.lower() == "yosune":
            numeroempleado = 5
    
        else: # Validador en caso de que el input sea incorrecto, se vuelve a repetir el while loop
            print("Nombre de vendedor incorrecto, seleccione entre (Veronica/Eduardo/Marcos/Federico,Yosune):")
            continue
        
        ventastemporales = empleados[quearticulo][numeroempleado]
        ventastemporales += cuantos
        empleados[quearticulo][numeroempleado] = ventastemporales
        
        #imprimirinventario()
        #imprimirempleados()
        break
    
    print(f"\n\nLa orden sería de {cuantos} piezas de {articulofinal.strip()}, es un total de ${precio * cuantos}\n\n")
    # COnfirmación final de orden y monto total




def actualizarinv(): # Función que agrega productos al inventario, elimina productos del inventario, y modifica propiedades individuales de cada producto
    while True: # While general en el que se engloba toda la función en caso de haber inputs incorrectos que se repita
        opciones = ["1. Agregar Producto",
                    "2. Eliminar Producto",
                    "3. Modificar Producto"]
        for i in opciones:
            print(i)
            
        seleccion = int(input("Seleccione el número de una de las opciones: "))
        if seleccion == 1:
            nuevoarticulo = []
            nombre = input("Nombre del producto que desea agregar: ")
            cantidad = int(input("Inserte la cantidad del artículo que desea agregar: "))
            precio = int(input("Inserte el precio del artículo: "))
            codigo = input("Inserte el código SKU del artículo: ")
        
            while len(nombre) < 20: # Con este while, se aladen espacios en blanco al producto hasta que su longitud llegue a 20 para darle formato a las tablas
                nombre += " "
            
            numarticulosiguiente = len(inventario) # El numero del artículo siguiente del inventario, para añadirlo de forma variable
            nuevoarticulo.append(numarticulosiguiente)
            nuevoarticulo.append(nombre)
            nuevoarticulo.append(cantidad)
            nuevoarticulo.append(precio)
            nuevoarticulo.append(codigo)
            
            inventario.append(nuevoarticulo)
            
            print("\n¡Listo! Inventario modificado ")
            #imprimirinventario()
            
            nombre = nombre.strip(" ")
            
            while len(nombre) < 20:
                nombre += " "
            
            nuevoempleados = [nombre,000,000,000,000,000]
            
            empleados.append(nuevoempleados) # Se añade el producto a la lista de las ventas de los empleados

            #imprimirempleados()
            break
        
        elif seleccion == 2: # Eliminar producto de inventario
            imprimirinventario()
            numeroeliminar = int(input("¿Qué número de producto desea eliminar? "))
            while True:  
                seguro = input("¿Seguro que desea eliminar el producto? (si/no): ")
                if seguro.lower() == "no":
                    print("Regresando al menú principal\n") # En caso de que haya sido una equivocación, se regresa al menú principal parando el loop
                    break
                elif seguro.lower() == "si":
                    del inventario[numeroeliminar] # Se accede a la lista a eliminar con un número insertado por el usuario
                    if numeroeliminar < len(inventario)-1:
                        num = 1
                        while num < len(inventario): 
                            inventario[num][0] = num
                            num += 1
                    
                    print("\n¡Listo! Producto eliminado\n")
                    del empleados[numeroeliminar]
    
                    #imprimirinventario()
                    #imprimirempleados()
        
                break
          
        elif seleccion == 3: # Statement que modifica propiedades individuales de cada producto en el inventario
            imprimirinventario()
            while True:
                que = int(input("Seleccione el número del producto que desee modificar: "))
                if que > len(inventario): # Se valida que el número insertado corresponda a un número de producto
                    print("Introdujo un número de producto fuera del rango de los que hay, pruebe otra vez\n ")
                    continue
                else:
                    break
            
            filadeproducto = inventario[que] # Se separa la lista adentro de una lista en una lista individual para modificarla con mayor facilidad
            
            seccion = input("Teclee la sección que desea modificar (nombre/cantidad/precio/Code): ")
            
            if seccion.lower() == "nombre":
                nombre = input("Ingrese el nuevo nombre que le quiere poner al producto: ")
                while len(nombre)<20:
                    nombre += " "
                filadeproducto[1] = nombre
                
                nombre = nombre.strip() # Modifica el nombre en lista de empleados
                while len(nombre)<20:
                    nombre += " "
                empleados[que][0] = nombre # En cada caso, se modifica otra propiedad del producto
                
            elif seccion.lower() == "cantidad":
                cantidad = int(input("Inserte la nueva cantidad del producto: "))
                filadeproducto[2] = cantidad
            
            elif seccion.lower() == "precio":
                cantidad = int(input("Inserte el nuevo precio del producto: "))
                filadeproducto[3] = cantidad
            
            elif seccion.lower() == "code":
                code = input("Inserte el nuevo código del producto: ")
                filadeproducto[4] = code
            
            #imprimirinventario()
            print("\n¡Listo! Producto modificado")
            
        break




def consultarproducto(): # Esta función sirve para que el usuario pueda ver la lista del inventario, o seleccionar un producto en particular para inspeccionarlo de mejor manera
    while True:
        print("1. Consultar todos los productos")
        print("2. Consultar un producto\n")
        que = int(input("¿Qué opción deseas? (1/2): "))
        if que == 1: # En la opción de mostrar todo el inventario, solo se usa la función previamente desarrollada al inicio del programa
            imprimirinventario()
            break
        elif que == 2: # En la opción de solo mostrar un item, se imprimen los encabezados de la tabla y se usa un for loop para que solo cuando el número de la iteración sea igual a la fila del producto, se imprima
            que2 = int(input("¿Qué producto deseas consultar? (Inserte su número): "))
            print("\n\n")
            n = 1
            for i in inventario: 
                for j in i:
                    if i == inventario[0]:
                        print(j, end=" ")  
                    elif i == inventario[que2]:
                        if n == 1:
                            print()
                        print(j, end="\t\t")
                        n += 1
                        
            print("\n\n")
            break
        else:
            print("\nNúmero fuera de rango, debe ser o 1 o 2, intente de nuevo")
            continue
                
            




def mainmenu(): # Ésta función es en la que se controla toda la estructura del sistema, las funciones que están en la parte de arriba sirven para desarrollar cada una de las tareas que puede hacer este programa, sin embargo esta es la función con la que se controla la estructura general
    while True:
        menu = ["Menú principal: ",
                "1. Registrar Ventas", # listo
                "2. Actualizar Inventario",
                "3. Consultar Ventas", # listo
                "4. Consultar Producto",
                "5. Salir"] # listo
        for i in menu:
            print(i)
        
        accion=input("\nSeleccione el número de la operación que desea realizar: ") # Dependiendo del número que se incerte en este input, se llamará a la función correspondiente que hace la tarea
        if accion == "1":
            registrarventas()
        elif accion == "2":
            actualizarinv()
        elif accion == "3":
            imprimirempleados()
        elif accion == "4":
            consultarproducto()
        elif accion == "5":
            salir = input("¿Seguro que deseas salir? (si/no): ")
            if salir.lower() == "si":
                exit() # Función para parar el programa completamente
            else:
                print("\nPerfecto, regresando al Menú principal\n\n")
                continue
        
        
mainmenu() # Llamado a función porncipal de estructura



