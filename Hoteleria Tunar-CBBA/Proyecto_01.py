#Hoteleria
print("    BIENVENIDO AL HOTEL TUNAR       ")
print("""
    Siga el registro porfavor
      """)
#Registro de datos del huésped 
#Nombre
while True:
  nombre_completo=input("Por favor, ingrese su nombre completo: ").strip()
  if len(nombre_completo)<3:
     print("Error:El nombre es demaciado corto. Intente nuevamente.")
  else:
     break 
#Documento CI
while True:
   documento=input("Ingrese su CI o Pasaporte: ").strip()
   if len(documento)<5 or len(documento)>12:
      print("Error:Documento invalido (Debe tener entre 5 a 12 caracteres.)")
   else:
      break
print("Registro completo con éxito.")
print("Accediendo al sistema...")   
 


