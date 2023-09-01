from banco import obterconta , banco
def transferir(contaori:int,contades: int,valor:float)->None:
    contaorigem = obterconta(contaori)
    contadestino = obterconta(contades)
    if contaorigem and contadestino:
        if contaorigem['saldo'] >= valor:
            contaorigem['saldo'] -= valor
            contadestino['destino'] += valor
            print('Transferencia realizada com sucesso!')
        else:
            print('saldo insuficiente')

    else:
        print('uma ou mais contas nao existem!')
if __name__== '__main__' :
    transferir(1, 2, 159.99)
    print(banco)