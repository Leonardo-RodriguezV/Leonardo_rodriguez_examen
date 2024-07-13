#Reportes_empresa
import random
import statistics
import csv


trabajadores = [
    "Juan Pérez", "María García", "Carlos López", "Ana Martínez", 
    "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez", 
    "Isabel Gómez", "Francisco Díaz", "Elena Fernández"
]

sueldos = []

def is_num():
    while True:
        try:
            x = input("Ingrese una opción: ")
            x = int(x)
            return x
        except ValueError:
            print("Error, debe ingresar un número, reintente.")

def asignar_sueldos():
    global sueldos
    sueldos = [random.randint(300000, 2500000) for _ in range(10)]
    print("Sueldos asignados aleatoriamente.")



def clasificar_sueldos():
    global sueldos 
    
    bajo = min[300000]
    entre= [300001 and 2499999 ]
    alto = max[2500000]
    
    for i in range(len(trabajadores)):
        if sueldos[i] < 800000:
            bajo.append((trabajadores[i], sueldos[i]))
        elif sueldos[i] >= 800000 and sueldos[i] <= 2000000:
            entre.append((trabajadores[i], sueldos[i]))
        else:
            alto.append((trabajadores[i], sueldos[i]))
    
    print("Sueldos menores a $800.000")
    print(f"TOTAL: {len(bajo)}")
    for nombre, sueldo in bajo:
        print(f"{nombre} ${sueldo}")
    
    print("\nSueldos entre $800.000 y $2.000.000")
    print(f"TOTAL: {len(entre)}")
    for nombre, sueldo in entre:
        print(f"{nombre} ${sueldo}")
    
    print("\nSueldos superiores a $2.000.000")
    print(f"TOTAL: {len(alto)}")
    for nombre, sueldo in alto:
        print(f"{nombre} ${sueldo}")
    
    print(f"\nTOTAL SUELDOS: ${sum(sueldos)}")

def ver_estadisticas():
    if not sueldos:
        print("Aún no se han asignado sueldos.")
        return
    
    sueldo_maximo = max(sueldos)
    sueldo_minimo = min(sueldos)
    promedio_sueldos = statistics.mean(sueldos)
    media_geometrica = statistics.geometric_mean(sueldos)
    
    print(f"Sueldo más alto: {sueldo_maximo}")
    print(f"Sueldo más bajo: {sueldo_minimo}")
    print(f"Promedio de sueldos: {promedio_sueldos}")
    print(f"Media geométrica de sueldos: {media_geometrica}")

def generar_reporte():
    if not sueldos:
        print("No se ha asignado Sueldo.")
        return
    
    descuento_salud = 0.07
    descuento_afp = 0.12
    
    print("Nombre Empleado, Sueldo Base, Descuento Salud, Descuento AFP, Sueldo Líquido")
    
    for i in range(len(trabajadores)):
        sueldo_base = sueldos[i]
        desc_salud = sueldo_base * descuento_salud
        desc_afp = sueldo_base * descuento_afp
        sueldo_liquido = sueldo_base - desc_salud - desc_afp
        
        print(f"{trabajadores[i]}, {sueldo_base}, {desc_salud}, {desc_afp}, {sueldo_liquido}")

        with open("trabajadores.csv", "w", newline='') as csvfile:
         fieldnames = ["Trabajadores", "Sueldo Base", "Dsct.Salud", "Dsct.AFP", "Sueldo Liquido"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for i in range(trabajadores):
        if trabajadores[i, 0] != "":
            writer.writerow({
                "Nombre": trabajadores[i, 0],
                "Sueldo Base": sueldo_base[i, 1],
                "Dsct.Salud": desc_salud[i, 2],
                "Dsct.AFP": desc_afp[i, 3],
                "Sueldo Liquido": sueldo_liquido[i, 4]
            })



def salir_del_programa():
    print("Finalizando el programa...")
    print("Desarrollado por Leonardo Rodriguez ")
    print("Rut 19.876.948-7")
    exit()



def show_menu():
        
        print("\n-- Menu de Reportes --")
        print("1. Asignar sueldos aleatorios")
        print("2. clasificacion de sueldos")
        print("3. Ver estadísticas")
        print("4. Reporte de sueldos")
        print("5. Salir del programa")
        


        
while True:
    show_menu()
    opcion = is_num()
    if opcion == "1":
            asignar_sueldos()
    elif opcion == "2":
            clasificar_sueldos()
    elif opcion == "3":
            ver_estadisticas()
    elif opcion == "4":
            generar_reporte()
    elif opcion == "5":
            salir_del_programa()
            print("Finalizando el programa...")
            print("Desarrollado por Leonardo Rodriguez ")
            print("Rut 19.876.948-7")
            break
    else:
            print("Opción inválida. Intente nuevamente.")

