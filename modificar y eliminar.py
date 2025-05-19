
#Modificar por nombre 
 if op==2:
  nombre=input("Ingrese el nombre del medicamento a modificar\n")
  encontrado=False
  nombre=input("Ingrese el nombre del medicamento:") 
  for i in range(1, tamanioVentas(ventas)+1):
   vent=recuperarVenta(ventas, i)
   if verNombre(vent)==nombre:
     encontrado=True
     control=True
     while control:
      print("\n¿Que quiere modificar?\n")
      print("\n1-Nombre del medicamento\n")
      print("\n2-Codigo\n")
      print("\n3-Importe\n")
      print("\n4-Facha y hora\n")
      print("\n5-Obra social\n")
      print("\n6-Droga\n")
      print("\n7-Salir\n")
      try:
        mod=int(input("Seleccionar:\n"))
      except ValueError:
        print("\nEl numero ingresado no es valido\n")
        continue
      if mod==1:
       nuevo=input("Ingrese nuevo nombre del medicamneto\n")
       modNombre(vent, nuevo)
      elif mod==2:
        nuevo=int(input("Ingrese codigo del medicamento\n"))
        modCodigo(vent, nuevo)
      elif mod==3:
        nuevo=float(input("Ingrese nuevo monto\n"))
        modImporte(vent, nuevo)
      elif mod==4:
        nuevo=input("Ingrese nuevo horario y fecha\n")
        modFechaHora(vent, nuevo)
      elif mod==5:
       nuevo=input("Ingrese nueva obra social\n")
       modObraS(vent, nuevo)
      elif mod==6:   
        nuevo=input("Ingrese nueva droga\n")
        modDroga(vent, nuevo)
      elif mod==7:
        control=False
      else:
        print("\nOpcion no valida\n")  
      break
  if not encontrado:
    print("No se encontro venta con el nombre solicitado\n")

   
#Eliminar por codigo
if tamanio(lista_venta)==0:
  print("No hay ventas para eliminar\n")
else:
  codigo=int(input("Ingrese el codigo del medicamento a eliminar\n"))
  i=1
  eliminado=False
 while i<=tamanio(lista_venta):
  venta=RecuperarVenta(lista_venta, i)
  if verCodigo(venta)==codigo:
     eliminarVenta(lista_ventas, venta)
     print("\nVenta eliminada con éxito.\n")
     eliminado = True
     break
  if not encontrado:
   print("No se encontro venta con ese codigo solicitado\n")

     
