#Hoteleria
print("    BIENVENIDO AL HOTEL TUNAR       ")
print("""
    Siga el registro porfavor
      """)
#Registro de datos del huésped 
#Nombre
while True:
  nombre_completo=input("Por favor, ingrese su nombre completo: ").strip().title()
  if len(nombre_completo)<3:
     print("Error:El nombre es demaciado corto. Intente nuevamente.")
  elif " " in nombre_completo:
    print("Error: El nombre no puede contener espacion en blanco")
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
      print("Cuenta de Usuario ingresado correctamente.")
      break
print("Registro completo con éxito.")
print("Accediendo al sistema...")   
print(" ")

 #Menu
while True:
   print("            MENÚ - HOTEL TUNARI-CBBA             ")
   print(" ")#Espacio
   print("1.Habitaciones y Reserva.")
   print("2.Cancela una reserva.")
   print("3.SALIR.Cerrar session")

   #Creamos la opcion de escoger
   opcion=input("Seleccione una opción (1-3): ").strip().upper()
   if opcion == "1":
      print("""    Habitaciónnes y Reserva   
            """)
      while True:
         print("""Submenú: Habitaciones y Reserva
               """)
         print("1.Habitacion 101 - Simple Tropical")
         print("2.Habitación 102 - Marimonial Chapare")
         print("3.Habitacion 103 - Doble Familiar")
         print("4.Habitacion 104 - Suite Presidencial Tunari")
         print("5.Volver al menu principal")

         select=input("Seleccione una opcion (1-5): ")
         if select == "1":
            print("""   
                  Habitacion  101 - Simple Tropical 
                  """)
            print("Cost por noche: 70 bs; Cama: 1 Simple.")
            while True:
             print("""
               ¿Desea hacer una reserva de habitación?
                   """)
             print("1.SI.")
             print("2.Volver al menu.")
            
             slc=input("Seleccione una opcion(1-2): ")
             if slc == "1":
                  print("""
                  Siga las instrucciones.
                       """)
                  precio=70
                  print("Modo de ingresar fecha ej: 25.05")  
                  fecha_entrada=float(input("Ingrese la fecha que desea ingresar: "))
                  fecha_salida=float(input("Ingrese la fecha que desea salir del hotel: "))
               
                  print("  ")
                  resta=fecha_salida-fecha_entrada
                  
                  if resta<=0:
                   print("Error:La fecha de salida debe ser mayor.") 
                  else:
                   total=resta*precio
                   print("Se realiso con exito su reserva",nombre_completo,", el total del costo es de:",total,"bs gracias por su preferencia.")
                   print(" ")
                   break
             elif slc == "2":
               print("Voviendo al menu.")
               break     
             else: 
               print("Error:Opcion no valida")
            break  
                               #2
         if select == "2":
            print("""   
                  Habitacion  102 - Matrimoniel Chapare 
                  """)
            print("Cost por noche: 150 bs; Cama: 1 grande de 2/5.")
            while True:
             print("""
               ¿Desea hacer una reserva de habitación?
                   """)
             print("1.SI.")
             print("2.Volver al menu.")
             slc=input("Seleccione una opcion(1-2): ")
             if slc == "1":
                  print("""
                  Siga las instrucciones.
                       """)
                  precio=150
                  print("Modo de ingresar fecha ej: 25.05")  
                  fecha_entrada=float(input("Ingrese la fecha que desea ingresar: "))
                  fecha_salida=float(input("Ingrese la fecha que desea salir del hotel: "))
               
                  print("  ")
                  resta=fecha_salida-fecha_entrada
                  
                  if resta<=0:
                   print("Error:La fecha de salida debe ser mayor.") 
                  else:
                   total=resta*precio
                   print("Se realiso con exito su reserva",nombre_completo,", el total del costo es de:",total,"bs gracias por su preferencia.")
                   print(" ")
                   break
             elif slc == "2":
              print("Volviendo al menu.")
              break    
             else:
               print("Error:Opcion no valida.")   
            break  
         if select == "3":
            print("""   
                  Habitacion  103 - Doble Familiar
                  """)
            print("Cost por noche: 160 bs; Cama: 3, 2 grandes y 1 simple.")
            while True:
             print("""
               ¿Desea hacer una reserva de habitación?
                   """)
             print("1.SI.")
             print("2.Volver al menu.")
            
             slc=input("Seleccione una opcion(1-2): ")
             if slc == "1":
                  print("""
                  Siga las instrucciones.
                       """)
                  precio=160
                  print("Modo de ingresar fecha ej: 25.05")  
                  fecha_entrada=float(input("Ingrese la fecha que desea ingresar: "))
                  fecha_salida=float(input("Ingrese la fecha que desea salir del hotel: "))
               
                  print("  ")
                  resta=fecha_salida-fecha_entrada
                  
                  if resta<=0:
                   print("Error:La fecha de salida debe ser mayor.") 
                  else:
                   total=resta*precio
                   print("Se realiso con exito su reserva",nombre_completo,", el total del costo es de:",total,"bs gracias por su preferencia.")
                   print(" ")
                   break
             elif slc == "2":
               print("Volviendo al menu.")
               break
             else:
               print("Error:Opcion no valida.")     
            break  
         if select == "4":
            print("""   
                  Habitacion  104 - Suite Presidencial Tunari
                  """)
            print("Cost por noche: 190 bs; Cama: 1 Extra Grande.")
            while True:
             print("""
               ¿Desea hacer una reserva de habitación?
                   """)
             print("1.SI.")
             print("2.Volver al menu.")
            
             slc=input("Seleccione una opcion(1-2): ")
             if slc == "1":
                  print("""
                  Siga las instrucciones.
                       """)
                  precio=190
                  print("Modo de ingresar fecha ej: 25.05")  
                  fecha_entrada=float(input("Ingrese la fecha que desea ingresar: "))
                  fecha_salida=float(input("Ingrese la fecha que desea salir del hotel: "))
               
                  print("  ")
                  resta=fecha_salida-fecha_entrada
                  
                  if resta<=0:
                   print("Error:La fecha de salida debe ser mayor.") 
                  else:
                   total=resta*precio
                   print("Se realiso con exito su reserva",nombre_completo,", el total del costo es de:",total,"bs gracias por su preferencia.")
                   print(" ")
                   break
             elif slc == "2" :
               print("Volviendo al menu")
               break    
             else:
               ("Error:Opcion no valida.")
            break
         if select == "5":
             print("Volviendo al menu.")
             break
         else:
           print("Error:Opcion invalida.")

#     CANCELAR UNA RESERVA
   if opcion == "2":
      print("     CancelaR una Reserva      ") 
      while True:
        print("""
               ¿Que habitacion desea cancelar la reserva?
              """)   
        print("1.Habitación 101 - Simple Tropical")
        print("2.Habitación 102 - Matrimonial Chapare")
        print("3.Habitacion 103 - Doble Familiar")
        print("4.Habitacion 104 - Suite Presidencial Tunari")
        print("5.Volver al menu")
        print(" ")
        change=input("Seleccione la habitación que desea cancelar (1-5): ").strip().upper()
        if change == "1":
          print("""
                    ¿Esta seguro que desea cancelar esta reserva?
                """)
          print("1.SI, confirmar Cancelacion.")
          print("2.NO, regresar al menu.")
          print(" ")
          conf=input("Seleccione una opcion (1-2): ").strip()
          if conf == "1":
            print("La habitacion fue cancelada 101 - Simple Tropical fue cancelada.")
          elif conf == "2":
            print("""Operacion Cancelada.
                  """)
            break
          else:
            print("Opcion no valida")

        if change == "2":
          print("""
                    ¿Esta seguro que desea cancelar esta reserva?
                """)
          print("1.SI, confirmar Cancelacion.")
          print("2.NO, regresar al menu.")
          print(" ")
          conf=input("Seleccione una opcion (1-2): ").strip()
          if conf == "1":
            print("La habitacion fue cancelada 102 - Matrimonial Chapare fue cancelada.")
          elif conf == "2":
            print("""Operacion Cancelada.
                  """)
            break
          else:
            print("Opcion no valida")

        if change == "3":
          print("""
                    ¿Esta seguro que desea cancelar esta reserva?
                """)
          print("1.SI, confirmar Cancelacion.")
          print("2.NO, regresar al menu.")
          print(" ")
          conf=input("Seleccione una opcion (1-2): ").strip()
          if conf == "1":
            print("La habitacion fue cancelada 103 - Doble  Familiar fue cancelada.")
          elif conf == "2":
            print("""Operacion Cancelada.
                  """)
            break
          else:
            print("Opcion no valida")

        if change == "4":
          print("""
                    ¿Esta seguro que desea cancelar esta reserva?
                """)
          print("1.SI, confirmar Cancelacion.")
          print("2.NO, regresar al menu.")
          print(" ")
          conf=input("Seleccione una opcion (1-2): ").strip()
          if conf == "1":
            print("La habitacion fue cancelada 104 - Suite Presidencial Tunari fue cancelada.")
          elif conf == "2":
            print("""Operacion Cancelada.
                  """)
            break
          else:
            print("Opcion no valida")

        if change == "5":
          print("""
                    Volviendo al menu.
                """)
          break 
   if opcion == "3":
     print("Cerrando sesion, Vuelve pronto",nombre_completo,"gracias por su preferencia.")
   break