#Una máquina expendedora necesita calcular el cambio que debe devolver. Escribe un programa que pida el importe de la compra y el dinero entregado por el cliente (ambos en euros, con decimales) y muestre:El cambio total que hay que devolver.El desglose del cambio con el menor número posible de billetes y monedas, usando billetes de 20 €, 10 € y 5 € y monedas de 2 €, 1 €, 50 cént., 20 cént., 10 cént. y 5 cént.
#Nombre:Saad Jlilou
#Fecha: 12/11/2026
importe=(float(input("Ingrese el valor del importe: ")))
dineroentregado=(float(input("Ingrese el valor del dinero: ")))
#Primero lo que e echo es pedir a la persona  los valores y los garde como numeros decimales
importe_cent= round(importe*100)
dineroentregado_cent=round(dineroentregado*100)
cambio_total=importe_cent-dineroentregado_cent
#despues he restado el dineroentregado menos el importe , para saber cuantos centimos tengo que delvolver
print (f"{cambio_total / 100:.2f}€")

cambio=cambio_total
b20 = cambio // 2000
cambio = cambio % 2000

b10 = cambio // 1000
cambio = cambio % 1000

b5 = cambio // 500
cambio = cambio % 500

m2 = cambio // 200
cambio = cambio % 200

m1 = cambio // 100
cambio = cambio % 100

m50 = cambio // 50
cambio = cambio % 50

m20 = cambio // 20
cambio = cambio % 20

m10 = cambio // 10
cambio = cambio % 10

m5 = cambio // 5
cambio = cambio % 5

#Con // y el porcentaje fui sacando cuantos billetes de 20 10 y 5  y todas las monedas caben , guardando lo que sobra en cambio
print(f"Billete de 20€:{b20}")
print(f"Billete de 10€:{b10}")
print(f"Billete de 5€:¨{b5}")
print(f"Monedas de 2€:{m2}")
print(f"monedas de 1€:{m1}")
print(f"monedas de 50 cent:{m50}")
print(f"monedas de 20 {m20}")
print(f"monedas de 10 {m10}")
print(f"monedas de 5 {m5}")
#al final he puesto los print para que se ejecuten