#Definir variables
Descuento:float=0.20
igv:float
preciobase:float
preciocondescuento:float
preciofinal:float
#Datos de Entrada
preciobase=float(input("Ingrese el precio base del artículo:"))
#Proceso
preciocondescuento=preciobase-(preciobase*Descuento)
igv=preciocondescuento*0.18
preciofinal=preciocondescuento+igv
#Datos de Salida
print(f"El precio con descuento es: {preciocondescuento}")
print(f"El precio final es: {preciofinal}")
