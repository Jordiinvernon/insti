print ('BIENVENIDO A LA CALCULADORA DE JORDI!')
respuesta2="si"
while respuesta2=="si":

 respuesta = input('que calculo quieres hacer? sumar,restar,multiplicar,dividir,ecuacion o área de un cuadrado:')

 if respuesta =="sumar":
    sumando1 = int(input("Introduzca el primer sumando: "))
    sumando2 = int(input("Introduzca el segundo sumando: "))
    print("Resultado de la suma: ", sumando1 + sumando2)

 elif respuesta =="multiplicar":
    multiplica1 = int(input("Introduzca el primer multiplica: "))
    multiplica2 = int(input("Introduzca el segundo multiplica: "))
    print("Resultado de la multiplicacio: ", multiplica1 * multiplica2)

 elif respuesta =="restar":
    resta1 = int(input("Introduzca el primer resta: "))
    resta2 = int(input("Introduzca el segundo resta: "))
    print("Resultado de la resta: ", resta1 - resta2)

 elif respuesta =="dividir":
    dividendo = float(input("Introduzca el dividendo: "))
    divisor = float(input("Introduzca el divisor: "))
    resultado = round(dividendo / divisor)
    print("Resultado de la division: ", resultado)

 elif respuesta =="área de un cuadrado":
    lado = float(input("introduzca el lado del quadrado:"))
    print("área:", lado*lado)

 elif respuesta=="ecuacion":
    print('introduce a b c(a no puede ser 0):')
    a = float(input("introduzca el valor de a:"))
    b = float(input("introduzca el valor de b:"))
    c = float(input("introduzca el valor de c:"))
    t = float((b*b) - (4*a*c))**(1/2)
    if a == 0:
      print("No es una ecuacion de segundo grado")
      
    else:
      x1 = ((-b + t) / (2 * a))
      x2 = ((-b - t) / (2 * a))
    
      print('Solución 1:', x1)
      print('Solución 2:', x2)

 print("Ahora quieres hacer otro calculo?")
 respuesta2 = input("si o no:")
 print ("HASTA LA PRÓXIMA!")






juego
print('En este juego tengo que adivinar el número que piensas.')
print('Piensa un número.')
print('Primero multiplica por 3 tu número.')
azul = int(input("Introduzca tu número: "))
rosa = int(input("Introduzca el 3: "))
print("Resultado: ", azul * rosa)

print('Ahora sumale 14.')
naranja = int(input("Introduzca el resultado anterior: "))
rojo = int(input("Introduzca el 14: "))
print("Resultado: ", naranja + rojo)

print('sumale el número que pensaste.')
naranj = int(input("Introduzca el resultado anterior: "))
roj = int(input("Introduzca tu número: "))
print("Resultado: ", naranj + roj)

print('Ahora restale 2.')
verde = int(input("Introduzca el resultado anterior: "))
morado = int(input("Introduzca el 2: "))
print("Resultado: ", verde - morado)

print('Ahora divide entre 4.')
blanco = int(input("Introduzca el resultado anterior: "))
negro = int(input("Introduzca el 4: "))
print("Resultado: ", blanco / negro)

print('Por último restale 3.')
dios = int(input("Introduzca el resultado anterior: "))
demonio = int(input("Introduzca el 3: "))
print("Tu número és: ", dios - demonio)
