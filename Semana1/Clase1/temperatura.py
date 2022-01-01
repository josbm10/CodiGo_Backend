import locale
locale.setlocale(locale.LC_ALL, '')
# PROGRAMA PARA CONVERTIR
# DATOS DE ENTRADA
tipocambio = 0
while(tipocambio == 0):
    monedaInicial = input("Ingrese temperatura a convertir(F/K/C): ")
    if(monedaInicial == "F"):
        montoInicial = float(input("Ingrese temperatura en " + monedaInicial + ": "))
        montoFinalF = float(montoInicial)
        montoFinalC = (float(montoInicial)-32)/1.8
        montoFinalK = (float(montoInicial) * 5/9)+273
        tipocambio = 4.067
    elif(monedaInicial == "K"):
        montoInicial = float(input("Ingrese temperatura en " + monedaInicial + ": "))
        montoFinalF = (float(montoInicial)-273)*1.8+32
        montoFinalC = float(montoInicial)-273
        montoFinalK = float(montoInicial)
        tipocambio = 4.886
    elif(monedaInicial == "C"):
        montoInicial = float(input("Ingrese temperatura en " + monedaInicial + ": "))
        montoFinalF = float(montoInicial)*1.8+32
        montoFinalC = float(montoInicial)
        montoFinalK = float(montoInicial)+273
        tipocambio = 4.886
    else:
        print("No selecciono una temperatura valida")
# PROCESO

# DATOS DE SALIDA
print("La temperatura de "+str(montoInicial)+" "+str(monedaInicial)+" es igual a: ")
print("Kelvin: " +str(montoFinalK)+" K")
print("Celsius: " +str(montoFinalC)+" °C")
print("Farentheit: " +str(montoFinalF)+" F" )

