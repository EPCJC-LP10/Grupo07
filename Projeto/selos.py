# -*- coding: iso8859-1 -*-
"""
Created on Fri Mar 21 11:42:06 2014

@author: i13354
"""

   
import menu


def inserir():
    
    codigo= input ("int. o codigo do selo")
    
    encontrou=False
    for i in range(len(selo)):
        if selo[i].codigo==codigo:
             encontrou=True
             break
    
    if encontrou:
        print 'esse codigo é repetido'
        return


    serie=input ("int. do serie do selo")
    ano=input ("int. o ano do selo")

    novo=novo_selo(codigo, serie, ano)

    selo.append(novo)
    

def listar_todos():
    if len(selo)==0:
        print 'nao existe selos inseridos'
        return
    for i in range(len(selo)):
        print 'codigo',selo[i].codigo
        print 'serie',selo[i].serie
        print 'ano',selo[i].ano
        print '---------'

def pesquisar():
    codigo = input("Qual o codigo do selo a pesquisar? ")

    pos = selo(codigo)

    if pos == -1:
        print "Não existe selo com esse código"
        return

    print "Codigo: ", selo[pos].codigo

        
def alterar():
    codigo= input ("int. codigo do selo")
    
    encontrou=False
    for i in range(len(selo)):
        if selo[i].codigo==codigo:
             encontrou=True
             pos=i
             break

    if not encontrou:
        print 'esse codigo nao existe'
        return

    novo_serie= input ("int. a serie do selo")
    novo_ano= raw_input ("int. o ano do selo")

    selo[pos]=selo[pos]._replace(tamnho=novo_serie, local=novo_ano)
    
def eleminar():
    codigo= input ("int. o codigo do selo")
    
    encontrou=False
    for i in range(len(selo)):
        if selo[i].codigo==codigo:
             encontrou=True
             pos=i
             break

    if not encontrou:
        print 'esse codigo nao existe'
        return
    
    selo.pop(pos)


def gerir():

    terminar = False

    while not terminar:
        op = menu.selos()

        if op == '1':
            inserir()
        elif op =='2':
            listar_todos()
        elif op == '3':
            pesquisar()
        elif op == '4':
            alterar()
        elif op == '5':
            eleminar()
        elif op == '0':
            terminar = True


from collections import namedtuple
novo_selo=namedtuple("novo_selo","codigo, serie, ano")

selo=[]

gerir()