from banco import obterconta,banco
def depositar(conta:int,valor:float)->None:
    cliente=obterconta(conta)
    if cliente:
        cliente['saldo']=cliente['saldo']+valor
    else:
        print('deposito realizado com sucesso!')

if __name__=='__main__':
    depositar(1, 300)
    print(banco)