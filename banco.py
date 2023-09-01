banco=[
    {'conta':1,'nome':'mariana','saldo':159.99 },
    {'conta':2,'nome':'jonas','saldo':205.50}
]
conta_atual=2
def adicionarconta(nome:str,saldo:float)->None:
    global conta_atual
    conta_atual +=1
    cliente= {
        'conta':conta_atual,
        'nome':nome,
        'saldo':saldo

    }
    banco.append(cliente)
    print('cliente cadastrado com sucesso!')
def consultarcliente(conta:int)->None:
    cliente= obterconta(conta)
    if cliente:
        print(f"N.conta:'{'conta'}")
        print(f"N.conta:{cliente['nome']}")
        print(f"saldo:{cliente['saldo']}")
    else:
        print('cliente nao existe')



def obterconta(conta:int) -> dict or None:
    for cliente in banco:
        if cliente['conta']==conta:
            return cliente
        return None

def deletarconta(conta:int) -> None:
    cliente =obterconta(conta)
    if cliente!=None:
        banco.remove(cliente)
        print('cliente deletado com sucesso!')
    else:
        print('cliente nao existe')

def editarnome(novoNome:str,conta:int)->None:
    cliente=obterconta(conta)
    if cliente:
        cliente['nome']=novoNome
        print('dados alterados com sucesso!')
    else:
        print('cliente nao existe')



def listartodascontas()->None:
    for cliente in banco:
        consultarcliente(cliente['conta'])
        print('>....................<')

if __name__ == '__main__':
 consultarcliente(1)
