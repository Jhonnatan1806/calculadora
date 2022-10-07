def SepararDecimal(num):
	cont=0
	for i in range(len(numero)):
		if(num[i]=="."):
			break
		cont+=1
	decimal=num[cont+1:len(num)]
	decimal=float(decimal)/float(pow(10,len(decimal)))
	return decimal
def SepararEntero(num):
	cont=0
	for i in range(len(num)):
		if(num[i]=="."):
			break
		cont+=1
	entero=int(numero[0:cont])
	return str(entero)

def BinEntero(num): #creamos una funciona que transforma enterio a binario
	Entero=""
	while num>=1:
		a= int(num)%2
		num=num/2
		Entero=str(a)+Entero
	if(num==0):
		Entero=0
	return Entero
#creamos una funcion que transforme decimal a binario (el binario debe ser menor de que uno)
def BinDecimal(num):
	cont=0
	palabra=""
	while num!=1:
		num=2*num
		if num<1:
			palabra=palabra+"0"
		else:
			palabra=palabra+"1"
			num=str(num)
			num=SepararDecimal(num)
		cont+=1
		if cont==23:  #precision de 23 bits
			break	
	return palabra
#ingresamos un numero real y definimos las siguientes variables
numero=input("Ingrese un numero: ")
signo=""
exponente=""
mantisa=""
numRealBin=""
#verificamos si el numero es posiitivo o negativo
numero=float(numero)
if numero<0:
	numero=numero*(-1)
	signo="1"
	numero=str(numero)
else:
	signo="0"
	numero=str(numero)
#separamos la parte entera y decimal del numero
entero=int(SepararEntero(numero))
decimal=SepararDecimal(numero)
#convertimos la parte decimal y entera en binario
entero=str(BinEntero(entero))
print(entero)
decimal=BinDecimal(decimal)
numRealBin=entero+","+decimal
print("Numero Real a Binario: ",numRealBin," Con presicion de 23 bits")
#luego 







