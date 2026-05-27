#======================PROYECTO HOTEL TUNARI======================
print("  \n  BIENVENIDO AL HOTEL TUNARI      ")
print("\nSiga el registro porfavor\n")
usuarios_registrados = {}
#======================MENÚ DE INICIO======================
while True:
 print("1.Iniciar sesion.")
 print("2.Crear una cuenta.")
 print("3.Salir.")
 prueba =input("\nSeleccione una opcion (1-3): ")
#======================INICIAR SESIÓN======================
 if prueba == "1":
   while True:
    nombre_completo=input("Por favor, ingrese su nombre completo: ").lower()
    if len(nombre_completo)<3:
     print("Error:El nombre es demaciado corto. Intente nuevamente.")
    else:
     break
#Documento CI
   while True:
     documento=input("Ingrese su CI o Pasaporte: ").strip()
     if not documento.isdigit():
      print("Error: El documento solo puede tener números (sin signo, ni letras)")
     elif len(documento)<5 or len(documento)>12:
      print("Error:Documento invalido (Debe tener entre 5 a 12 caracteres.)")

     else:
      #Verificamos el documento y usuario ingresado
      if documento in usuarios_registrados and usuarios_registrados[documento] == nombre_completo:
       print("\nCuenta de Usuario ingresada correctamente.")
       print("Registro completo con éxito.")
       print("Accediendo al sistema...\n")
       break
      else:
       print("Error: Los datos ingresados no coinciden o el usuario no esta registrado.")
       break
    
 #======================CREAR CUETA======================
 elif prueba == "2":
  while True:
   nuevo_usuario=input("Ingrese su nombre completo para crear la cuenta: ").lower()
   if len (nuevo_usuario)<3:
    print("Error:El nombre es demaciado corto. Intente nuevamente.")
   else:
       break
#Nuevo contraseña de usuario registrando
  while True:
    cedula=input("Ingrese su CI o Pasaporte a registrar: ").strip()
    if not cedula.isdigit():
     print("Error: El documento solo puede tener números (sin signo, ni letras)")
    elif len(cedula)<5 or len(cedula)>12:
      print("Error:Documento invalido (Debe tener entre 5 a 12 caracteres.)")
    else:
     #Guardamos informacion del nuevo registro.
      usuarios_registrados[cedula]=nuevo_usuario
      print(f"\nRegistro con éxito: {nuevo_usuario}")
      break

#======================SALIR======================    
 elif prueba == "3":
  print("Gracias por visitarnos, vuelva pronto.")
  break   
 else:
    print("Opcion invalida. Por favor, elija 1, 2 o 3.")