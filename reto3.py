from random import randint
print("Bienvenido al sistema de ubicación para zonas públicas WIFI")
nombreDeUsuario = int(input("Ingrese su usuario: "))

contrasena = 63615
menu = [" 1.Cambiar contraseña"," 2.Ingresar coordenadas actuales", " 3.Ubicar zona wifi más cercana", " 4.Guardar archivo con ubicación más cercana", " 5.Actualizar registros de zonas wifi desde archivo",
         " 6.Elegir opción de menú favorita", " 7.Cerrar sesión"]

#Función la cual contiene el resto de opciones del menú y se hace el llamado a la función de favoritos
def menuAdaptativo():
  intentos = 0

  while(intentos <= 2):
    for i in range(0, len(menu)):
     print(menu[i])

    opcion = int(input("Elija una opción: "))
    aux = opcion
    opcion -=1
    if(opcion == 0):
      opcion += 1
      cambioContrasena()
    elif(opcion == 1):
      opcion += 1
      ingresarCoordenadas()
      break
    elif(opcion == 2):
      opcion += 1
      print(f"Usted ha elegido la opción {opcion}")
      break
    elif(opcion == 3):
      opcion += 1
      print(f"Usted ha elegido la opción {opcion}")
      break
    elif(opcion == 4):
      opcion += 1
      print(f"Usted ha elegido la opción {opcion}")
      break
    elif(opcion == 5):
      favoritos()
    elif(opcion == 6):
        print("Hasta pronto")
        break
    elif(aux > 7):
      intentos += 1
      if(intentos ==3):
        print("Error")

#Función para que se pueda elegir la opción favorita de la persona
def favoritos():
  favorita = int(input("Seleccione opción favorita: "))
  if(favorita <=4 and favorita != 6 and favorita != 7):
    respuesta = int(input("Para confirmar por favor responda:\n¿Cuánto son tres medias moscas y mosca y media?: "))
    if(respuesta == 3):
      respuesta2 =int(input("Para confirmar por favor responda:\n¿Qué cosa será aquella que mirada del derecho y mirada del revés siempre un número es?:"))
      if(respuesta2 == 6):
        aux = favorita - 1
        quitando = menu.pop(aux)
        menu.insert(0,quitando)
      else:
        print("Error")       
    else:
        print("Error")
  else:
    print("Error")
    exit()


#Función para el cambio de contraseña
def cambioContrasena():
    nueva = int(input("Ingrese la nueva contraseña: "))
    if(nueva != contrasena and nueva != 0):
        confirmacion = int(input("Para hacer el cambio, por favor ingrese la contraseña anterior: "))
        if(confirmacion == contrasena):
            menuAdaptativo()
        else:
          print("Error")
          exit()
    else:
        print("Error")
        exit()
 
#función para imprimir una matriz
def imprimirMatrix (X):
  for i in range(3):
    for j in range(1):
      print(f"coordenada [latitud,longitud] {i+1} :", X[i], end="")
    print()

#Ingresar las coordenadas
Matriz = []
latitudSup = 6.306
latitudInf = 5.888
longitudOr = -72.321
longitudOcc = -72.552
def ingresarCoordenadas():
 if(len(Matriz) == 0):
  for i in range(3): # Ciclo de las filas
   aux_fila = []
   for j in range(1): # Ciclo de latitud
    latitud = float(input(f"ingrese latitud #{i+1}: "))
    if(latitudInf < latitud and latitud < latitudSup and latitud != None ):
      aux_fila.append(latitud)
    else:
     print("Error coordenada")
     exit()

    for k in range(1):# Ciclo de longitud
     longitud = float(input(f"ingrese longitud #{i+1}: "))
     if(longitudOcc < longitud and longitud < longitudOr and longitud != None):
      aux_fila.append(longitud)
     else:
      print("Error coordenada")
      exit()
   Matriz.append(aux_fila)#inserta los valores a la matriz
  menuAdaptativo()

 elif(len(Matriz) != 0):
   imprimirMatrix(Matriz)
   coordenadaAlSur()
   coordenadaAlOccidente()
   cambiarCoordenada()

def coordenadaAlSur():
  menor = Matriz[0][0]
  i = 0
  while(i < len(Matriz)):
    if(Matriz[i][0] < menor):
      menor = Matriz[i][0]
    i+=1
  print(f"la coordenada {menor} es la que está más al sur")

def coordenadaAlOccidente():
  menor = Matriz[0][1]
  i = 0
  while(i < len(Matriz)):
    if(Matriz[i][1] < menor):
      menor = Matriz[i][1]
    i+=1
  print(f"la coordenada {menor} es la que está más al occidente")

#Función para actualizar la coordenada que el usuario elija
def cambiarCoordenada():
  cambio = int(input("Presione 1,2 o 3 para actualizar la respectiva coordenadas\npresione 0 para regresar al menú "))
  if(cambio == 1 or cambio == 2 or cambio == 3):
    nueva_fila = []
    for i in range(len(Matriz[cambio - 1])):
      aux = float(input(f"Ingrese la nueva coordenada{i + 1}: ")) #se ingresan las nuevas coordenadas
      if(latitudInf < aux and aux < latitudSup and aux != None ):
        nueva_fila.append(aux)
      elif(longitudOcc < aux and aux < longitudOr and aux != None):
        nueva_fila.append(aux)
      else:
        print("Error")      
    Matriz[cambio - 1] = nueva_fila #acá se hace el cambio con los valores agregados en la matriz original
    menuAdaptativo()
  elif(cambio == 0):
    menuAdaptativo()
  else:
    print("Error actualización")
    exit()


#Funcion para iniciar sesión por parte del usuario 
def inicioDeSesion(): 
  if(nombreDeUsuario == 51636):
   contrasenaUsu = int(input("Ingrese su contraseña: "))
   if(contrasenaUsu == contrasena):
     numero1 = nombreDeUsuario % 1000
     numero2 = int(6/(6 % 5+1))
     suma = int(input("Ingrese la suma de " + str(numero1) + " + " + str(numero2) + " = "))   
     if(suma == 639):   
       menuAdaptativo()      
     else:
       print("Error")
   else:
      print("Error")
  else:
   print("Error")


inicioDeSesion()




