from platform import system as plat
from os import system as command
from random import choice, sample

calcIMC = None
inPeso, inAlt = 0, 0
avgIdeal = 21.7
dias = ["LUNES","MARTES","MIÉRCOLES","JUEVES","VIERNES","SÁBADO","DOMINGO"]
genDieta, genRutina = None, None

def limpiarPantalla(): # Limpia la pantalla según el sistema operativo
    command("clear" if(plat() != "Windows") else "cls")

def imc(peso, altura): # Calcula el IMC
    return peso / (altura * altura)

def categoriaIMC(imc, error): # Categoriza el IMC según su valor
    categorias = ["Bajo peso", "Peso normal", "Sobrepeso", "Obesidad grado I",
                  "Obesidad grado II","Obesidad grado III"]
    
    if(0 < imc < 18.5):
        print(categorias[0])
    elif(18.5 <= imc <= 24.9):
        print(categorias[1])
    elif(25 <= imc <= 29.9):
        print(categorias[2])
    elif(30 <= imc <= 34.9):
        print(categorias[3])
    elif(35 <= imc <= 39.9):
        print(categorias[4])
    elif(40 <= imc):
        print(categorias[5])
    else:
        print(error)

def alejamiento(): # obtiene la diferencia entre el promedio del IMC ideal y el actual
    global calcIMC, avgIdeal

    try:
        return round(calcIMC - avgIdeal, 3)
    except:
        print("\aDebes calcular tu IMC primero\n")

def dieta(res): # Genera un plan de dieta
    global calcIMC, avgIdeal, dias, genDieta
    dec = None

    if(genDieta != None):
        print("Dieta guardada\n",*genDieta)

    if(0 <= abs(res) <= 3.2):
        print("Tu IMC indica un peso normal")
        while(1):
            dec = input("¿Deseas realizar una dieta? S/N -> ").upper()
            if(dec not in ("S","N")):
                print("Intenta de nuevo...\n")
            elif(dec == "S"):
                dec = input("¿Deseas (A)umentar o (D)isminuir de peso? -> ").upper()
                if(dec not in ("A","D")):
                    print("Comienza de nuevo...\n")
                else:
                    break
            else:
                return

    if(res < 0 or dec == "A"):
        print("\nDieta para aumentar de peso")

        while(True):
            generada = []
            aumento = {"desayuno": {"Pan adicionado con cereales integrales": (660, 4), "Sandwich": (252, 1),
                                "Huevos": (190, 1), "Yogur": (220, 3), "Manzana": (100, 1), "Plátano": (122, 1)},
                "dia": {"Barra de cereal": (200, 2), "Almendras": (600, 2), "Cacahuates": (600, 2), "Aguacate": (160, 2),
                        "Pistaches": (610, 2), "Nueces": (610, 2), "Chocolate oscuro": (560, 4), "Pasas": (150, 2), "Jugo": (150, 2)},
                "comida": {"Garbanzo": (290, 1), "Lentejas": (290, 1), "Arroz": (130, 2), "Pasta Integral": (180, 2), "Carne": (288, 1),
                            "Pescado": (120, 1)}}

            for i in range(len(dias)):
                if(dias[i] == "DOMINGO"):
                    generada.append("\n%s\n\tDía libre\n" % dias[i])
                else:
                    desayuno1, desayuno2 = sample(list(aumento["desayuno"]), 2)
                    comida = choice(list(aumento["comida"]))
                    dia1, dia2 = sample(list(aumento["dia"]), 2)
                    dia1 = (dia1, aumento["dia"][dia1])
                    dia2 = (dia2, aumento["dia"][dia2])

                    generada.append("\n%s\n\tDesayuno: %s y %s\n\tComida: %s\n\tDia: %s (%d porciones) y %s (%d porciones)"
                    % (dias[i], desayuno1, desayuno2, comida, dia1[0], dia1[1][1], dia2[0], dia2[1][1]))
            else:
                print(*generada)

                while(True):
                    dec = input("¿Deseas guardar la dieta? S/N -> ").upper()
                    if(dec not in ("S","N")):
                        print("Intenta de nuevo...\n")
                    elif(dec == "S"):
                        genDieta = generada
                        print("\n¡No te olvides de combinar tu plan de dieta con una rutina de ejercicios para lograr mejores resultados!\n")
                        return
                    else:
                        break
                while(True):
                    dec = input("¿Deseas generar otra dieta? S/N -> ").upper()
                    if(dec not in ("S","N")):
                        print("Intenta de nuevo...\n")
                    elif(dec == "S"):
                        break
                    else:
                        return
    elif(res > 3.2 or dec == "D"):
        print("\nDieta para disminuir de peso")

        while(True):
            generada = []
            dismin = {"desayuno": {"Huevos": (190, 1), "Yogur": (220, 3), "Manzana": (100, 1), "Plátano": (122, 1), "Avena": (20, 1),
                           "Pera": (46, 1)},
                      "dia": {"Almendras": (600, 2), "Cacahuates": (600, 2), "Pistaches": (610, 2), "Nueces": (610, 2),
                      "Fresas": (100, 3)},
                      "comida": {"Carne": (288, 1), "Salmón": (120, 1), "Pollo": (570, 1), "Atún": (170, 1)},
                      "verduras": {"Aguacate": (160, 2), "Camote": (172, 2), "Verduras verdes": (40, 4), "Papa": (100, 1),
                           "Berenjena": (25, 1)}}

            for i in range(len(dias)):
                desayuno1, desayuno2 = sample(list(dismin["desayuno"]), 2)
                comida = choice(list(dismin["comida"]))
                verdura = choice(list(dismin["verduras"]))
                dia1, dia2 = sample(list(dismin["dia"]), 2)
                dia1 = (dia1, dismin["dia"][dia1])
                dia2 = (dia2, dismin["dia"][dia2])

                generada.append("%s\n\tDesayuno: %s y %s\n\tComida: %s\n\tVerdura: %s\n\tDia: %s (%d porciones) y %s (%d porciones)\n"
                % (dias[i], desayuno1, desayuno2, comida, verdura, dia1[0], dia1[1][1], dia2[0], dia2[1][1]))
            else:
                print(*generada)

                while(True):
                    dec = input("¿Deseas guardar la dieta? S/N -> ").upper()
                    if(dec not in ("S","N")):
                        print("Intenta de nuevo...\n")
                    elif(dec == "S"):
                        genDieta = generada
                        print("\n¡No te olvides de combinar tu plan de dieta con una rutina de ejercicios para lograr mejores resultados!\n")
                        return
                    else:
                        break
                while(True):
                    dec = input("¿Deseas generar otra dieta? S/N -> ").upper()
                    if(dec not in ("S","N")):
                        print("Intenta de nuevo...\n")
                    elif(dec == "S"):
                        break
                    else:
                        return

def rutina(res):
    global calcIMC, avgIdeal, genRutina

    if(genRutina != None):
        print("RUTINA GUARDADA")
        print(*genRutina,sep="\n")

        while(True):
            dec = input("Ya existe una rutina generada\n"
                        "¿Deseas generar otra?\n"
                        "S/N -> ").upper()
            if(dec == "S"):
                break
            elif(dec == "N"):
                return
            else:
                print("Error, intenta de nuevo...")

    reps, generada = False, [[],[]]

    try:
        with open("ejercicios.txt","r") as ejerFile:
            pos = 0
            while(True):
                curr = ejerFile.readline()
                
                if(curr == "SEP\n"):
                    generada[pos].append("\n")
                elif(curr == "DSEP\n"):
                    pos += 1
                elif(curr == "FIN"):
                    break
                else:
                    generada[pos].append(curr)
    except FileNotFoundError as fe:
        print("\aEl archivo \"ejercicios.txt\" no ha sido encontrado.\nAgrega este archivo para poder generar las rutinas de ejercicio...\n")
        return

    if(0 <= abs(res) <= 3.2):
        print("Tu IMC indica un peso normal\n"
              "Advertencia: Una rutina intensa puede resultar perjudicial si no se ejecuta correctamente")
        reps = True

    print("\nRUTINA SUGERIDA")

    if(res < 0 or reps): # Rutina para aumentar de peso y definir musculatura
        print(*generada[0],sep="\n")
        genRutina = generada[0]
    elif(res > 3.2): # Rutina para bajar de peso
        print(*generada[1],sep="\n")
        genRutina = generada[1]

    print("¡No te olvides de combinar tu rutina de ejercicios con un plan de dieta para lograr mejores resultados!")

def nombreArchivo():
        prohibidos = ["<",">",":","\"","/","\\","|","?","*"]

        while(True):
            found = False
            nombre = input("Ingresa un nombre para tu archivo: ")
            for c in nombre:
                for p in prohibidos:
                    if(c == p):
                        found = True

                if(found):
                    break
            else:
                return nombre

            print("\nIngresa un nombre válido para tu archivo...\n") 

def exportarArchivo(elementos, modo=0):
        success = False

        try:
            if(not modo):
                with open("%s.txt" % nombreArchivo(), "x") as f:
                    for l in elementos:
                        f.write(l)
                    else:
                        success = True
            elif(modo == 1):
                count = 0
                with open("%s.txt" % nombreArchivo(), "x") as f:
                    for l in elementos:
                        if(isinstance(l,list)):
                            for ll in l:
                                f.write(ll)
                        else:
                            f.write(l)

                        f.write("\n\n")
                    else:
                        success = True
        except FileExistsError as fe: # Archivo ya existe
            print("¡El archivo ya existe!\nIntenta con otro nombre...\n")
        except Exception as e:
            print("Un error inesperado ha ocurrido, intenta de nuevo...\n")
            print(e)
        finally:
            if(success):
                print("¡Archivo creado con éxito!")

def exportarArchivos():
    global genDieta, genRutina

    if(genDieta== None and genRutina == None):
        print("Error: no hay información para generar ningún archivo aún.\nIntenta utilizar las herramientas del sistema...")
        return

    if(genDieta == None):
        print("Advertencia: no se ha generado ninguna dieta aún...")
    
    if(genRutina == None):
        print("Advertencia: no se ha generado ninguna rutina de ejercicios aún...")

    while(True):
        modo = input("Selecciona qué archivo deseas exportar\n"
                      "D - Dieta\n"
                      "R - Rutina\n"
                      "A - Ambos\n"
                      "-> ").upper()
        if(modo in ("D","R","A")):
            break
        else:
            print("Ingresa una opción válida...\n")   

    if(modo == "A" and genDieta != None and genRutina == None): # Ambos
        print("\nArchivo para dieta")
        exportarArchivo(genDieta)

        print("\nArchivo para rutina")
        exportarArchivo(genRutina)
    elif(modo == "D" and genDieta != None): # Dieta
        exportarArchivo(genDieta)
    elif(modo == "R" and genRutina != None): # Rutina
        exportarArchivo(genRutina)
    else:
        print("\n\aError, vuelve a intentar...\n")

def imprimirPantalla():
    global calcIMC, inPeso, inAlt, genDieta, genRutina

    if(calcIMC == None):
        print("¡No hay información para guardar!")
        return

    dumpIMC = "Último IMC calculado: %.2f con peso %.2f y altura %.2f\n\n" % (calcIMC, inPeso, inAlt)

    if(genDieta== None and genRutina == None):
        print("Advertencia: no se utilizaron las herramientas del sistema\n"
              "Únicamente se imprimirá el IMC")
        exportarArchivo([dumpIMC])
        return
    elif(genDieta == None):
        print("Advertencia: no se generó una dieta")
        exportarArchivo([dumpIMC, genRutina], 1)
        return
    elif(genRutina == None):
        print("Advertencia: no se generó una rutina")
        exportarArchivo([dumpIMC, genDieta], 1)
        return
    
    exportarArchivo([dumpIMC, genDieta, genRutina], 1)

def menu(): # Despliega el menú y retorna la opción seleccionada
    global calcIMC, inPeso, inAlt
    
    while(True):
        try:
            return int(input("\nSelecciona una opción\n"
                             "1.- %s\n"
                             "2.- Plan de dieta\n"
                             "3.- Rutina de ejercicios\n"
                             "4.- Exportar archivos\n"
                             "5.- Limpiar pantalla\n"
                             "6.- Salir\n"
                             "-> "
            % ("Calcular IMC" if(calcIMC == None) else "Nuevo IMC (Peso: %.2f, Altura: %.2f, IMC: %.2f)" % (inPeso,inAlt,calcIMC))))
        except:
            print("\aIngresa una opción válida...\n")

if(__name__ == "__main__"): # Para ejecutar como módulo principal
    error = "\aUn error inesperado ha ocurrido, intenta de nuevo...\n"
    
    print("----- BIENVENID@ -----")

    while(True):
        dec = menu()
        print("\n")

        if(dec == 1): # Calcular IMC
            while(True):
                try:
                    inPeso = float(input("Ingresa el peso en KG -> "))
                    inAlt = float(input("Ingresa la altura en METROS -> "))

                    if(0 >= inPeso or inPeso >= 600):
                        print("Peso inválido, intenta de nuevo...\n")
                    elif(0 >= inAlt or inAlt >= 2.5):
                        print("Altura inválida, intenta de nuevo...\n")
                    else:
                        calcIMC = round(imc(inPeso, inAlt),1)
                        break
                except:
                    print("Revisa tus entradas...\n")

            print("\nEl IMC calculado es: %.2f\nEstado: " % calcIMC, end="")
            categoriaIMC(calcIMC, error)
        elif(dec == 2): # Obtener plan de dieta
            res = alejamiento()

            if(res):
                dieta(res)
        elif(dec == 3): # Obtener rutina de ejercicio
            res = alejamiento()

            if(res):
                rutina(res)
        elif(dec == 4): # Exportar dieta y archivos
            exportarArchivos()
        elif(dec == 5): # Limpiar pantalla
            limpiarPantalla()
        elif(dec == 6): # Salir
            imprimirPantalla()
            input("Gracias por usar nuestro programa, ¡Hasta pronto!"
                  "\nPresiona ENTER para continuar...")
            exit()
