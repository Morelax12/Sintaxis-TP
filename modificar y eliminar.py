\\modificar por nombre 

 if tamanio(lista_ventas)==0
  print("No hay lisya para modificar\n")
 else 
  nombre=input("Ingrese el nombre del medicamento:") 
  i=1
  encontrado=False
  while i<=tamanio(lista_vacia)
   if verNombre(venta)==nombre
   print("\nVenta encontrada\n")
   
   nuevoimporte=float(input("Ingrese nuevvo importe\n"))
   cantidad=int(input("Ingrese nueva cantidad\n"))

   cargaVenta(venta,cod,nom,dro,os,plan,nuevoimporte)
   print("Venta modificado con exito\n")
   encontrado=True
   break
  
  if not encontrado
   print("No se encontro venta con ese nombre\n")
   
\\eliminar por codigo

if tamanio(lista_venta)==0
 print("No hay ventas para eliminar\n")
else
  codigo=int(input("Ingrese el codigo del medicamento a eliminar\n"))
  i=1
  eliminado=False
            
while i<=tamanio(lista_vanta)
   if verCodigo(venta)=codigo
     eliminarVenta(lista_ventas, venta)
     print("Venta eliminada con éxito.\n")
     eliminado = True
     break
  if not encontrado
  print("No se encontro venta con ese codigo\n")
