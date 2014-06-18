# -*- coding: iso8859-1 -*-

from collections import namedtuple

import menu


correspondenteReg = namedtuple("correspondenteReg", "id, nome")
listacorrespondente = []



def encontrar_correspondente(codigo):
    pos = -1
    for i in range (len(listacorrespondente)):
        if listacorrespondente[i].id == codigo:
            pos = i
            break
                            
    return pos


def inserir_correspondente():
    cod = input("Qual o codigo? ")

    pos = encontrar_correspondente(cod)

    if pos >= 0:
        print "C�digo j� existe"
        return

    #ler dados
    nome = raw_input("Qual o nome? ")
    
    registo = correspondenteReg(cod, nome)
    listacorrespondente.append(registo)


def pesquisar_correspondente():
    cod = input("Qual o codigo do correspondente a pesquisar? ")

    pos = encontrar_correspondente(cod)

    if pos == -1:
        print "N�o existe correspondente com esse c�digo"
        return

    print "C�digo: ", listacorrespondente[pos].id
    print "Nome: ", listacorrespondente[pos].nome
    


def listar_correspondente():
    for i in range (len(listacorrespondente)):
        print "C�digo: ", listacorrespondente[i].id
        print "Nome: ", listacorrespondente[i].nome
        
  

def eliminar_correspondente():
    cod = input ("C�digo do correspondente a eliminar --> ")
    pos = encontrar_correspondente(cod)

    if pos == -1:
        print "N�o existe correspondente com esse c�digo"
        return

    # TODO: Confirmar elimina��o
    listacorrespondente.pop(pos)


    
def alterar_correspondente():
    cod = input ("C�digo do correspondente a alterar --> ")
    pos = encontrar_correspondente(cod)

    if pos == -1:
        print "N�o existe correspondente com esse c�digo"
        return

    # s� altera o nome
    novonome = raw_input("Qual o nome? ")
    listacorrespondente[pos] = listacorrespondente[pos]._replace(nome=novonome)



        

def gerir():

    terminar = False

    while not terminar:
        op = menu.correspondentes()

        if op == '1':
            inserir_correspondente()
        elif op =='2':
            listar_correspondente()
        elif op == '3':
            pesquisar_correspondente()
        elif op == '4':
            alterar_correspondente()
        elif op == '5':
            eliminar_correspondente()
        elif op == '0':
            terminar = True




if __name__ == "__main__":
    print "Este programa n�o deve ser executado diretamente"










