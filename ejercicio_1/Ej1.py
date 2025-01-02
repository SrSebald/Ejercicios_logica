Banco_cliente = "Estado"
Cuenta_cliente = True
Saldo_cliente = 1100000
Banco_destino = "Santander"
Cuenta_destino =  True
Hora_transferencia = 9
Monto_transferencia = int(input("Indique la cantidad de la transferencia que quiere realizar:  "))
Costo_transferencia = 0

if Cuenta_cliente == True:
    if Cuenta_destino == True:
        if Banco_cliente == Banco_destino:
            Costo_transferencia = Costo_transferencia +  0
        else: 
            Costo_transferencia = Costo_transferencia + 100
            if Saldo_cliente >= Monto_transferencia + Costo_transferencia:
                if (Hora_transferencia >= 9 and Hora_transferencia <= 12) or (Hora_transferencia >= 15 and Hora_transferencia <= 20):
                    print("Transferencia realizada con éxito :-) ")
                else:
                    print("No se pueden realizar transferencias fuera de horarios")
            else: 
                print("El Monto ingresado excede el saldo en la cuenta")
         
    else:
        print("Cuanta de destino no valida")
else:
    print("Cuenta Cliente no valida")


