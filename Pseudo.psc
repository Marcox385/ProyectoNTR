SubProceso valor <- imc (peso, altura)
	valor <- peso / (altura^2)
FinSubProceso

SubProceso valor <- dieta ()
	Escribir "Generar dieta basada en IMC"
	Escribir "Guardar dieta en variable global"
FinSubProceso

SubProceso valor <- rutina ()
	Escribir "Generar rutina de ejercicios basada en IMC"
	Escribir "Guardar rutina fija en variable global"
FinSubProceso

SubProceso valor <- exportar ()
	Escribir "Selecciona qué archivo deseas exportar"
	Escribir "D - Dieta"
	Escribir "R - Rutina"
	Escribir "A - Ambos"
	Leer seleccion
	
	Si seleccion == "D" Entonces
		Escribir "Exportar archivo de dieta"
	SiNo
		Si seleccion == "R" Entonces
			Escribir "Exportar archivo de rutina de ejercicios"
		SiNo
			Si seleccion == "A" Entonces
				Escribir "Exportar ambos archivos"
			SiNo
				Escribir "Error en selección"
			FinSi
		FinSi
	FinSi
FinSubProceso

SubProceso decision <- menu ()
	Escribir ""
	Escribir "Selecciona una opción"
	Escribir "1.- Calcular IMC"
	Escribir "2.- Plan de dieta"
	Escribir "3.- Rutina de ejercicios"
	Escribir "4.- Exportar archivos"
	Escribir "5.- Limpiar pantalla"
	Escribir "6.- Salir"
	Leer decision
Fin SubProceso


Proceso main
	Dimension categorias[6]
	categorias[0] <- "Bajo peso"
	categorias[1] <- "Peso normal"
	categorias[2] <- "Sobrepeso"
	categorias[3] <- "Obesidad grado I"
	categorias[4] <- "Obesidad grado II"
	categorias[5] <- "Obesidad grado III"
	error <- "Un error inesperado ha ocurrido, intenta de nuevo..."
	
	Escribir "----- BIENVENID@ -----"
	
	
	Definir peso como real
	Definir altura como real
	
	control1 <- 1
	Mientras control1 = 1 Hacer
		decision <- menu()
		Escribir ""
		Segun decision Hacer
			1:
				control2 <- 1
				Mientras control2 = 1 Hacer
					Escribir "Ingresa el peso en KG " sin saltar
					Leer peso
					
					Escribir "Ingresa la altura en METROS " sin saltar
					Leer altura
					
					Si 0 >= peso O peso >= 600 Entonces
						Escribir "Peso inválido, intenta de nuevo..."
					SiNo
						Si 0 >= altura O altura >= 2.5 Entonces
							Escribir "Altura inválida, intenta de nuevo..."
						SiNo
							calcImc <- redon(imc(peso, altura))
							control2 <- 0
						FinSi
					FinSi
				FinMientras
				
				Escribir "El IMC calculado es: " + ConvertirATexto(calcImc)
				Escribir "Estado: " sin saltar
				
				Si 0 < calcImc Y calcImc < 18.5 Entonces
					Escribir categorias[0]
				SiNo
					Si 18.5 <= calcImc Y calcImc <= 24.9 Entonces
						Escribir categorias[1]
					SiNo
						Si 25 <= calcImc Y calcImc <= 29.9 Entonces
							Escribir categorias[2]
						SiNo
							Si 30 <= calcImc Y calcImc <= 34.9 Entonces
								Escribir categorias[3]
							SiNo
								Si 35 <= calcImc Y calcImc <= 39.9 Entonces
									Escribir categorias[4]
								SiNo
									Si 40 <= calcImc Entonces
										Escribir categorias[5]
									SiNo
										Escribir error
									FinSi
								FinSi
							FinSi
						FinSi
					FinSi
				FinSi
			2:
				Escribir "Calcular alejamiento"
				Escribir dieta()
			3:
				Escribir "Calcular alejamiento"
				Escribir rutina()
			4:
				Escribir exportar()
			5:
				Limpiar Pantalla
			6:
				Escribir "Gracias por usar nuestro programa, ¡Hasta pronto!"
				control1 <- 0
		FinSegun
	Fin Mientras	
FinProceso	
