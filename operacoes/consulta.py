from banco import obterconta,banco
def consultasaldo(conta:int)->None:
    cliente = obterconta(conta)
    if cliente:
        print(f"saldo:{cliente['saldo']}")
    else:
        print('conta nao existe')
if __name__=='__main__':
    consultasaldo(1)
    print(banco)